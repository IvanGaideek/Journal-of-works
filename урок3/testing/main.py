from flask import Flask, render_template
from data import db_session
from data.users import User, Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    data_jobs = db_sess.query(Jobs).all()
    team_leaders = []
    for i in data_jobs:
        team_leaders.append(' '.join(db_sess.query(User.surname, User.name).filter(User.id == i.team_leader).first()))
    return render_template('index.html', all=zip(data_jobs, team_leaders))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
