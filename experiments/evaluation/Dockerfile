# Use a lightweight base image with Python
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    HF_HOME=/root/.cache/huggingface \
    TRANSFORMERS_CACHE=/root/.cache/huggingface/transformers

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install \
    transformers \
    accelerate \
    lm-eval \
    huggingface_hub

RUN  pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

WORKDIR /workspace
VOLUME ["/workspace/output"]
COPY config.yaml /workspace/config.yaml
COPY run_eval.sh /workspace/run_eval.sh

ENTRYPOINT ["bash", "/workspace/run_eval.sh"]