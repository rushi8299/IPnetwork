from flask import Flask, render_template, request, jsonify
import re, os, socket, colorama,turtle
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

app = Flask(__name__)



@app.route('/data_center')
def datacenter():
    a = request.args.get('a', 0, type=str)
    def data():
        center_data = []
        # with open('search.txt', 'w',encoding="utf-8") as search:
        #     for line in a:
        #         textdata = search.write(line.strip(''))
        #         print("line printed." + str(line))
        with open("datacenter.txt", 'r', encoding="utf-8") as search1:

            for row in search1.read().split():
                response = os.popen(f"ping {row} -n 2").read()
                if "Received = 2" and "TTL" in response:
                    center_data.append(row + " Active " + "/")
                else:
                    center_data.append(row + " Inactive " + "/")


            return ("".join(center_data))
    return jsonify(centerdata=data())


@app.route('/')
def mainsearch():
    return render_template('tree.html')


if __name__ == "__main__":
    app.run(debug=True)
