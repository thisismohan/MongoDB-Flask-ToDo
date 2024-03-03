from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask("__name__")
# Connection to Mongo DB
client = MongoClient("") # add connection string

# func to get, store & display todos
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=='POST':
        # getting content and degree from 'form' and storing in variables
        content=request.form['content']
        degree=request.form['degree']
        # inserting datas to mongodb 'flask_database' database's 'todos' collection
        todos.insert_one({'content':content,'degree':degree})
        return redirect(url_for('index'))
    all_todos=todos.find()

    return render_template("index.html",toos=all_todos)

# func to delete particular todo
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({'_id':ObjectId(id)})
    return redirect(url_for('index'))

# Creating database and collection to store the todos
db = client.flask_database
todos = db.todos


if __name__ == "__main__":
    app.run(debug=True)
