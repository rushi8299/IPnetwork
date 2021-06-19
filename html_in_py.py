import webbrowser, colorama
import time
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

country = "Indiaaaaa"
html_content = f"<html> <head> </head> <h1> {country}  </h1> <body> </body> </html>"

with open("alldepts.html","w") as html_file:
    html_file.write(bcolors.UNDERLINE + html_content)
    # for row in html_content:
    #     roww = row.split()
    #     if "India" in roww:
    #         print("Maharashtra")
print(bcolors.UNDERLINE + "hii")

time.sleep(1)
# webbrowser.open("alldepts.html")