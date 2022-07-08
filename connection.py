#pip install sockets

import socket

#Bağlantımızı Socket Modulu ile Oluşturuyoruz
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bağlantı için IP ve PORT'umuzu yazıyoruz
connection.connect(("IP",PORT))

#Bağlantıyı gönderiyoruz
connection.send()

#ve Bağlantıyı Kapatıyoruz
connection.close()
