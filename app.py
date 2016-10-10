from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/bar')
def bar():
    return render_template('int_bar.html')


@app.route('/line')
def line():
    return render_template('int_line.html')


@app.route('/filter')
def filter():
    return render_template('int_line_filter.html')


@app.route('/scatter')
def scatter():
    return render_template('int_scatter.html')


if __name__ == '__main__':
    app.run(debug=True)
