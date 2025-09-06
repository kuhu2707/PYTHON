#Task 4: Build a simple Flask app that serves a "Hello World" page with a form input.

from flask import Flask , request 

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def home():
    if request.method == 'POST':
        name = request.form['name']
        email =  request.form['email']
        return f"Hello {name}! your email is {email}"
    
    return '''
        <form method='post'>
           Enter Name: <input type='text' name ='name'>
           <br>
           Enter Email: <input type='email' name='email'>
           <br>
           <button type='submit'>Login</button>
        </form>
'''

if __name__ == "__main__":
    app.run(debug=True)
    

