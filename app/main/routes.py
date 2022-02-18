from app.main import bp
from flask import render_template


@bp.route('/index', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html', title='Главная')


@bp.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('main/projects.html', title='Проекты')
