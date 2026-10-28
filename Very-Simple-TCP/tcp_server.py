import socket as sck


# The socket is an object which represents an endpoint of a communications channel
__SOCKET__ = sck.socket(sck.AF_INET,sck.SOCK_STREAM)

# SOCK_STREAM - Transport protocol used for communication  [TCP] 
# AF_INET - IPv4 Address

_HOST = "127.0.0.1" # Loopback Interface; localhost  
PORT = 8000
__SOCKET__.bind((_HOST, PORT))

# Program opens port on localhost
__SOCKET__.listen(10)

while True:
    #  Awaits client connection
    d, a = __SOCKET__.accept()
    d.send(b"Live. ")
    
    print('/> ', a)
    d.close()
