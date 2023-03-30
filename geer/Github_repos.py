import os

def git_repos():
  print("Installing Github Repositories)
  os.system("""
  mkdir github
  cd github
  git clone https://github.com/t3l3machus/hoaxshell
  git clone https://github.com/JohnHammond/msdt-follina
  git clone https://github.com/paranoidninja/Brute-Ratel-C4-Community-Kit
  git clone https://github.com/H1R0GH057/Anonymous
  git clone https://github.com/debajyotidasgupta/blackeye.git
  """)
