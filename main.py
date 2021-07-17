from flask import Flask
app = Flask(__name__)


@app.route('/shortlinks', methods=['GET', 'POST'])
def short_links():
    if request.method == 'POST':
        return get_short_links()
    else:
        return post_short_link(request.json)
