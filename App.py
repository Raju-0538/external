from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App! Go to /register to register."

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        
        return render_template('success.html', name=username)

    return render_template('v2.html')

if __name__ == '__main__':
    app.run(debug=True)