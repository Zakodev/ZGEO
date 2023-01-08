try:
	import sys
	import time
	import os
	from colorama import Back, Fore, Style, deinit, init
	from ip2geotools.databases.noncommercial import DbIpCity
except:
	print("Module manquant !")
	try:
		os.system("pip install -r requirements.txt")
	except:
		print("Impossible d'installer les modules")
		quit()


def animation(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(2./90)


def anim(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.5/90)

try:
	os.system("/usr/bin/clear")
except:
	try:
		os.system("cls")
	except:
		pass
animation(Fore.BLUE + Style.NORMAL + """     Géoip développé par zako#7777""")

anim(Fore.BLUE + Style.NORMAL + """

/$$$$$$$$  /$$$$$$  /$$$$$$$$  /$$$$$$ 
|_____ $$  /$$__  $$| $$_____/ /$$__  $$
     /$$/ | $$  \__/| $$      | $$  \ $$
    /$$/  | $$ /$$$$| $$$$$   | $$  | $$
   /$$/   | $$|_  $$| $$__/   | $$  | $$
  /$$/    | $$  \ $$| $$      | $$  | $$
 /$$$$$$$$|  $$$$$$/| $$$$$$$$|  $$$$$$/
|________/ \______/ |________/ \______/ """)
animation("\n\nQuelle est l'adresse ip a géolocalisé ?: ")
ip = input()
reponse = DbIpCity.get(ip, api_key='free')

print(Fore.RED + Style.NORMAL + "\nResultat:")
ipp = animation(Fore.RED + Style.NORMAL + "Ip: " + reponse.ip_address)
pays = animation(Fore.RED + Style.NORMAL + "Pays: " + reponse.country)
region = animation(Fore.RED + Style.NORMAL + "Région: " + reponse.region)
ville = animation(Fore.RED + Style.NORMAL + "Ville: " + reponse.city)
latitude = animation(Fore.RED + Style.NORMAL + "Latitude: " + str(reponse.latitude))
longitude = animation(Fore.RED + Style.NORMAL + "Longitude: " + str(reponse.longitude))

input()