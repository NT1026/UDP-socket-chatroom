# Server side
import socket

# Configuration
ADDRESS = ('25.45.192.99', 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)
client = {}


def main():
    while True:
        receive, addr = s.recvfrom(1024)
        command = receive.decode().split('::')[0]
        data = receive.decode().split('::')[1]

        # For new user
        if command == '__newUser__':
            welcome_message = '__message__::Welcome, ' + data + '!'
            client[addr] = data
            print(data + ' enters the chatroom!')

            for address in client.keys():
                s.sendto(welcome_message.encode(), address)

        # For general messages
        if command == '__message__':
            for address in client.keys():
                s.sendto(receive, address)

        # For leaving user
        if command == '__exit__':
            leaving_message = '__message__::' + client[addr] + ' leaves the chatroom!'
            print(client[addr] + ' leaves the chatroom!')
            client.pop(addr)
            for address in client.keys():
                s.sendto(leaving_message.encode(), address)


if __name__ == '__main__':
    main()
