import socket
import json

class Conection:
	
	def __init__(self, dato_entrada):
		self.dato_entrada = dato_entrada
		
	def realizar_busqueda(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 
		# Conecta el socket en el puerto cuando el servidor esté escuchando
		self.server_address = ('localhost', 10000)
		self.sock.connect(self.server_address)

		try:
			 
			# Enviando datos
			self.message = self.dato_entrada
			self.sock.send(self.message.encode('utf-8'))
		 
			# Buscando respuesta
			self.amount_received = 0
			self.amount_expected = len(self.message)
			while self.amount_received < self.amount_expected:
				self.data = self.sock.recv(10000)
				self.amount_received += len(self.data)
				self.resultado_pre = self.data.decode('utf-8')
				self.resultado = json.loads(self.resultado_pre)
				
			"""while True:
				mensajes = [1,2,3]
				mensaje = json.dumps(mensajes)
				print('enviando "%s"' % mensaje)
				sock.send(mensaje.encode('utf-8'))
				if mensaje == "quit":
					break
				else:
					amount_received = 0
					amount_expected = len(mensaje)
			 
					while amount_received < amount_expected:
						data = sock.recv(len(mensaje))
						datos = str(data)
						amount_received += len(data)
						print('recibiendo "%s"' % data)
						print(data)
						print(datos)"""
						
		 
		finally:
			self.sock.close()
			return self.resultado
