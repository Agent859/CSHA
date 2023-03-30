import os

def docker_install():
  print("installing docker and portainer")
  os.system("""
  sudo apt install docker.io -y
  sudo systemctl enable docker --now
  sudo usermod -aG docker $USER
  sudo docker volume create portainer_stuff
  docker run -d -p 9443:9443 -p 8000:8000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_stuff:/data portainer/portainer-ce:latestcls
  """)
