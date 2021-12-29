import subprocess


def login():
    #This will login to ACR(azure container registry)
    subprocess.call('az acr login --name teeautocr001', shell=True)

login()


def pushApp():
    subprocess.call('docker push teeautocr001.azurecr.io/pythonbapp:v1', shell=True)

pushApp()