from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="password123"


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')


@app.route('/destroy_session')
def clear_the_session():
    session.clear()
    return redirect ('/')


@app.route('/count', methods=['POST'])
def count_by_two():
    if request.form['change'] =='add':
        session['count'] += 1
    elif request.form['change'] =='reset':
        session['count'] = 0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)