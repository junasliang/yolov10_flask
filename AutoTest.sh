#!/bin/bash

# 1. Install uv
if ! command -v uv &> /dev/null; then
    echo "[INFO] Installing uv..."
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# 2. python 3.10 venv
echo "[INFO] Creating Python 3.10 environment..."
uv install --python=3.10
uv venv --python=3.10

# 3. venv activation, install dependencies requirements.txt
echo "[INFO] Activating environment and installing requirements..."
source .venv/bin/activate
uv pip install -r requirements.txt

# 4. nohup server.py
echo "[INFO] Starting server.py in background..."
nohup python server.py > server.log 2>&1 &

echo "[SUCCESS] Server is running. Logs: server.log"