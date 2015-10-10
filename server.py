
#
#  br_pychat_server.py
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

import threading
import socketserver

CONNECTION_PORT = 9311

connections = {}

class TCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        try:
            cur_thread = threading.current_thread()
            print("'{ip}' requested connection.".format(ip = self.client_address[0]))
            print("Connection request granted.")
            if threading.activeCount() > 3:
                print("Number of current client connections: {n}".format(n = threading.activeCount() - 3))
            if self.client_address[0] not in connections.keys():
                connections[self.client_address[0]] = self.request
            while 1:
                received_from_client = self.request.recv(10000)
                for connection in connections:
                    connections[connection].sendall(bytes("'{ip}': {data}".format(ip = self.client_address[0], data = received_from_client), "utf-8"))
        except ConnectionResetError:
            pass

class TCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    HOST  = ""
    print("Chat Server Project initiated.")
    print("Waiting for incoming connection requests...")
    server = TCPServer((HOST, CONNECTION_PORT), TCPHandler)
    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

