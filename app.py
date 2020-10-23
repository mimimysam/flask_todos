from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

if __name__ == '__main__':
   app.run(debug=True)

@app.route("/")
def index():
   todos = Task.query.all()
   return render_template("todo.html", todos=todos)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("db.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Task: {}>".format(self.task)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("todo-text")
    new_task = Task(task=task)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/mark_complete/<int:task_id>")
def mark_complete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for("index"))