# Script for compressing all files in the folder with TinyJPG
# All libs in requirements.txt

import os
import tinify
import shutil

api_key = input('Please, enter your API Key from TinyJPG: ')
ext = ['jpg', 'jpeg','png']

def create_folder():
	try:
		os.makedirs('Output')
		print('Output folder created!')
		return True
	except FileExistsError:
		print('Output folder already!')
		return True
	except:
		return False

def compress_load(pack):
	for r in ext:
		if pack.endswith(r):
			#fullpath = pack[0] + "\\" + f
			#shutil.copy(fullpath, 'Output')
			#print(fullpath)
			source = tinify.from_file(pack)
			source.to_file("Output/"+pack)
			print(pack)

def compress():
	counter=0
	local = os.getcwd()
	print("Current folder > "+local)
	print("\n+--------------------------------+")
	print("| FILES                          |")
	print("+--------------------------------+")

	for pack in os.listdir(local):
		compress_load(pack)
		counter+=1

	print("+--------------------------------+")
	print('| FILES: '+str(counter)+'  |')
	print("+--------------------------------+\n")			
				
def main():
	api = tinify.key = api_key
	proxy = input("Use proxy? (Y/N) ")

	if proxy == 'Y' or proxy == 'y' or proxy == 'Yes' or proxy == 'yes':
		proxy = input("Need a authentication?")
		if proxy == 'Y' or proxy == 'y' or proxy == 'Yes' or proxy == 'yes':
			ip = input("Your IP proxy: ")
			port = input("Port: ")
			user = input("Username: ")
			pwd = input("Password: ")
			
			try:
				proxy_load = tinify.proxy = "https://"+user+":"+pwd+"@"+ip+":"+port
				print("\nConnected!\n")
			except:
				proxy_load = tinify.proxy = "http://"+user+":"+pwd+"@"+ip+":"+port
				print("\nConnected!\n")
		else:
			ip = input("Your IP proxy: ")
			port = input("Port: ")
			
			try:
				proxy_load = tinify.proxy = "https://"+ip+":"+port
				print("\nConnected!\n")
			except:
				proxy_load = tinify.proxy = "http://"+ip+":"+port
				print("\nConnected!\n")



	if create_folder() == False:
		print('Failed to create an output folder...')
		exit()
	else:
		compress()

	
main()