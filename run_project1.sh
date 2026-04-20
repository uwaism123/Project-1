#!/bin/bash

echo "🔧 Building Docker image..."
docker build -t project_1 .

echo "🚀 Running FileFlow..."
MSYS_NO_PATHCONV=1 docker run -v "$(pwd):/app" project_1