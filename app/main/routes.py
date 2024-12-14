"""
Contains routes for main purpose of app
"""
import os
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from prometheus_client import Gauge
from app import db
from app.main.forms import EditProfileForm, PostForm
from app.models import User, Post
from app.main import bp

alert_button_gauge = Gauge("alert_button_gauge", "State of the alert button (1 = active, 0 = inactive)")

@bp.before_request
def before_request():
    """
    update last_seen for User before handling request
    """
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        current_app.logger.debug(f"{current_user} is authenticated")
        db.session.commit()



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required 
def index():
    """
    Route for index page
    """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        current_app.logger.debug(f"{post}")
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))

    posts = current_user.followed_posts().all()
    return render_template("index.html", title='Home Page', form=form,
                           posts=posts)



@bp.route('/explore')
@login_required
def explore():
    """
    Route for explore
    """
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', title='Explore', posts=posts)



@bp.route('/user/<username>')
@login_required
def user(username):
    """
    Route for user
    """
    user_ = User.query.filter_by(username=username).first_or_404()
    posts = user_.posts.all()
    return render_template('user.html', user=user_, posts=posts)



@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """
    Route for editing user profile
    """
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit(): #pylint: disable=no-else-return
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@bp.route('/follow/<username>')
@login_required
def follow(username):
    """
    Follow a User
    """
    user_ = User.query.filter_by(username=username).first()
    if user_ is None:
        flash(f'User {username} not found.')
        return redirect(url_for('index'))
    if user_ == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user_)
    db.session.commit()
    flash(f'You are following {username}!')
    return redirect(url_for('main.user', username=username))

@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    """
    Unfollow a User
    """
    user_ = User.query.filter_by(username=username).first()
    if user is None:
        flash(f'User {username} not found.')
        return redirect(url_for('index'))
    if user_ == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user_)
    db.session.commit()
    flash(f'You are not following {username}.')
    return redirect(url_for('main.user', username=username))

@bp.route('/version')
def version():
    """
    Preview the current version of microblog.
    """
    app_version = os.environ.get("VERSION") or "No version found"
    return render_template('version.html', version=app_version)

@bp.route('/alert')
def alert():
    """
    Page for starting alerts
    """
    return render_template('alert.html', active=False)

@bp.route("/start-alert", methods=["POST"])
def start_alert():
    """
    Actives alert in prometheus
    """
    alert_button_gauge.set(1)
    return render_template('alert.html', active=True)

@bp.route("/reset-alert", methods=["POST"])
def reset_alert():
    """
    Deactives alert in prometheus
    """
    alert_button_gauge.set(0)
    return render_template('alert.html', active=False)
