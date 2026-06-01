#to test first if the ssh port is accepting requests in the system

from pwn import *

try:
    conn = ssh(
        host="127.0.0.1",
        user="username",
        password="password",
        port=22
    )

    print("[+] Login Successful")
    conn.close()

except Exception as e:
    print(f"[-] Error: {e}")
