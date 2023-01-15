# Чат сервер - підрахунок слів
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
k=len(data.split())
conn.send(pickle.dumps(f"Number of words: {k}"))
conn.close()