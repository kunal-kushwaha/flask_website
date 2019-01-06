from flask import Flask, render_template
from article import Article
app = Flask(__name__)

posts = [
    Article('title', 'subtitle', "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", 'jatin katyal'),
    Article('title', 'subtitle', 'body', 'kunal kushwaha'),
    Article('title', 'subtitle', 'body', 'shashank'),
    Article('title', 'subtitle', 'body', 'apoorv goyal')
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=posts)

@app.route('/articles/<int:id>')
def article(id):
    try: 
        post = posts[id-1]
        return render_template('article.html', article=post)
    except IndexError:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)