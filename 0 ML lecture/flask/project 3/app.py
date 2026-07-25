from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "pradhans284"              # setting up secret key

# -------------------------------------------------------------------------------------------
# Home page / Welcome page
@app.route('/')
def welcome():
    return render_template('1_welcome_page.html')

# -------------------------------------------------------------------------------------------
# going to the login page (2_login_page.html)
@app.route('/login')
def login():
    return render_template('2_login_page.html')

# -------------------------------------------------------------------------------------------
# getting the login information
@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('username')        # flask receives the 'username' bcoz the name is set 'username' for the name input field
    user_email = request.form.get('email')

    # putting admin previlage
    admins={
        'name' : 'admin',
        'email' : 'admin@123'
    }

    admin_html = f"<h2>Hello {user_name}</h2>"

    if user_name in admins['name'] and user_email in admins['email']:
        return render_template('3_page.html', name=user_name, email=user_email)
    elif user_name and user_email:
        return render_template('3_page.html', name=user_name, email=user_email)
    else:
        return render_template('2_login_page.html')


# -------------------------------------------------------------------------------------------













if __name__ == '__main__':
    app.run(debug=True)
