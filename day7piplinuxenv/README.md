fajriillahi@Fajris-MacBook-Pro ~ % which python3.8
/opt/homebrew/bin/python3.8

pip install virtualenv
virtualenv -p /opt/homebrew/bin/python3.8 env3.8
virtualenv -p /opt/homebrew/bin/python3.9 env3.9
virtualenv -p /opt/homebrew/bin/python3.10 env3.10

# For Linux
virtualenv -p /usr/bin/python3.8 env3.8
virtualenv -p /usr/bin/python3.9 env3.9
virtualenv -p /usr/bin/python3.10 env3.10

source env3.8/bin/activate
source env3.9/bin/activate
source env3.10/bin/activate

deactivate