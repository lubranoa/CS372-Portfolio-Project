#!/usr/bin/env python3

# ----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 372 - 401
# Assignment: Client/Server Chat: chat_client.py
# Date: 12/03/2022
#
# Sources Used:
#     - Python 3 Docs:
#           https://docs.python.org/3/library/socket.html
#           https://docs.python.org/3/howto/sockets.html
# 
#     - Socket Programming in Python (Guide) by Nathan Jennings of Real Python:
#           https://realpython.com/python-sockets/#echo-server
#
# ----------------------------------------------------------------------------

import socket

HOST = "localhost"
PORT = 9999
QUIT_MSG = "/q"

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to localhost and port xxxx
s.connect((HOST, PORT))
print(f"Connected to: {HOST} on port: {PORT}")

num_sent_msgs = 0
# While connected:
while True:

    # Prompt user for a message to send
    if num_sent_msgs == 0: print("Type /q to quit\nEnter message to send...")
    send_msg = input(">>>")

    # If message is "/q", client quits
    if send_msg == QUIT_MSG: 
        s.send(QUIT_MSG.encode())
        break

    # Else, client sends message
    s.send(send_msg.encode())
    num_sent_msgs += 1

    # Call recv to receive any data
    rcv_msg = s.recv(1024)
    if rcv_msg.decode() == QUIT_MSG: break

    # Print data
    print(rcv_msg.decode())

# Close sockets
s.close()
