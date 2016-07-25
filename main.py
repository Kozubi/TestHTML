import flask
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


# main route
@app.route("/")
def home():
    return "Heloo"


# route providing informations
@app.route("/items", methods=["POST"])
def items():
    items_db = {"woda": 1, "warzywa": 2, "sok": 1, "chleb": 3}
    answer = flask.jsonify(items_db)
    return answer


@app.route('/storage/<int:number>', methods=['POST', 'GET'])
def storage(number):
    # POST
    # create table with name = number
    # save stuff provided from webpage
    if request.method == 'POST':
        print(number)


    # GET
    # get information from db
    # send it back to web page
    else:
        return redirect(url_for('home'))


app.run(debug=True)
