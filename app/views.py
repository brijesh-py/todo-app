from flask import render_template, redirect, request, url_for
from datetime import datetime
from .models import ToDoList
from app import db

# home page
def index():
    todolist = ToDoList.query.all()
    if request.method == 'POST':
        content = request.form['content'].strip()
        if content:
            created_time = datetime.now().strftime("%b %d %Y - %H:%M")
            add_todo = ToDoList(content=content, create_at=created_time)
            db.session.add(add_todo)
            db.session.commit()
            return redirect(url_for('home', success='Todo successfully added.'))
        return redirect(url_for('home', error='Todo content empty.'))
    return render_template("index.html", todolist=todolist)

# delete todo
def todo_delete():
    todo_id = request.args.get('query')
    todo = ToDoList.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('home', success='Todo successfully deleted.'))
    return redirect(url_for('home', error='Todo not found.'))

# delete todo
def todo_update():
    if request.method == 'POST':
        content = request.form['content'].strip()
        todo_id = request.form['todo-id']
        if content and todo_id:
            update_todo = ToDoList.query.filter_by(id=int(todo_id)).first()
            update_todo.content = content
            db.session.commit()
            return redirect(url_for('home', success='Todo successfully updated.'))
        return redirect(url_for('home', error='Todo not update.'))
    return redirect(url_for('home', error='Method not allow.'))
    

