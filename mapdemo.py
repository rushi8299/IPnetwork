from flask import Flask, render_template, request, jsonify
import re, os, socket, colorama,turtle
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

app = Flask(__name__)

@app.route('/mapdemo')
def map():
    b = request.args.get('a', 0, type=str)
    def map1():
        deptnm= []
        store1_data=[]
        store2_data=[]
        store1_da=[]
        with open("mapdemo.txt", 'r', encoding="utf-8") as infile2:

            for roww in infile2:
                row = roww.split()
                response = os.popen(f"ping {row[1]} -n 1").read()

                if "Received = 1" and "Minimum" and "TTL" and "Approximate" in response:
                    # store1_data.append(row[0] + " " + row[1] + " Active " + row[2] + "/")
                    store1_data.append("_" + row[0] + " " + "/ ")
                # elif "Destination net unreachable." in response:
                #     store1_data.append(row[0] + " " + row[1] + " Destination_net_unreachable " + row[2] + "/")
                else:
                    store1_data.append("0" + row[0] + " " + "/ ")

            return ("".join(store1_data))
    return jsonify(mapinfo=map1())



@app.route('/mappdemo')
def mainmapdemo():
    return render_template('mapdemo.html')

if __name__ == "__main__":
    app.run(debug=True)
