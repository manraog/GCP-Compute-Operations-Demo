#! /bin/bash

#Instalación de agentes de logging y monitoring
curl -sSO https://dl.google.com/cloudagents/add-monitoring-agent-repo.sh
sudo bash add-monitoring-agent-repo.sh
curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh
sudo bash add-logging-agent-repo.sh
sudo apt-get update
sudo apt upgrade
sudo apt-get install stackdriver-agent
sudo apt-get install google-fluentd
sudo apt-get install google-fluentd-catch-all-config-structured
sudo service google-fluentd start

#Instalación de aplicación
apt -y install git python3 python3-pip
git clone https://github.com/manraog/GCP-Compute-Operations-Demo.git
cd GCP-Compute-Operations-Demo
pip3 install -r requeriments.txt
#python3 main.py