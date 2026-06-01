
# MiniProject - SSH-BruteForce Project

Overview

This mini project demonstrates the fundamentals of automating SSH authentication attempts using Python 3. The script leverages the pwntools framework and Paramiko (included within pwntools) to establish SSH connections and test credentials against a target SSH service.

The project is intended for educational purposes, cybersecurity training environments, and authorized security assessments where permission has been explicitly granted.


## Requirements

1. To run the python3 script, pwntools is required to be imported and can be installed with the command

```bash
  sudo apt install python3-pwntools
```

## Learning Objectives

Through this mini-project the hands-on experience gained are mainly for:

Basic offensive security concept of how SSH ports can be bruteforced with Python3 scripting.
## What you will learn

The main takeaway from the mini-project was:

1. How to setup SSH in your localhost machine
2. Python3 Scripting for basic SSH bruteforcing using paramiko from pwntools - ssh-brutefore.py
3. Basic Python3 Scripting to check if your system has the SSH port 22 open and is accessbile. - ssh-localhosttest.py
4. Limitations that come with the ssh-bruteforcing when proper security configuration is applied.






## Setup to run the ssh-brutforce.py successfully in your localhost
The main takeaway from the mini-project was:

1.  Setup of Kali Linux system to check if the tool sshd is installed or not.

```bash
which sshd
```

If it's not installed:
```bash
sudo apt update
sudo apt install openssh-server
```

2. SSH service

--Start the ssh service
```bash
sudo systemctl start ssh
```
--Enable it at boot:
```bash
sudo systemctl enable ssh
```
--Verify the status:
```bash
sudo systemctl status ssh
```
You should see something similar to:
```bash
Active: active(running)
```

3. Verify localhost connectivity

---First, try connecting manually:
```bash
ssh username@127.0.0.1
```
If prompted for a password and you can log in successfully, the SSH service is working.

4. Verify the SSH daemon configuration
```bash
sudo vi /etc/ssh/sshd_config
```
Relevant settings:
```bash
Port 22
PasswordAuthentication yes
PermitRootLogin no
```
After changes:
```bash
sudo systemctl restart ssh
```


## Useful Diagnostics

1. Check whether SSH is reachable
```bash
nc -vz 127.0.0.1 22
```

Expected:
```bash
Connection to 127.0.0.1 22 port [tcp/ssh] succeeded!
```

2. View SSH logs while testing
```bash
sudo journalctl -fu ssh
```
or
```bash
sudo tail -f /var/log/auth.log
```
## After project takeaway:

1. Default Kali SSH configuration will block authentication attempts after 10 attempts (MaxStartups 10:30:10). 

2. If you want to test 100 connections + the valid password using the above wordlist, you will need to edit your sshd_config (for example, by setting MaxStartups 101) and restarting the service. 

3. Alternatively to test, use a wordlist with less than 10 invalid passwords.

4. Running diagnostics while running the the python script is much more helpful. 
```bash
sshd[475532]: srclimit_penalise: 127.0.0.1/32: activating ipv4 penalty of 19.944 seconds for penalty: failed authentication
```
The above lets you know how the security works when you make multiple failed SSH attempts.

## Common cause of failure 

1. SSH server not running.
2. Password authentication disabled.
3. Wrong username.
4. Firewall blocking the port. ( for localhost you can run ```bash sudo ufw allow 22/tcp ``` )
5. Script attempting too many connections too quickly and hitting server-side limits.
6. Using the wrong host (localhost vs 127.0.0.1 is usually fine, but verify what your code uses).
## Screenshots

Successful([https://github.com/WNobsi/MiniProject---SSH-BruteForce-script-using-Python3/blob/3d1b2c35407022ee30a812d60c9b8cb70b7125e7/img/SSH%20Diagnostics.png])

Diagonostic([https://github.com/WNobsi/MiniProject---SSH-BruteForce-script-using-Python3/blob/3d1b2c35407022ee30a812d60c9b8cb70b7125e7/img/SSH%20Diagnostics.png])

