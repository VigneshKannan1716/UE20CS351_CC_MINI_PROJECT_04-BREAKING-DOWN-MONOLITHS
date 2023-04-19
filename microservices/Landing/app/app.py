from flask import Flask, render_template, request, flash, redirect, url_for


import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

# URL = 'http://landing-service:'


def add(n1, n2):
    URL = 'http://addition-service:'
    port = 5051
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1+n2


def minus(n1, n2):
    URL = 'http://subtraction-service:'
    port = 5052
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1-n2


def multiply(n1, n2):
    URL = 'http://multiplication-service:'
    port = 5053
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1*n2

def divide(n1, n2):
    URL = 'http://division-service:'
    port = 5054
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1/n2
    
def greater_than(n1, n2):
    URL = 'http://greater_than-service:'
    port = 5055
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1>n2

def less_than(n1, n2):
    URL = 'http://less_than-service:'
    port = 5056
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1<n2

def equal(n1, n2):
    URL = 'http://equal-service:'
    port = 5057
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1==n2

def gcd(n1, n2):
    URL = 'http://gcd-service:'
    port = 5063
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']

def modulus(n1, n2):
    URL = 'http://modulus-service:'
    port = 5059
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1%n2
   
def exponent(n1, n2):
    URL = 'http://exponent-service:'
    port = 5060
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
    # return n1**n2
    
def lcm(n1, n2):
    URL = 'http://lcm-service:'
    port = 5061
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    print(response)
    return response.json()['result']
       
@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result = minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            if number_2==0:
                        result = 'Zero Division Error'
            else:
                        result = divide(number_1, number_2)             
        elif operation == 'greater_than':
            result = greater_than(number_1, number_2)
        elif operation == 'less_than':
            result = less_than(number_1, number_2)
        elif operation == 'equal':
            result = equal(number_1, number_2)
        elif operation == 'modulus':
            if number_2==0:
                        result = 'Zero Division Error'
            else:
                        result = modulus(number_1, number_2)                                

        elif operation == 'exponent':
            if number_2==0:
                        result = 1
            else:
                        result = exponent(number_1, number_2)       
        elif operation == 'gcd':
            result = gcd(number_1, number_2)
        elif operation == 'lcm':
            if (number_1>number_2):
                        result = lcm(number_2, number_1)
            else:
                        result = lcm(number_1, number_2)                        
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        return render_template('index.html')
    except:
        flash(f'No input value')
        return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )

