from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, InputRequired


class JobForm(FlaskForm):
    job = StringField('Job', validators=[DataRequired()])
    team_leader = IntegerField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('work size', validators=[InputRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    start_date = StringField('Start date', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?', validators=[DataRequired()])
    submit = SubmitField('Submit')