from geer import *
import os
import time

os.system("""
  echo getting sudo access
  sudo whoami
  cd ~
  echo updating packages
  sudo apt update
  """)

apt_install.apt_install()
docker_sintall.docker_install()
git_install.git_repos()

rbt_msg="We will now reboot your system. \n rebboting in..."
for i in range(len(rbt_msg)):
  print(rbt_msg)
  time.sleep(0.2)
  
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
