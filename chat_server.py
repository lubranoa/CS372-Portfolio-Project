#!/usr/bin/env python3

# ----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 372 - 401
# Assignment: Client/Server Chat: chat_server.py
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

# Create socket and set options
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to localhost and port xxxx
server.bind((HOST, PORT))

# Listen for a connection
server.listen(1)
print(f"Server listening on: {HOST} on port: {PORT}")

conn, addr = server.accept()

# While connected
with conn:

    num_sent_msgs = 0
    print(f"Connected by {addr}")
    print("Waiting for message...")
    
    while True:
    # Server calls recv to receive data
        rcv_msg = conn.recv(1024)
        if rcv_msg.decode() == QUIT_MSG: break

        # Server prints data, then prompts for a reply
        print(f"{rcv_msg.decode()}")
        if num_sent_msgs == 0: print("Type /q to quit\nEnter message to send...")
        send_msg = input(">>>")

        # If reply is "/q", server quits
        if send_msg == QUIT_MSG: 
            conn.send(QUIT_MSG.encode())
            break

        # Else, server sends the reply
        conn.send(send_msg.encode())
        num_sent_msgs += 1

# Close sockets
server.close()
