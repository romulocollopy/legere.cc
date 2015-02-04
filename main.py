from bottle import Bottle, run, static_file


app = Bottle()

@app.route('/')
def hello():
    return "<h1>Legere!<h1>"

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')

run(app, host='localhost', port=8080)
