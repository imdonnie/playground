from flask import Flask
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

globalPath = {
	'win_upload_path':r'D:\Python3\flask_app\uploads',
}

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        save_filename = globalPath['win_upload_path']+'\\'+secure_filename(f.filename)
        f.save(save_filename)
        return save_filename