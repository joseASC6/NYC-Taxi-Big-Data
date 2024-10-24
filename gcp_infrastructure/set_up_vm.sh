# Install pip3
sudo apt -y install python3-pip python3.11-venv

# Create a Python Virtual Environment
python3 -m venv pythondev

# Activate the Python Virtual Environment
cd pythondev; source bin/activate

# Install the required Python packages
pip3 install --upgrade pip
pip3 install jupyter pandas numpy requests 
pip3 install google-cloud-storage

# Set up credentials for Google user account
gcloud auth application-default login

# Create extracting taxi data script
nano extracting_taxi_data.py

# Excute python script
python3 extracting_taxi_data.py

# Create extracting weather data script
nano extracting_weather_data.py

# Excute python script
python3 extracting_weather_data.py

