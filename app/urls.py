from app import app
from .views import index, todo_delete, todo_update

# home route
app.add_url_rule('/', 'home', index, methods=['GET','POST'])
# delete route
app.add_url_rule('/delete/', 'delete', todo_delete, methods=['GET','POST'])
# update route
app.add_url_rule('/update/', 'update', todo_update, methods=['GET','POST'])


