from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.restless import APIManager
from flask_restful import Resource, Api
import mysql.connector


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(45))


#manager = Api(app, flask_sqlalchemy_db=db)

# manager.create_api(Person)
# manager.create_api(TestTable)
#api.add_resource(TestTable, '/table')

# endpoint to show all users


@app.route("/testTable", methods=["GET"])
def get_data():
    all_data = TestTable.query.all()
    result = users_schema.dump(all_data)
    return jsonify(result.data)


if __name__ == "__main__":
    app.run(debug=True)
