#!/bin/bash

# Set constants
CONTAINER_NAME="lm_eval_container"
LOCAL_OUTPUT_DIR="./output"
CONTAINER_OUTPUT_DIR="/workspace/container_output"

echo "Building the Docker image and starting container..."
docker compose up --build


CONTAINER_ID=$(docker ps -a -q --filter "name=$CONTAINER_NAME")

if [ -z "$CONTAINER_ID" ]; then
    echo "Error: Container $CONTAINER_NAME not found!"
    exit 1
fi

mkdir -p $LOCAL_OUTPUT_DIR

echo "Copying output from container..."
docker cp $CONTAINER_ID:$CONTAINER_OUTPUT_DIR $LOCAL_OUTPUT_DIR

# Step 7: Clean up the container
echo "Cleaning up..."
docker rm $CONTAINER_ID

echo "Done! Output saved in $LOCAL_OUTPUT_DIR"