from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug = True)
    
@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit **order
        n = n//10
        
    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
            "Number" : copy_n,
            "Armstrong" : True,
            "server IP" : "122.234.213.53"
            # "Other Numbers" : [1,23,43,5,3]
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result = {
            "Number" : copy_n,
            "Armstrong" : False,
            "server IP" : "122.234.213.53"
            # "Other Numbers" : [1,23,43,3,3]
        }
        
        return jsonify(result)
    if __name__ == "__main__":
        app.run(debud = True)
            
        