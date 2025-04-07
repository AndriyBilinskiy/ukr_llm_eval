# Use a lightweight base image with Python
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN  pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

RUN pip install --upgrade pip \
    && pip install \
    transformers \
    accelerate \
    lm-eval \
    huggingface_hub \
    sentencepiece \
    protobuf \
    grpcio \
    vllm

WORKDIR /workspace
VOLUME ["/workspace/output"]
COPY config.yaml /workspace/config.yaml
COPY run_eval.sh /workspace/run_eval.sh
COPY subset_constructive_dilemma.yaml /workspace/subset_constructive_dilemma.yaml
COPY subset_disjunctive_syllogism.yaml /workspace/subset_disjunctive_syllogism.yaml
COPY subset_material_implication.yaml /workspace/subset_material_implication.yaml
COPY subset_modus_ponens.yaml /workspace/subset_modus_ponens.yaml
COPY subset_modus_tollens.yaml /workspace/subset_modus_tollens.yaml


ENTRYPOINT ["bash", "/workspace/run_eval.sh"]
