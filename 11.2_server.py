# Чат сервер-бот зі стандартими повідомленнями
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
if data =="Hello":
    conn.send(pickle.dumps("Hello!"))
    conn.close()
elif data =="Hi":
    conn.send(pickle.dumps("Hi!"))
    conn.close()
elif data =="How are you?":
    conn.send(pickle.dumps("Hello! OK, thank you. like you?"))
    conn.close()
else:
    conn.send(pickle.dumps("Repeat I don't understand :("))
    conn.close()

