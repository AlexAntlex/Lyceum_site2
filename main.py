from flask import Flask
import datetime

from data import db_session
from data.jobs import Job
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    app.run()


if __name__ == '__main__':
    db_session.global_init("db/blogs.sqlite")

    session = db_session.create_session()
    jobs = Job()
    jobs.team_leader = 1
    jobs.job = 'deployment of residential modules 1 and 2'
    jobs.work_size = 15
    jobs.collaborators = '1, 2'
    dateTimeObj = datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%H:%M:%S.%f - %b %d %Y")
    jobs.start_date = timestampStr
    jobs.is_finished = False
    session.add(jobs)
    session.commit()

    main()



