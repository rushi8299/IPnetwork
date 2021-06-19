import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLACK + Back.GREEN + " Active ")

# import os
# from time import sleep
#
# def add():
#     print("Down")
# #
# def sub():
#     print("UP")
#
# def ping():
#     online = os.system("ping -n 1 192.168.43.216")
#     print("rr",online)
#     if(online == 0):
#          print("Avilabe with ",online)
#          return True
#     else:
#          print("Ofline with ",online)
#          return False
#
# while True:
#    add()
#
# else:
#     print("Down")
#    sleep(0.5)
#    if( ping()):
#     sub()
