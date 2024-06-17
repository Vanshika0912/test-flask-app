from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vanshika:rVCvnJYpnxuaxIwd9XI72u3DZXKTP0nk@dpg-cpmjoquehbks73fq36r0-a.oregon-postgres.render.com/test_db_nzvl'
    # 'postgresql://vanshika:rVCvnJYpnxuaxIwd9XI72u3DZXKTP0nk@dpg-cpmjoquehbks73fq36r0-a.oregon-postgres.render.com/test_db_nzvl'
    # 'postgresql://vanshika:rVCvnJYpnxuaxIwd9XI72u3DZXKTP0nk@dpg-cpmjoquehbks73fq36r0-a/test_db_nzvl'
    #'postgresql://postgres:vgarg@localhost:5432/test_flask_db'

db = SQLAlchemy(app)
class Task(db.Model):
#     __table__ = 'tablename'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
with app.app_context():
    db.create_all()

@app.route('/tasks')
def get_tasks():
    tasks = Task.query.all()
    task_list = [
        {'id': task.id, 'title': task.title, 'done': task.done} for task in tasks
    ]
    return jsonify({"Tasks":task_list})


@app.route('/form')
def index():
    return render_template('form.html')
@app.route('/submit', methods=['POST'])
def submit():
    data=request.get_json()
    new_task = Task(title=data['title'], done=data['done'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"Message":"task added!"})
    # title = request.form['title']
    # done = request.form.get('done') == 'on'
    # new_task = Task(title=title, done=done)
    # db.session.add(new_task)
    # db.session.commit()
    # return redirect(url_for('success'))
@app.route('/success')
def success():
    return "Task added successfully!"
@app.route('/')
def home():
    # return 'Hello, World! DevMart is coming SooN!'
    return render_template('index.html')
@app.route('/app')
def somethingother():
    return jsonify({"Going":"Good"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
