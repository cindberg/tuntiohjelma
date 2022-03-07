from flask import request, session, redirect, render_template, url_for
from index import Account, create_account, Calender
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from second import second

app.register_blueprint(second, url_prefix="")


@app.route('/')
def index():
    return redirect("/login")

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

    else:
        username = session['username']
        user = Account.query.filter_by(username=username).first()
        task_obj = Calender(
            account_id=user.id,
            account=user,
            planned_date=request.form['plan'],
            schedule_date=request.form['schedule'],
            end_date=request.form['end'],
            hours=request.form['hours'],
            task_name=request.form['name'],
            task_description=request.form['description']
        )
        db.session.add(task_obj)
        db.session.commit()
        return redirect(url_for('task'))


@app.route('/getacc', methods=['GET', 'POST'])
def getacc():
    accounts = Account.query.all()
    for i in accounts:
        print(i)
    return "Test a"


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if session and session['username']:
        print(session['username'])
        return redirect(url_for('home', username=session['username']))

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        account = Account.query.filter_by(username=username).first()

        if account and check_password_hash(account.password, password):
            session['username'] = username
            msg = 'Kirjauduit onnistuneesti!'
            return redirect(url_for('home', username=username))
        else:
            msg = 'Väärä käyttäjä / Salasana !'
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return render_template('out.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    carbrands = [
        {
            'brand_id': 1,
            'brand_name': 'Työntekijä'
        },
        {
            'brand_id': 2,
            'brand_name': 'Projektipäällikkö'
        }
    ]
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        roletype = request.form['search_category']
        # We find the correct roletype
        account = Account.query.filter_by(username=username).first()
        if account:
            msg = 'Tili on jo olemassa!'
        else:

            account = create_account(username, password, roletype)
            msg = 'Olet onnistuneesti rekisteröitynyt!'
            print(account)
    else:
        msg = 'Rekisteröidy!'

    return render_template('register.html', carbrands=carbrands, msg=msg)


@app.route('/task', methods=['GET', 'POST'])
def task():
    if session and session['username']:
        user_id = Account.query.filter_by(username=session['username']).first()
        calenders = Calender.query.filter_by(account_id=user_id.id).all()
        return render_template('task.html', data=calenders)

    else:
        return redirect(url_for('login'))


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
