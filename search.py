from flask import Flask, render_template, request, jsonify
import re, os, socket

app = Flask(__name__)

@app.route('/search')
def Pinging():
    a = request.args.get('a', 0, type=str)
    def buffer_data():
        search_data = []
        with open('search.txt', 'w',encoding="utf-8") as search:
            for line in a:
                textdata = search.write(line.strip(''))
                print("line printed." + str(line))
        with open("search.txt", 'r', encoding="utf-8") as search1:

            for row in search1.read().split():
                response = os.popen(f"ping {row} -n 1").read()
                if "Received = 1" and "TTL" in response:
                    search_data.append(row + " --Active" + "\n")
                else:
                    search_data.append(row + " --Inactive" + "\n")


            return ("".join(search_data))
            print("Complete")
    return jsonify(sear=buffer_data())


@app.route('/searc')
def mainApp():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
