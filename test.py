# -*- coding: UTF-8 -*-
import irc_client
import horoscope
import random
import requests
from url import youtube_search
from multiprocessing import Process, Manager
import sys, os

channel = "#CN_demo"
port = 6667
server = "127.0.0.1"
nick = "botT07902124"
user_name = "T07902124"

client = irc_client.Client()
client.connect(server, port, user_name, nick, channel)

client.greet()

tester = ""


def send_process(client_, tester_, fileno):

    sys.stdin = os.fdopen(fileno)
    while True:
        msg = input()
        client_.send_user(tester_, msg)



while True:
    received = client.extract()

    if "PRIVMSG" in received and nick in received:

        tester = received.split(':')[1].split('!')[0]
        content = received.split(nick + ' :')[1].split('\r')[0]
        # print("Private Massage:  " + received)
        print("from: " + tester + "   content: " + content)

        # client.send_user(tester, "you just said: " + content)

        if horoscope.hs(content)[0]:
            print("sending horoscope of " + content)
            client.send_user(tester, horoscope.hs(content)[1])

        if content == '!guess':
            client.send_user(tester, "猜一个1～10的数字吧～")
            guess = 0
            answer = random.randint(1, 10)
            guessed = []
            legal = range(1, 11)
            print(tester + " is playing guessing number. Answer is " + str(answer))

            while guess != answer:
                received = client.extract()

                if "PRIVMSG" in received and nick in received:
                    tester = received.split(':')[1].split('!')[0]
                    content = received.split(nick + ' :')[1].split('\r')[0]

                    if not content.isdigit():
                        continue

                    if int(content) in legal:
                        guess = int(content)

                        if guess == answer:
                            client.send_user(tester, "恭喜你，猜对了！ 答案是" + str(answer) + "!")

                        if guess < answer:
                            if guess in guessed:
                                client.send_user(tester, "你猜过" + str(guess) + "了诶 =_=!， 大于" + str(guess) + "!")
                            else:
                                client.send_user(tester, "答案大于" + str(guess) + "喔!~")
                                guessed.append(guess)

                        if guess > answer:
                            if guess in guessed:
                                client.send_user(tester, "你猜过" + str(guess) + "了诶 =_=!， 小于" + str(guess) + "!")
                            else:
                                client.send_user(tester, "答案小于" + str(guess) + "喔!~")
                                guessed.append(guess)

        if nick + ' :!song' in received:

            if len(content.split('!song ')) <= 1:
                client.send_user(tester, "请正确输入曲名～ 如[!song Perfect]")
            else:
                song_name = content.split('!song ')[1]
                client.send_user(tester, "Bot为你在Youtube查找歌曲: [" + song_name + "]")
                client.send_user(tester, youtube_search(song_name))

        if content == '!chat':
            print("==========" + tester + "想要跟你联系==========")
            flag = True
            fn = sys.stdin.fileno()
            while flag:

                p = Process(target=send_process, args=(client, tester, fn))
                p.start()

                received_msg = client.extract()
                if "PRIVMSG" in received_msg and nick in received_msg and tester in received_msg:
                    received_massage = received_msg.split(nick + ' :')[1].split('\r')[0]
                    print(tester + ":" + received_massage)
                    if received_massage == '!bye':
                        flag = False

                p.terminate()
                p.join()

                # received = client.extract()
                # if "PRIVMSG" in received and nick in received and tester in received:
                #     received_massage = received.split(nick + ' :')[1].split('\r')[0]
                #     print(tester + ":" + received_massage)
                #     if received_massage == '!bye'
                #         last_massage[0] = 1

            print("==========" + tester + "已离开聊天室==========")
