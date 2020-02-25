from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
    hostname = request.host_url
    message = 'homeless map'
    return render_template('main.html', host=hostname, msg=message)


@app.route('/about', methods=['GET'])
def mission():
    return render_template('about.html')



@app.route('/map', methods=['GET'])
def map():
    return render_template('map.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/interface', methods=['GET'])
def interface():
    return render_template('interface.html')


