from flask import Flask, render_template
app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = 'brunodamato.com'

@app.route('/')
def index():
    return render_template('brunodamato.com/index.html')

@app.route('/', subdomain='www')
def www_index():
    return render_template('brunodamato.com/index.html')


@app.route('/', subdomain='work')
def workana_index():
    return '''  <a href=http://www.brunodamato.com>Index</a>  '''

if __name__ == '__main__':
    app.run(host='172.31.30.116', port=80)
