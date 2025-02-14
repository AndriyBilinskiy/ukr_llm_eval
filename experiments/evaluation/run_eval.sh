#!/bin/bash
DEVICE="cpu"

# Check if CUDA is available
if python -c "import torch; print(torch.cuda.is_available())" | grep "True"; then
    DEVICE="cuda"
fi

echo "Using device: $DEVICE"
echo "Using splits: $SPLITS"
echo "Number of samples per split: $NUM_SAMPLES_PER_SUBSET"
echo "Using model: $MODELS"

# Define splits
IFS=',' read -r -a SPLIT_ARRAY <<< "$SPLITS"
IFS=',' read -r -a MODEL_ARRAY <<< "$MODELS"

for MODEL in "${MODEL_ARRAY[@]}"; do
  for SPLIT in "${SPLIT_ARRAY[@]}"; do
    echo "Processing model: $MODEL"
    echo "Processing split: $SPLIT"
    sed -i "s|VALIDATION_SPLIT_PLACEHOLDER|$SPLIT|g" /workspace/config.yaml
    OUTPUT_DIR="/workspace/output/${SPLIT}/${MODEL}"

    lm_eval \
      --model hf \
      --device "$DEVICE"\
      --model_args pretrained="$MODEL" \
      --include_path ./ \
      --tasks config \
      --output "$OUTPUT_DIR" \
      --limit "$NUM_SAMPLES_PER_SUBSET" \
      --log_samples
  done
done