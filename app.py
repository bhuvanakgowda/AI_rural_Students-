import google.generativeai as genai
import os

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "eduassist"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eduassist"
)

cursor = db.cursor()

@app.route('/ask', methods=['POST'])
def ask():

    question = request.form['question']

    response = model.generate_content(question)

    return {"answer": response.text}
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        sql = "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)"
        values = (name, email, password)

        cursor.execute(sql, values)
        db.commit()

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM users WHERE email=%s AND password=%s"
        values = (email, password)

        cursor.execute(sql, values)

        user = cursor.fetchone()

        if user:
            session['user'] = user[1]
            return redirect('/dashboard')
        else:
            return "Invalid Login"

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():

    if 'user' in session:
        return render_template('dashboard.html', name=session['user'])

    return redirect('/login')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
