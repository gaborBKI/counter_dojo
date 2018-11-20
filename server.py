from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
counts = 0
count = {'GET': 0, 'POST': 0, 'DELETE': 0, 'PUT': 0}

@app.route('/')
def route_home():
    return render_template('home.html')


@app.route('/request-counter-get', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_get_request():
    global counts
    counts += 1
    count[request.method] += 1
    return redirect('/')


@app.route('/statistics')
def route_statistics():
    return render_template('statistics.html', counts = counts, count = count)


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
