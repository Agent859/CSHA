import os

def apt_install():
  print("Apt Installation Starting")
  os.system("""
  echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
  echo "deb http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
  sudo apt install steghide -y
  sudo apt install beef -y
  
  """)
