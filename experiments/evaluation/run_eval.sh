#!/bin/bash
DEVICE="cpu"

# Check if CUDA is available
if python -c "import torch; print(torch.cuda.is_available())" | grep "True"; then
    DEVICE="cuda"
fi

echo "Using device: $DEVICE"

# Define splits
IFS=',' read -r -a SPLIT_ARRAY <<< "$SPLITS"

for SPLIT in "${SPLIT_ARRAY[@]}"; do
  echo "Processing split: $SPLIT"
  sed -i "s|VALIDATION_SPLIT_PLACEHOLDER|$SPLIT|g" /workspace/config.yaml
  OUTPUT_DIR="/workspace/container_output/${SPLIT}"

  lm_eval \
    --model hf \
    --device "$DEVICE"\
    --model_args pretrained=bigscience/bloom-3b \
    --include_path ./ \
    --tasks config \
    --output "$OUTPUT_DIR" \
    --limit 1 \
    --log_samples
done