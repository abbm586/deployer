from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound
from flask_login import login_required


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__, template_folder='templates', static_folder='static'
)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    """ Serve unauthenticate home Page"""
    return render_template('index.html', segment='index',
                           title='Orchestration Login Page',
                           subtitle='Login is requested for elevated access'
                           )


@home_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """ Serve unauthenticate home Page"""
    return render_template('dashboard.html', segment='dashboard',
                           title='Orchestration Login Page',
                           subtitle='Login is requested for elevated access'
                           )
