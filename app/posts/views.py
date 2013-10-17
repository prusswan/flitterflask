from flask import Blueprint, render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager

from app.users.models import User
from app.posts.models import Post
from forms import SubmitPostForm

from sqlalchemy import desc

mod = Blueprint('posts', __name__)

from config import POSTS_PER_PAGE

@mod.route('/flitter/user/<username>', methods=('GET', 'POST'))
@app.route('/flitter/user/<username>/<int:page>', methods = ['GET', 'POST'])
def posts_view(username=None, page=1):
    user = db.session.query(User).filter_by(name=username).first()
    if user is None:
        return render_template('404.html'), 404

    posts = user.posts.order_by(desc(Post.created_at)).paginate(page, POSTS_PER_PAGE, False)

    form = None
    if current_user == user:
        form = SubmitPostForm(request.form)

        if form.validate_on_submit():
            post = Post()
            form.populate_obj(post)
            post.user_id = current_user.id
            db.session.add(post)
            db.session.commit()
            return redirect('/flitter/user/' + username)

    return render_template('posts/index.html', form=form, posts=posts, username=user.name)
