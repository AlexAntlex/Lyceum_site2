from flask import Flask

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

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session = db_session.create_session()
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Planet"
    user.name = "Mars"
    user.age = 4.603E9
    user.position = "expeditions"
    user.speciality = "subject of study"
    user.address = "Mars"
    user.email = "Mars_plnet@mars.org"
    user.hashed_password = "red_planet_for_everyone"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

    user = User()
    user.surname = "rover"
    user.name = "Sojourner"
    user.age = 23
    user.position = "equipment"
    user.speciality = "rover"
    user.address = "Mars"
    user.email = "Sojourner@mars.org"
    user.hashed_password = "where_water"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

    main()

