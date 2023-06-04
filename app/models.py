from app import db

class ToDoList(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String())
    create_at = db.Column(db.String())

    def __init__(self, content, create_at):
        self.content = content
        self.create_at = create_at

