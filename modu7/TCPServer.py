from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server TCP siap...")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()
    modifiedSentence = sentence.upper()
    connectionSocket.send(modifiedSentence.encode())
    connectionSocket.close()