#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  br_pychat_display.py
#  
#  Copyright 2015 Ericson Willians (Rederick Deathwill) <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket

CONNECTION_PORT = 9311

if __name__ == '__main__':
	print("Chat Display Project initiated.")
	HOST = input("Please provide an IP Address: ")
	done = False
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((HOST, CONNECTION_PORT))
	while 1:
		received = str(sock.recv(10000), "utf-8")
		print(received)
