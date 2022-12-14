# Client side
import socket
import sys
import threading

# Configuration
SERVER = ('127.0.0.1', 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
NAME = ''


# Set the username
def set_username():
    global NAME
    NAME = input('Please enter your name: ')
    print('---\nEnter "__exit__" to exit the chatroom.\n---')
    message = '__newUser__::' + NAME
    s.sendto(message.encode(), SERVER)


def receive_messages():
    while True:
        receive, addr = s.recvfrom(1024)
        command = receive.decode().split('::')[0]
        message = receive.decode().split('::')[1]

        # For general messages
        if command == '__message__':
            print(message)


def send_messages():
    while True:
        message = input()

        # For leaving
        if message == '__exit__':
            message = '__exit__::__exit__'
            s.sendto(message.encode(), SERVER)
            print('Goodbye!')

            sys.exit()

        # For general messages
        else:
            message = '__message__::[' + NAME + ']:' + message
            s.sendto(message.encode(), SERVER)


def main():
    global SERVER
    # Threads Configuration
    SERVER = (input('Please input the chatroom server IP: '), 8888)
    receive_messages_from_server = threading.Thread(target=receive_messages)
    send_messages_to_server = threading.Thread(target=send_messages)

    # Set username
    set_username()

    # Start chatting
    receive_messages_from_server.start()
    send_messages_to_server.start()


if __name__ == '__main__':
    main()
