from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from flask import Blueprint
from flask import current_app as app

from apps import login_manager
from .forms import LoginForm
from .models import Users


# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__, template_folder='templates', static_folder='static'
)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Create the Login Page"""
    if current_user.is_authenticated:
        return render_template(url_for('home_bp.home'))
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(abNumber= form.abNumber.data).first()

        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home_bp.dashboard'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login'))

    return render_template('login.html', form=form, segment='login',
                           title='Orchestration Login Page',
                           subtitle='Login is requested for elevated access'
                           )


@auth_bp.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    """User log-out logic"""
    logout_user()
    return redirect(url_for('home_bp.home'))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return Users.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
