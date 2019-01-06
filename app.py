from flask import Flask, render_template, request
from article import Article
app = Flask(__name__)

postss = []

@app.route('/')
def index():
    return render_template('index.html', size=len(postss))

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=postss)

@app.route('/articles/<int:id>')
def article(id):
    try: 
        post = postss[id-1]
        return render_template('article.html', article=post)
    except IndexError:
        return render_template('404.html')

@app.route('/new_article', methods=['GET', 'POST'])
def new_article():
    if request.method == "GET":
        return render_template('new_article.html')
    else:
        article = Article(
            request.form['title'],
            request.form['subtitle'],
            request.form['body'],
            request.form['author']
        )
        posts.append(article)
        return "Created Successfully"

@app.route('/tv')
def tv():
    return render_template('tv.html')

@app.route('/songs')
def songs():
    return render_template('songs.html')



if __name__ == '__main__':
    app.run(port=8000, debug=True)