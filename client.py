
#  br_pychat_client.py
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
import tkinter as tk
import threading

CONNECTION_PORT = 9311

class App(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.start()
	
	def callback(self):
		self.root.quit()
		
	def run(self):
		self.root = tk.Tk()
		self.root.protocol("WM_DELETE_WINDOW", self.callback)
		self.root.title("Social Pie Client")
		self.root.grid()
		self.root.grid_columnconfigure(1, weight=1)
		self.create_widgets()
		self.console.insert(tk.END, "Social Pie initiated.\n")
		self.connected = False
		self.root.mainloop()
	
	def create_widgets(self):
		self.host_label = tk.Label(self.root, text="Host: ")
		self.host_label.grid(column=0, row=0, padx=270, pady=10, columnspan=2, sticky="w")
		self.host_entry = tk.Entry(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2, takefocus=1)
		self.host_entry.grid(column=0, row=0, pady=10, columnspan=2)
		self.host_entry.bind("<Return>", self.connect)
		self.console = tk.Text(self.root, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2)
		self.console.grid(column=0, row=1, padx=20, columnspan=2)
		self.msg_label = tk.Label(self.root, text="Message: ")
		self.msg_label.grid(column=0, row=2, padx=25)
		self.msg_area = tk.Text(self.root, height=6, width=58, bg="#000", fg="#0F0", highlightcolor="#F00", highlightthickness=2)
		self.msg_area.grid(column=0, row=3, ipadx=10, padx=25, pady=10, columnspan=2, sticky="w")
		self.msg_area.bind("<Return>", self.send)
		self.connect_button = tk.Button(self.root, text="Connect", command=self.connect)
		self.connect_button.grid(column=0, row=3, ipadx=10, padx=85, pady=10, columnspan=2, sticky="es")
		self.quit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
		self.quit_button.grid(column=1, row=3, ipadx=10, padx=30, pady=10, sticky="es")
		self.host_entry.focus_set()
	
	def send(self, x=None):
		self.sock.sendall(bytes(self.msg_area.get("1.0", tk.END), "utf-8"))
		self.msg_area.delete("1.0", tk.END)
		
	def connect(self, x=None):
		if not self.connected:
			self.host = self.host_entry.get()
			self.console.insert(tk.END, "Connecting to {host}...\n".format(host = self.host))
			done = False
			try:
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.connect((self.host, CONNECTION_PORT))
				self.console.insert(tk.END, "Connection established.\n")
				self.connect_button.config(text="Disconnect")
				self.connected = True
				
			except Exception as e:
				self.console.insert(tk.END, "Error trying to connect to {host}: {msg}\n".format(host = self.host, msg = str(e)))
			
		else:
		#	self.sock.close()
		#	self.rsock.close()
			self.console.insert(tk.END, "Connection with {host} destroyed.\n".format(host = self.host))
			self.connect_button.config(text="Connect")
			self.connected = False

if __name__ == '__main__':
	app = App()
	while 1:
		try:
			received = app.sock.recv(10000).decode("utf-8")
			app.console.insert(tk.END, "{msg}.".format(msg = received))
		except:
			pass
		
