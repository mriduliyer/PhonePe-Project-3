from flask import Flask, render_template

app = Flask(__name__)

# Root route to render main.html
@app.route('/', methods=['GET'])
def render_main():
    return render_template('main.html')

@app.route('/view', methods=['GET'])
def view():
    return render_template('view.html')

@app.route('/metrics', methods=['GET'])
def metrics():
    return render_template('metrics.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000, debug=True)

