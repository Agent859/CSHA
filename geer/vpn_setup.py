import os
print("Setting up ProtonVPN, a free VPN service. Create an account at account.protonvpn.com")

def vpn_setup():
  os.system("""
    curl -O https://repo.protonvpn.com/debian/dists/stable/main/binary-all/protonvpn-stable-release_1.0.3_all.deb
    sudo apt-get install ./protonvpn-stable-release_1.0.3_all.deb
    sudo apt-get update
    sudo apt-get install protonvpn
    """)
