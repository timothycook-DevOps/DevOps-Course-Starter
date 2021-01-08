from flask import Flask, render_template, request, redirect, url_for
import ApiAccess as api
import View_Model as model

app = Flask(__name__)
app.config.from_object('flask_config.Config')


obj1 = api.AccessTrelloApi()
"""

def get_items():

    Items1 = obj1.getCardsFromTrelloList(
        api.TODOLISTURL, 'To Do')

    Items2 = obj1.getCardsFromTrelloList(
        api.DONELISTURL, 'Done')

    return Items1 + Items2
"""
obj2 = model.ViewModel()


@app.route('/')
def index():
    obj2.add_items()
    return render_template('index.html', items=obj2.get_items())


@app.route('/add_item/', methods=['POST'])
def add_item():
    NewItem = request.form["NewItem"]
    obj1.AddItemTodoList(NewItem)
    obj2.add_items()
    return render_template('index.html', items=obj2.get_items())


@app.route('/complete_item/<item>', methods=['GET'])
def complete_item(item):
    obj1.MarkItemAsDone(item)
    obj2.add_items()
    return render_template('index.html', items=obj2.get_items())


if __name__ == '__main__':
    app.run(debug=True)
