from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

# client = MongoClient("mongodb+srv://username:password@clustername.qwgwafu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        due = request.form['due']
        todos.insert_one({'content': content, 'degree': degree, 'due': due})
        return redirect(url_for('index'))

    all_todos = todos.find().sort([('degree', ASCENDING), ('due', ASCENDING)])
    return render_template('index.html', todos=all_todos)


@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
