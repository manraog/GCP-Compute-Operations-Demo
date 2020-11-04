#! /bin/bash
apt update
apt -y install git python3 python3-pip
git clone https://github.com/manraog/GCP-Compute-Operations-Demo.git
cd GCP-Compute-Operations-Demo
pip3 install requeriments.txt
python3 main.py