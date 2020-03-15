from django.shortcuts import redirect
from flask import Flask, render_template

from data import db_session
from data.jobs import Job
from data.users import User
from form.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mars_for_everyone'


def main():
    db_session.global_init("db/mars.sqlite")
    app.run()


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()



