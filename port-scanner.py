#!/usr/bin/env python

import socket
import sys
import time
from multiprocessing import Pool

def scan(args):
  target_ip, port = args

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(1)

  try:
    sock.connect((target_ip, port))
    sock.close()

    return port, True

  except (socket.timeout, socket.error):
    return port, False

def main():
  try:
    TARGET_IP = input("Enter the target IP:")
    START_PORT = input("Starting port: ")
    END_PORT = input("End port: ")
    NUM_PROCS = 1000

    print("Scanning the target IP: {} with {} processes".format(TARGET_IP, NUM_PROCS))
    print("="*80)
    start = time.time()

    pool = Pool(processes=NUM_PROCS)


    for port,status in pool.imap_unordered(scan, [(TARGET_IP, port) for port in range(int(START_PORT), int(END_PORT))]):
      if status:
        print("Port {} is open".format(port))

    end = time.time()
    print("="*80)
    print("Scan completed in {} seconds.".format(end-start))
    print("="*80)

  except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()

if __name__ == "__main__":
  main()
