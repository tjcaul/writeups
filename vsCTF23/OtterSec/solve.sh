# Warning: the environment takes 1.6 GB
# Still lighter than running ../dist/Dockerfile though

# Setup environment
python3 -m venv venv &&
cp -r home venv &&
cd venv/home &&
source ../bin/activate &&
pip3 install -r requirements.txt

# Do the h4xx0rz1ng
python3 train.py
base64 -i new_model.h5 | nc 172.86.96.174 10105
