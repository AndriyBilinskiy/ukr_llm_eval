#!/bin/bash

# Detect available device
DEVICE="cpu"

if python -c "import torch; print(torch.cuda.is_available())" | grep "True"; then
    DEVICE="cuda"
elif python -c "import torch; print(torch.backends.mps.is_available())" | grep "True"; then
    DEVICE="mps"
fi

echo "Using device: $DEVICE"

echo "Using splits: $SPLITS"
echo "Number of samples per split: $NUM_SAMPLES_PER_SUBSET"
echo "Using models: $MODELS"

# Detect the number of available GPUs
NUM_GPUS=$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)
echo "Detected $NUM_GPUS GPUs."


# Set PyTorch memory optimization to reduce fragmentation
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"

IFS=',' read -r -a MODEL_ARRAY <<< "$MODELS"

for MODEL in "${MODEL_ARRAY[@]}"; do
    echo "Processing model: $MODEL"
    OUTPUT_DIR="${HOME}/workspace/output/${MODEL}"
    mkdir -p "$OUTPUT_DIR"  # Ensure output directory exists

    echo "Loading model $MODEL with tensor_parallel_size=$NUM_GPUS..."

    # Run the evaluation with multi-GPU distributed inference
    lm_eval \
        --model vllm \
        --device "$DEVICE" \
        --model_args pretrained="$MODEL",tensor_parallel_size="$NUM_GPUS",dtype="bfloat16",gpu_memory_utilization=0.95,enforce_eager=True,max_model_len=1200 \
        --include_path ./ \
        --tasks "$SPLITS" \
        --output "$OUTPUT_DIR" \
        --log_samples || { echo "Error: lm_eval failed for model $MODEL"; exit 1; }

    echo "Completed processing model: $MODEL"
done

echo "All models processed successfully."