from flask import Flask, render_template

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






# -------------------------------------------------------------------------------------------













if __name__ == '__main__':
    app.run(debug=True)
