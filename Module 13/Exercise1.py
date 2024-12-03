from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<num>')
def prime_check(num):
    num = int(num)
    i = 2
    isPrime = 1
    if num <= 2:
        isPrime = num - 1
    else : 
        while i * i < num :
            if num % i == 0 :
                isPrime = 0
                break
            i += 1
    
    response = {
        "Number" : num,
        "isPrime": bool(isPrime)
    }
    return response
                

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
