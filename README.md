# Yolov10m Flask
## Installation
Run the AutoTest.sh for auto-setup and server initailization. Might need extra 5-10 seconds for server to be initialized (you may check server logs). 
## Execution
Activate venv and run the client.py script.
```
# activate venv
source .venv/bin/activate

# run script
python client.py
 ```

## Problem shooting
If the auto-setup bash script didn't work, the following setups should be procceded manually.
### UV
An extremely fast Python package and project manager, written in Rust.
[github] <https://github.com/astral-sh/uv>  

```
# Installation
curl -LsSf https://astral.sh/uv/install.sh | sh  
```
```
# Download python3.10 and create venv
uv install --python=3.10
uv venv --python=3.10
```
```
# Activate venv and install dependencies
source .venv/bin/activate
uv pip install -r requirements.txt
 ```

### Run server
```
nohup python server.py > server.log 2>&1 &
```

### Run client
Activate venv and run the client.py script.
```
# activate venv
source .venv/bin/activate

# run script
python client.py
 ```

