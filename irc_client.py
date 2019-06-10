# -*- coding: UTF-8 -*-
import socket


class Client:

    def __init__(self):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.channel = " "
        self.user_name = " "
        self.nick = " "

    def get_form(self, str):
        a = str + '\r\n'
        return a.encode('utf-8')

    def connect(self, server, port, user_name, nick, channel):
        self.skt.connect((server, port))
        self.skt.send(self.get_form("NICK " + nick))
        self.skt.send(self.get_form("USER " + user_name + " " + user_name + " " + server + " :" + user_name))
        self.skt.send(self.get_form("JOIN " + channel))

        self.channel = channel
        self.user_name = user_name
        self.nick = nick

        print("connecting success! Server:" + server + " Port:" + str(port))

    def extract(self):
        str = self.skt.recv(2048).decode('utf-8')
        return str

    def send_channel(self, msg):
        self.skt.send(self.get_form("PRIVMSG " + self.channel + " :" + msg))

    def send_channel_(self, channel, msg):
        self.skt.send(self.get_form("PRIVMSG " + channel + " :" + msg))

    def send_user(self, user, msg):
        self.skt.send(self.get_form("PRIVMSG " + user + " :" + msg))

    def pure_send(self, msg):
        self.skt.send(self.get_form(msg))

    def greet(self):
        self.send_channel("I'm " + self.user_name)

    # def send_user_input(self, user):
    #     while True:
    #         msg = input()
    #         print(msg)
    #         self.send_user(user, msg)
