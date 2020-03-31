from flask import jsonify, request
from flask_restful import abort, Resource

from data import db_session
from data.jobs import Job
from api.job_parser import parser


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        abort(404, message=f'Job {job_id} not exist')


def abort_if_job_not_correct():
    if not request.json:
        abort(400, message='error: Empty request')
    if not all(key in request.json for key in
               ['team_leader', 'job', 'work_size',
                'collaborators', 'start_date', 'is_finished']):
        abort(400, message='error: Bad Request')


class JobsResource(Resource):    # one job
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Job).get(job_id)
        return jsonify({'job': jobs.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                  'is_finished')
        )})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Job).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, job_id):
        abort_if_job_not_correct()
        abort_if_job_not_found(job_id)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Job).get(job_id)

        job.team_leader = args['team_leader']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.start_date = args['start_date']
        job.is_finished = args['is_finished']
        job.job = args['job']

        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):     # all jobs
    def get(self):
        session = db_session.create_session()
        job = session.query(Job).all()
        return jsonify({'job': [
            item.to_dict(
                only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                      'is_finished')
            ) for item in job
        ]
        })

    def post(self):
        abort_if_job_not_correct()
        args = parser.parse_args()
        session = db_session.create_session()
        job = Job(
            team_leader=args['team_leader'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            is_finished=args['is_finished'],
            job=args['job']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})