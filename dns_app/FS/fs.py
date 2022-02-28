from flask import Flask, request,make_response, abort, Response
import requests
import requests
import json
import socket
from socket import *

app = Flask(__name__)

# @app.route('/register')
# def register():
#     host_name = request.args.get('hostname')
#     ip_address = '0.0.0.0'
#     dict = {}
#     dict['name'] = host_name
#     dict['address'] = ip_address
#     r = requests.post('http://0.0.0.0:53533', data = dict)
#     return r.text

@app.route('/register', methods = ['PUT'])
# @app.route('/register')
def register():
    content = request.get_json()
    hostname = content.get('hostname')
    ip = content.get('ip')
    as_ip = content.get('as_ip')
    as_port = int(content.get('as_port'))

    json = {'TYPE': 'A', 'NAME': hostname, 'VALUE': ip, 'TTL': 10}

    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.sendto(json.dumps(json).encode(), (as_ip, as_port))
    response_message, server_address = client_socket.recvfrom(2048)

    response = make_response(json.loads(response_message.decode()), 201)
    response.mimetype = "text/plain"
    return response
    

@app.route('/fibonacci')
def Fibonacci():
    x = request.args.get('number')
    result = Fibonacci_calculator(int(x))
    # return str(result)
    return Response("the fibo for "+str(x)+" is: "+str(result), status = 200)

def Fibonacci_calculator(n):
    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci_calculator(n-1) + Fibonacci_calculator(n-2)


app.run(host='0.0.0.0',
        port=9090,
        debug=True)