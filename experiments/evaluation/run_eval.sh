#!/bin/bash
DEVICE="cpu"

# Check if CUDA is available
if python -c "import torch; print(torch.cuda.is_available())" | grep "True"; then
    DEVICE="cuda"
elif python -c "import torch; print(torch.backends.mps.is_available())" | grep "True"; then
    DEVICE="mps"
fi

echo "Using device: $DEVICE"
echo "Using splits: $SPLITS"
echo "Number of samples per split: $NUM_SAMPLES_PER_SUBSET"
echo "Using model: $MODELS"

IFS=',' read -r -a MODEL_ARRAY <<< "$MODELS"

for MODEL in "${MODEL_ARRAY[@]}"; do
  echo "Processing model: $MODEL"
  OUTPUT_DIR="${HOME}/workspace/output/${MODEL}"

  lm_eval \
    --model hf \
    --device "$DEVICE"\
    --model_args pretrained="$MODEL" \
    --include_path ./ \
    --tasks "$SPLITS" \
    --output "$OUTPUT_DIR" \
    --log_samples
done