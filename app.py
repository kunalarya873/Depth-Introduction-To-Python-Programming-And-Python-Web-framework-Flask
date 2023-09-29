from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        todo_title = request.form['title']
        desc_todo =request.form['desc']
        data = Todo(title=todo_title, desc=desc_todo)
        db.session.add(data)
        db.session.commit()
    alltodo = Todo.query.all()
    # db.create_all()
    # Create a new Todo instance and add it to the database session
    # new_todo = Todo(title="First Todo", desc="Testing first todo!")
    # db.session.add(new_todo)
    # db.session.commit()
    return render_template('index.html', alltodo=alltodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
