import imp
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# make app know where to connect to the database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre123@localhost/height_collector'
db = SQLAlchemy(app) # create a SQLAlchemy object for the Flask Application

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    height_= db.Column(db.Integer, unique=True, nullable=False)
    volatge_ = db.Column(db.Integer)

    def __init__(self, height_, voltage_,):
        self.height_ = height_
        self.voltage_ = voltage_

@app.route("/")
def index():
    return render_template("form.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        height = request.form["height_name"]
        voltage = request.form["voltage_name"]
        print(height, voltage)

        # check if the email has already existed in the db
        # it's a int 
        if db.session.query(Data).filter(Data.height_== height).count() == 0:
            data = Data(height) #create a data object
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    
    return render_template('success.html',
    text="Seems like we got something from the email address already!")
if __name__ == '__main__':
    app.debug=True
    # app.run(debug=True, port=8080)
    app.run()
    