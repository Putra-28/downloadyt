import os, sys, time

#warna
HEADER = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

def logo():
  os.system('clear')
  print(RED+"-"*50)
  print(RED+"|-----------",GREEN+ "Download Vidio Dan Musik",RED+"-----------|")
  print(RED+"|-------------",GREEN+"Creator: mr.2805eror",RED+"-------------|")
  print(RED+"-"*50)
logo()
def menu():
  print(GREEN+"SILAHKAN DOWNLOAD VIDIO ATAU MUSIK")
  print(CYAN+"1. Musik")
  print("2. Vidio")
  print("00. KELUAR")
  menu = input(HEADER+"|=> ")
  while (True):
    if menu == '1':
      time.sleep(2)
      os.system('clear')
      print("_____DOWNLOAD MUSIK_____".center(55))
      time.sleep(2)
      folder = str(input(GREEN+"NAMA FOLDER: "))
      link = str(input(GREEN+"Link Youtube: "))
      y = os.system('youtube-dl -x --audio-format mp3 -o "/sdcard/"'+folder +'"/%(title)s.%(ext)s" ' +link)
      if y == 0:
        os.system('clear')
        print(RED+"+> Berhasil <+")
        time.sleep(1)
        print("+> Tersimpan Difolder "+folder +"<+".center(55))
        time.sleep(2)
        break
      else:
        os.system('clear')
        print(RED+"+> Gagal <+".center(55))
        time.sleep(2)
        
    elif menu == '2':
      time.sleep(2)
      os.system('clear')
      print(RED+"_____DOWNLOAD VIDIO_____".center(55))
      time.sleep(2)
      namafolder = str(input(GREEN+"NAMA FOLDER: "))
      linkyt = str(input(GREEN+"Link Youtube: "))
      v = os.system('youtube-dl -o "/sdcard/"'+namafolder +'"/%(title)s.%(ext)s"' +linkyt)
      if v == 0:
        os.system('clear')
        print(RED+"+> Berhasil <+".center(55))
        time.sleep(1)
        print("+> Tersimpan Difolder "+namafolder +"<+".center(55))
        time.sleep(2)
        break
      else:
        os.system('clear')
        print(RED+"+> Gagal <+".center(55))
        time.sleep(2)
        
    elif menu == '00':
      time.sleep(2)
      print("Terima Kasih Telah Menggunakan Tools Saya")
      print("By: Mr.2805eror")
      time.sleep(2)
      os.system('clear')
      break
    else :
      print("Coba lagi")
      break
menu()