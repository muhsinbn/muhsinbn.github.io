from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')  # Assuming the HTML is saved as 'register.html'

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['psw']
    password_repeat = request.form['psw-repeat']

    # Here you can add logic to validate the data, save it to a database, etc.
    if password == password_repeat:
        # For example, save the user to a database (code omitted)
        return redirect(url_for('success'))  # Redirect to a success page
    else:
        # Handle the case where passwords don't match
        return 'Passwords do not match!', 400

@app.route('/success')
def success():
    return 'Registration successful!'

if __name__ == '__main__':
    app.run(debug=True)

