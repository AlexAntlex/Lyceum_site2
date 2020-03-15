from flask import Flask, render_template

from data import db_session
from data.jobs import Job

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


if __name__ == '__main__':
    main()



