#!/usr/bin/env python3

# ----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 372 - 401
# Assignment: Client/Server Chat: chat_server.py
# Date: 12/03/2022
#
# Sources Used:
#     -
#
# ----------------------------------------------------------------------------

import socket

HOSTNAME = "localhost"
HOST = socket.gethostbyname(HOSTNAME)
PORT = 17777
QUIT_MSG = "/q"

# Create socket and set options
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to localhost and port xxxx
server.bind((HOST, PORT))

# Listen for a connection
server.listen(1)
print(f"Server listening on: {HOSTNAME} on port: {PORT}")

conn, addr = server.accept()
print(f"Connected by {addr}")
print("Waiting for message...")

# While connected
    
    # Server calls recv to receive data

    # Server prints data, then prompts for a reply

    # If reply is "/q", server quits

    # Else, server sends the reply

# Close sockets
socket.close()
