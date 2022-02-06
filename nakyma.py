from flask import request, session,redirect, render_template, url_for
from index import Account
from app import app





@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if session and session['username']:
            username = session['username']
            user = Account.query.filter_by(username=username).first()
            role = 'Työntekijä' if user.roletype == '1' else 'Projektipäällikkö'
        else:
            return redirect(url_for('login'))

        return render_template('home.html', username=username, role=role)





@app.route('/getacc', methods =['GET', 'POST'])
def getacc():
    accounts = Account.query.all()
    for i in accounts:
        print(i)
    return "toimiiko?"





@app.route('/login', methods =['GET', 'POST'])
def login():
    viesti = ''
    if session and session['username']:
        print(session['username'])
        return redirect(url_for('home', username=session['username']))

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        account = Account.query.filter_by(username=username).first()

        if account(account.password, password):
            session['username'] = username
            viesti = 'Kirjauduit onnistuneesti!'
            return redirect(url_for('home', username=username))
        else:
            viesti = 'Incorrect username / password !'
    return render_template('login.html', viesti=viesti)
    





@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return render_template('out.html')





@app.route('/about', methods =['GET','POST'])
def about():
    return render_template('about.html')