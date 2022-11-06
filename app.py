from flask import Flask, render_template, request
from user_data.listing import bp as listing_bp

app = Flask(__name__)
app.register_blueprint(listing_bp)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('main_page.html')


@app.route('/listing.js', methods=['GET'])
def send_js():
    with open('front_end/listing.js', 'rb') as js:
        return js.read()


if __name__ == '__main__':
    app.run(debug=True)
