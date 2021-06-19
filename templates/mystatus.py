from flask import Flask, render_template, request, jsonify
import re, os, socket, colorama,turtle
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

@app.route('/')
def status():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip=[]
    finalstat=[]
    ip.append(ip_address)

    def mystat():
        for row in ip:
            response = os.popen(f"ping {row} -n 2").read()
            if "Minimum" and "TTL" and "Approximate" in response:
                finalstat.append(hostname + row + " Active")
            else:
                finalstat.append(hostname + row + "inactive")

        return ("".join(ip))
    return jsonify(result=mystat())

@app.route('/findmystatus')
def mainstat():
    return render_template('status.html')