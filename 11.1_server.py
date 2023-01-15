# Чат сервер повідомлення з консолі
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')

conn, addr = sock.accept()
data = conn.recv(1024)
data = pickle.loads(data)
print(data)

msg1 = input("Enter a message for the klient: ")
conn.send(pickle.dumps(msg1))
conn.close()



