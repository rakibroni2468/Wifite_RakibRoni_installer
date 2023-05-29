import os
print('''\033[1;36;40mWifite_RakibRoni Installer By ItsRakibRoni
Your Device Must Be Rooted
If Any Question,
Contact Me On Facebook
Facebook_User: https://www.facebook.com/h4cker11 \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/rakibroni2468/Wifite_RakibRoni")

os.system("cd ..;chmod +x Wifite_RakibRoni/wifihack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python Wifite_RakibRoni/wifihack.py -i wlan0 -K")