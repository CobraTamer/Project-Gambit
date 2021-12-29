import subprocess
from subprocess import check_output
import time

#1. Please make sure you install Docker desktop (tested on windows)
#2. imply create a new folder, add the Gambit.py and then looping traceroute Batch script(app that will be containerised) that will be containerised 
#3. simply Run Gambit.py from thw follder

def createACR():
    #THIS WILL CREATE ACR(azure Container registry)
    subprocess.call('az acr create --resource-group WERG --name teeautocr001 --sku Basic', shell=True)

createACR()

def createdocker():
    #Create docker file
    f= open("dockerfile", "w")
    f.write("""
    FROM mcr.microsoft.com/windows/nanoserver:1803-amd64
    COPY . /
    RUN 
    CMD [ "12.bat" ]""")
    f.close()

createdocker()

#Build the docker image based on the docker file
def buildDockerimage():
    subprocess.call('docker build -t autoapp .', shell=True)

buildDockerimage()

#Tag the docker Image
def tagImage():
    subprocess.call('docker tag autoapp teeautocr001.azurecr.io/pythonbapp:v1', shell=True)

tagImage()

time.sleep(30)

def login():
    #This will login to ACR(azure container registry)
    subprocess.call('az acr login --name teeautocr001', shell=True)

login()

#Push App to Azure Container registry 
def pushApp():
    subprocess.call('docker push teeautocr001.azurecr.io/pythonbapp:v1', shell=True)

pushApp()
