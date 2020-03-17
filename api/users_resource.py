from flask import jsonify
from flask_restful import abort, Resource

from data import db_session
from data.users import Job
from api.user_parser import parser


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(Job).get(user_id)
    if not user:
        abort(404, message=f'User {user_id} not exist')


class UsersResource(Resource):    # one user
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(Job).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('email', 'name', 'position', 'surname', 'age',
                  'speciality', 'address')
        )})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(Job).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, user_id):
        abort_if_user_not_found(user_id)
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(Job).get(user_id)

        user.email = args['email']
        user.name = args['name']
        user.position = args['position']
        user.surname = args['surname']
        user.age = args['age']
        user.speciality = args['speciality']
        user.address = args['address']

        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):     # all users
    def get(self):
        session = db_session.create_session()
        user = session.query(Job).all()
        return jsonify({'user': [
            item.to_dict(
                only=('email', 'name', 'position', 'surname', 'age',
                      'speciality', 'address')
            ) for item in user
        ]
        })

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = Job(
            email=args['email'],
            name=args['name'],
            position=args['position'],
            surname=args['surname'],
            age=args['age'],
            speciality=args['speciality'],
            address=args['address']
        )
        session.add(users)
        session.commit()
        return jsonify({'success': 'OK'})