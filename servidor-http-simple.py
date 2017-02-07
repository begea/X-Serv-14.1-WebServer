#!/usr/bin/python

# Borja Egea Madrid

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 32122))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# La IP esta alojada en la posicion 1 de address.
# El Puerto esta alojado en la possicion 2 de address.

while True:
	print 'Waiting for connections'
	(recvSocket, address) = mySocket.accept()
	print 'HTTP request received:'
	print recvSocket.recv(1024)
	recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
			"<html><body><h1>Hola! Eres de esta IP: " + address[0] +
			" y de este Puerto: " + str(address[1]) + 
			"</h1></body></html>" +
			"\r\n", "utf-8")
	recvSocket.close()
