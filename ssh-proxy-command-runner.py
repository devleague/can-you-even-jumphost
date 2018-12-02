#!/usr/bin/env python

import sys
import socket
import paramiko

def create_proxy_connection(jump_host, jump_port, jump_user, jump_password, remote_host, remote_port, remote_user):
  try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=jump_host, username=jump_user, port=jump_port, password=jump_password)
    print("Successfully connected to {} through {}".format(remote_host, jump_host))

    while True:
      ssh_session = client.get_transport().open_session()
      if ssh_session.active:
        command = input("Command to execute on remote host: ")

        if str(command).strip().lower() == "exit":
          client.close()
          return

        full_command = "ssh -t {}@{} {}".format(remote_user, remote_host, command)
        print("Full command to run on remote: {}".format(full_command))

        ssh_session.exec_command(full_command)
        output = ssh_session.recv(1024)
        print(output.decode())

  except (paramiko.AuthenticationException) as e: 
    print("Login to jump host {} failed. \nError: {}".format(jump_host, e))
    return

  except (paramiko.BadHostKeyException) as e:
    print("Error with bad host key connecting to host: {}\nError: {} \n".format(jump_host, e))
    return

  except (paramiko.SSHException) as e:
    print("Error connecting to the specified host: {}\nError: {} \n".format(jump_host, e))
    return


def main():
  try: 
    PROXY_HOST = input("IP Address of the jump host: ")
    PROXY_PORT = input("Port of the jump host: ")
    PROXY_USER = input("Username of jump host: ")
    PROXY_PASSWORD = input("Password of jump host: ")
    TARGET_HOST = input("IP Address of the remote host: ")
    TARGET_PORT = input("Port of the remote host: ")
    TARGET_USER = input("Username of remote host: ")

    create_proxy_connection(
      PROXY_HOST, 
      PROXY_PORT, 
      PROXY_USER, 
      PROXY_PASSWORD, 
      TARGET_HOST,
      TARGET_PORT, 
      TARGET_USER
    )

  except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()

if __name__ == "__main__":
    main()