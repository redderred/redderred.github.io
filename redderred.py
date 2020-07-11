from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'category': 'general',
        'title': 'At last, I begin',
        'when_where': '12 July 2020, 0314, from my favourite chair',
        'content': "Welcome to my new blog/website!"
    },
    {
        'category': 'category',
        'title': 'blog post',
        'when_where': 'date time place',
        'content': "this space is for content! <|:D this is a guy with a party hat. it's a hat party!"
    }
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='about')

if __name__ == '__main__':
    app.run(debug=True)