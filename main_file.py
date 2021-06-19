from flask import Flask, render_template, request, jsonify
import re, os, socket, colorama,turtle
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

app = Flask(__name__)

@app.route('/home')

@app.route('/')
def mainhome():
    return render_template('homE.html')

@app.route('/_ping_nodes')
def Pinging():
    a = request.args.get('a', 0, type=str)
    def buffer_data():
        store_data = []
        # with open('Buffer.txt', 'w',encoding="utf-8") as infile:
        #     for line in a:
        #         textdata = infile.write(line.strip(''))
        #         print("line printed." + str(line))
        with open("Buffer.txt", 'r', encoding="utf-8") as infile1:
            for roww in infile1:
                row = roww.split()

                response = os.popen(f"ping {row[1]} -n 1").read()

                if "Received = 1" and "Minimum" and "TTL" and "Approximate" in response:
                    store_data.append(row[0] + " " + row[1] + " Active " + "/")
                # elif "Destination net unreachable." in response:
                #     store_data.append(row[0] + " " + row[1] + " Destination_net_unreachable " + "/")
                else:
                    store_data.append(row[0] + " " + row[1] + " Inactive " + "/")


            return ("".join(store_data))
    return jsonify(result=buffer_data())

@app.route('/pingnorth')
def mainnorth():
    return render_template('ping_north.html')

@app.route('/_ping_south')
def Pingingsouth():
    b = request.args.get('a', 0, type=str)
    def dept():
        deptnm= []
        store1_data=[]
        store1_da=[]
        with open("buffer1.txt", 'r', encoding="utf-8") as infile2:

            for roww in infile2:
                row = roww.split()
                response = os.popen(f"ping {row[1]} -n 1").read()

                if "Received = 1" and "Minimum" and "TTL" and "Approximate" in response:
                    # store1_data.append(row[0] + " -- " + row[1] + '\033[31m' + " -- Active" + "\n")
                    store1_data.append(row[0] + " " + row[1] + " Active " + "/")
                elif "Destination net unreachable." in response:
                    store1_data.append(row[0] + " " + row[1] + " Destination_net_unreachable " + "/")
                else:
                    store1_data.append(row[0] + " " + row[1] + " Inactive " + "/")

            return ("".join(store1_data))
    return jsonify(deptinfo=dept())

@app.route('/pingsouth')
def mainsouth():
    return render_template('ping_south.html')


@app.route('/search')
def searchh():
    a = request.args.get('a', 0, type=str)
    def buffer_data():
        search_data = []
        with open('search.txt', 'w', encoding="utf-8") as search:
            for line in a:
                textdata = search.write(line.strip(''))
                print("line printed." + str(line))
        with open("search.txt", 'r', encoding="utf-8") as search1:

            for row in search1.read().split():
                response = os.popen(f"ping {row} -n 2").read()
                if "Received = 2" and "TTL" in response:
                    search_data.append(row + " --Active" + "/" + response)
                else:
                    search_data.append(row + " --Inactive" + "/" + response)


            return ("".join(search_data))
            print("Complete")
    return jsonify(sear=buffer_data())


@app.route('/searc')
def mainsearch():
    return render_template('search.html')

@app.route('/map')
def map():
    b = request.args.get('a', 0, type=str)
    def map1():
        deptnm= []
        store1_data=[]
        store2_data=[]
        store1_da=[]
        with open("tree.txt", 'r', encoding="utf-8") as infile2:

            for roww in infile2:
                row = roww.split()
                response = os.popen(f"ping {row[1]} -n 1").read()

                if "Received = 1" and "Minimum" and "TTL" and "Approximate" in response:
                    store1_data.append(row[0] + " " + row[1] + " Active " + row[2] + "/")
                elif "Destination net unreachable." in response:
                    store1_data.append(row[0] + " " + row[1] + " Destination_net_unreachable " + row[2] + "/")
                else:
                    store1_data.append(row[0] + " " + row[1] + " Inactive " + row[2] + "/")

            return ("".join(store1_data))
    return jsonify(mapinfo=map1())



@app.route('/mapp')
def mainmap():
    return render_template('tree.html')

@app.route('/findstatus')
def status():

    def mystat():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ip = []
        host = []
        finalstat = []
        ip.append(ip_address)
        host.append(hostname)
        for row in ip:
            response = os.popen(f"ping {row} -n 2").read()
            if "127.0.0.1" in response:
                finalstat.append(hostname + " " + "-------" + " " + "Inactive" + " /" + " ")
            else:
                finalstat.append(hostname + " " + row + " " + "Active" + " /" + " ")

        return ("".join(finalstat))
    return jsonify(status=mystat())

@app.route('/findmystatus')
def mainstat():
    return render_template('status.html')


if __name__ == "__main__":
    app.run(debug=True)
