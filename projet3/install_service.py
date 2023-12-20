# install_service.py

import subprocess

def install_apache():
    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo", "apt-get", "install", "-y", "apache2"])

def install_ssh():
    subprocess.run(["sudo", "apt-get", "install", "-y", "openssh-server"])

if __name__ == "__main__":
    install_apache()
    install_ssh()
