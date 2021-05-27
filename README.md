# Python TCP Chatroom

Python chatroom implementation that connects users to a server over a specified port and allows them to send and receive messages.

### Contents:
- `server.py`: **Server** class models a server that listens on a specified port for incoming messages from clients.

- `client.py`: **User** class models a user connecting to a chatroom's server on a specified port.

### Logic:
***Server***
On instantiation of the Server class a server socket is created and binded to the provided *IP Address* and *Port Number*. The Server class contains 3 methods:
- `handle(client)`: continuously receives data from the clients and broadcasts that to every client that is connected to the server. If a client disconnects the client will be removed from the *clients* list
- `broadcast(message)`: sends the message to each client connected to the server. All the clients that connect are stored in a *clients* list.
- `receive()`: continuously listens for clients that connect to the server. If a client connects the server will send an initial message to the client requesting a nickname to be used chatroom. After the client replies with the nickname the server will add the client object to the client list and the nickname to a *nickname* list

***User***
On instantiation of the User class a client socket is created and the nickname provided as an argument is stored in an instance variable. The User class contains 4 methods:
- `connect(host, port)`: connects to the server on the host and port provided
- `receive()`: continuously listens for incoming data. If the message is the nickname request from the server the client will respond with a chosen nickname to be used in the chatroom. If not the messages received will be printed
- `write()`: sends messages to the server
- `join()`: creates, binds and starts two separate threads for receiving and writing

***constants***
Store variables used as constants:
- `MAGIC`: the message sent by the server to the client requesting a nickname
- `ENCODING`: the encoding method used to encode and decode messages
- `HOST_NAME`: server host name
- `PORT`: server port
