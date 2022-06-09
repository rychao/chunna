# script to run headless Selenium on Chrome to retrieve pricing information

#Python Imports
sleep 8
sudo apt -y update
sudo apt -y install python3-pip
pip3 install selenium

#Install Chromedriver
curl -O https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
sudo apt -y install unzip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/.

# 2022 chromium Install
curl -O https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_linux64.zip
sudo apt-get install chromium -y
