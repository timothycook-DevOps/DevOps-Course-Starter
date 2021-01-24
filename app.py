from flask import Flask, render_template, request, redirect, url_for
import ApiAccess as api
import View_Model as model

app = Flask(__name__)
app.config.from_object('flask_config.Config')

obj2 = model.ViewModel()


@app.route('/')
def index():
    obj2.add_items()
    obj2.seperate_done_items()
    return render_template('index.html', object_items=obj2)


@app.route('/add_item/', methods=['POST'])
def add_item():
    NewItem = request.form["NewItem"]
    obj2.create_new_item(NewItem)
    obj2.add_items()
    return render_template('index.html', object_items=obj2)


@app.route('/start_item/<item>', methods=['GET'])
def start_item(item):
    obj2.start_item(item)
    obj2.add_items()
    return render_template('index.html', object_items=obj2)


@app.route('/complete_item/<item>', methods=['GET'])
def complete_item(item):
    obj2.complete_item(item)
    obj2.add_items()
    obj2.seperate_done_items()
    return render_template('index.html', object_items=obj2)


@app.route('/show_all/', methods=['GET'])
def show_all():
    return render_template('index.html', object_items=obj2)


if __name__ == '__main__':
    app.run(debug=True)
