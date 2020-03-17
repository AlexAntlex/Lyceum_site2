import flask
from flask import jsonify, request

from data import db_session
from data.jobs import Job

blueprint = flask.Blueprint('jobs_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job', 'user.name', 'user.surname', 'work_size',
                                    'collaborators', 'start_date', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs_one(job_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('team_leader', 'job', 'user.name', 'user.surname', 'work_size',
                                       'collaborators', 'start_date', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size',
                  'collaborators', 'start_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    if session.query(Job).filter(Job.id == request.json['id']).first():
        return jsonify({'error': 'Id already exists'})
    jobs = Job(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        is_finished=request.json['is_finished']
    )
    session.add(jobs)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:news_id>', methods=['DELETE'])
def delete_job(job_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    session.delete(jobs)
    session.commit()
    return jsonify({'success': 'OK'})