#!/usr/bin/env python3

# ----------------------------------------------------------------------------
# Author: Alexander Lubrano
# Course: CS 372 - 401
# Assignment: Client/Server Chat: chat_client.py
# Date: 12/03/2022
#
# Sources Used:
#     - 
#
# ----------------------------------------------------------------------------

import socket

HOST = socket.gethostbyname("localhost")
PORT = 17777
QUIT_MSG = "/q"

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to localhost and port xxxx


# While connected:

    # Prompt user for a message to send

    # If message is "/q", client quits

    # Else, client sends message

    # Call recv to receive any data

    # Print data

# Close sockets
s.close()
