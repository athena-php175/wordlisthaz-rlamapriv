import os
print("""


   _____   __  .__                          
  /  _  \_/  |_|  |__   ____   ____ _____   
 /  /_\  \   __\  |  \_/ __ \ /    \\__  \  
/    |    \  | |   Y  \  ___/|   |  \/ __ \_
\____|__  /__| |___|  /\___  >___|  (____  /
        \/          \/     \/     \/     \/ 

""")
os.system("cls")
isim = input("Hedefin ismi : ")
soyisim = input("Hedefin soyismi : ")
hayvan = input("Evcil hayvanının adı :")
th = open("cıktı.txt","w")
th.write("\n"+isim+soyisim)
th.write("\n"+hayvan+soyisim)
th.write("\n"+soyisim+isim)
th.write("\n"+soyisim+hayvan)
th.write("\n"+hayvan+isim)
th.close()
