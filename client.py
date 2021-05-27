import socket
import threading
import constants


class User:
    """
        User class that models a chat room user.
        @nickname: nickname chosen by user to be sent to the server
                    and used as an identifier in the chat room
    """
    def __init__(self, nickname):
        self.__nickname = nickname
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.client.connect((host, port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode(constants.ENCODING)
                if message == constants.MAGIC:
                    self.client.send(self.__nickname.encode(constants.ENCODING))
                else:
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f'{self.__nickname} : {input("")}'
            self.client.send(message.encode(constants.ENCODING))

    def join(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()


nick = input("Choose a nickname: ")
user = User(nick)
user.connect(constants.HOST_NAME, constants.PORT_NUM)
user.join()
