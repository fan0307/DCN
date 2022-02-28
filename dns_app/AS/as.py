from socket import *
import requests
import json
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/home')
def AS_home():
    return "welcome to AS home page"
    
@app.route('/', methods = ['GET', 'POST'])
def AS():
# serverPort = 53533

# serverSocket = socket(AF_INET,SOCK_DGRAM)
# serverSocket.bind(('',serverPort))
# print("THe server is ready to receive")

# while True:
#     message, clientAddress=serverSocket.recvfrom(2048)

#     m = message.decode()
#     m=json.loads(m)
    
#     #DNS Query
#     if len(m) == 2:                            
#         with open("out.json", "r") as outfile:
#             dictionary = json.load(outfile)
#         DNS_response = dictionary[m["NAME"]]
#         dns_object = json.dumps(DNS_response)
#         serverSocket.sendto(dns_object.encode(),clientAddress)   
    if request.method == 'GET':
        key = request.args.get('name')
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            if key not in data:
                return Response("hostname not found", status = 404)
            else:
                address = data.get(key)
                return Response(address, status = 200)
#     #Registration
#     else:
#         database = {m["NAME"]: m}         
#         as_object = json.dumps(database)
#         with open("out.json", "w") as outfile:
#             outfile.write(as_object)
#         serverSocket.sendto(str(201).encode(), clientAddress)

    else:
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        dict = {}
        dict[host_name] = ip_address
        with open(file, 'w') as json_file:
            json.dump(dict, json_file)
        return Response("successfully registered", status = 200)
    
app.run(host='0.0.0.0',
        port=53533,
        debug=True)
   
