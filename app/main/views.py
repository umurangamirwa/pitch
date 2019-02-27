from flask import render_template,request,redirect,url_for, abort
from . import main
# from ..request import get_movies,get_movie,search_movie
from .forms import pitchForm, UpdateProfile
from ..import db, photos
from ..models import User, Pitch, Comment
from flask_login import login_required, current_user
@main.route('/')
@login_required
def index():


    '''
    View root page function that returns the index page and its data
    '''

    title = 'pitches'
    product_pitch = pitch.query.filter_by(category = 'product.Pitch').all()
    pickup_lines = pitch.query.filter_by(category = 'pickup Lines').all()
    interview_pitch = pitch.query.filter_by(category = 'Interview pitch').all()
    promotion_pitch = pitch.query.filter_by(category = 'Interview pitch').all()
    return render_template('index.html', title = title,product_pitch=product_pitch,pickup_lines=pickup_lines,promotion_pitch=promotion_pitch)
# @main.route('/movies/<int:id>')
# def movies(movie_id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('movie.html',id = movie_id)
# @main.route('/movie/<int:id>')
# def movie(id):

#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     movie = get_movie(id)
#     title = f'{movie.title}'
#     reviews = Review.get_reviews(movie.id)

#     return render_template('movie.html',title = title,movie = movie,reviews = reviews)
# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'
#     return render_template('search.html',movies = searched_movies)

# @main.route('/reviews/<int:id>')
# def movie_reviews(id):
#     movie = get_movie(id)

#     reviews = Review.get_reviews(id)
#     title = f'All reviews for {movie.title}'
#     return render_template('movie_reviews.html',title = title,reviews=reviews)

@main.route('/review/<int:id>')
def single_review(id):
    # review=Review.query.get(id)
    if review is None:
        abort(404)
    # format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    # return render_template('review.html',review = review,format_review=format_review)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
def new_review(id):
    form = ReviewForm()
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        # new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)

        # save review method
    #     new_review.save_review()
    #     return redirect(url_for('.movie',id = movie.id ))

    # title = f'{movie.title} review'
    # return render_template('new_review.html',title = title, review_form=form)

@main.route('/user/<uname>')

def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/pitch/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()    

    if pitch_form.validate_on_submit():
        pitch = Pitch(title = pitch_form.title.data, category = pitch_form.category.data, pitch_content = pitch_form.pitch_content.data, author = pitch_form.author.data)

        db.session.add(pitch)
        db.session.commit() 
        
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html', pitch_form = pitch_form)   

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/pitch/comments', methods = ['GET', 'POST'])
@login_required
def comments():    
    comments_form = CommentsForm() 
    comments = Comment.query.all()    

    if comments_form.validate_on_submit():       

        # Updated comment instance
        new_comment = Comment(body = comments_form.body.data)

        # Save review method
        new_comment.save_comment()
        return redirect(url_for('main.comments'))
    return render_template('comments.html', comments_form = comments_form, comments = comments)


