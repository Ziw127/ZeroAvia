# import Flask class and create an instance for this class
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import FetchedValue

# define the name of the application's module - app
app = Flask(__name__)
# make app know where to connect to the database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre123@localhost/ZeroAvia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # create a SQLAlchemy object for the Flask Application


class Temperature(db.Model):
    __tablename__ = 'temperature'
    id = db.Column(db.Integer, primary_key=True)
    opeLowTem = db.Column(db.Float, nullable=False)
    opeHighTem = db.Column(db.Float)
    shortLow = db.Column(db.Float)
    shortHigh = db.Column(db.Float)
    loss = db.Column(db.Float)
    groundSurLow = db.Column(db.Float)
    groundSurHigh = db.Column(db.Float)
    altitude = db.Column(db.Float)
    feet = db.Column(db.Float)
    decompression = db.Column(db.Float)
    overpression = db.Column(db.Float)
    category = db.Column(db.String)


    def __init__(self, opeLowTem, opeHighTem, shortLow, shortHigh, loss, groundSurLow, groundSurHigh, 
                 altitude, feet, decompression, overpression, category):
        self.opeLowTem = opeLowTem
        self.opeHighTem = opeHighTem
        self.shortLow = shortLow
        self.shortHigh = shortHigh
        self.loss = loss
        self.groundSurLow = groundSurLow
        self.groundSurHigh = groundSurHigh
        self.altitude = altitude
        self.feet = feet
        self.decompression = decompression
        self.overpression = overpression
        self.category = category


@app.route("/")
def index():
    return render_template("formTest.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        # Temperature and Altitude
        opeLowTem = request.form["op_low"]
        opeHighTem = request.form["op_high"]
        shortLow = request.form["sh_low"]
        shortHigh = request.form["sh_high"]
        loss = request.form["loss"]
        groundSurLow = request.form["gr_Low"]
        groundSurHigh = request.form["gr_High"]
        altitude = request.form["alt"]
        feet = request.form["feet"]
        decompression = request.form["decom"]
        overpression = request.form["overpre"]
        category = request.form["cat"]

        # test inputs
        print(category)
        print(opeLowTem, opeHighTem, shortLow, shortHigh, loss)
        print(groundSurLow, groundSurHigh, altitude, feet)
        print(decompression, overpression)
        # Category A1, A2, A3, A4
        if category == 'A1':
            opeLowTem, opeHighTem = -15.0, 55.0
            shortLow, shortHigh = -40.0, 70.0
            loss = 30.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 15.0, 4.6
        elif category == 'A2':
            opeLowTem, opeHighTem = -15.0, 70.0
            shortLow, shortHigh = -40.0, 70.0
            loss = 40.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 15.0, 4.6
        elif category == 'A3':
            opeLowTem, opeHighTem = -15.0, 70.0
            shortLow, shortHigh = -40.0, 85.0
            loss = 45.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 15.0, 4.6
        elif category == 'A4':
            opeLowTem = -15.0
            altitude, feet = 15.0, 4.6
        # Category B1, B2, B3, B4
        elif category == 'B1':
            opeLowTem, opeHighTem = -20.0, 55.0
            shortLow, shortHigh = -40.0, 70.0
            loss = 30.0
            groundSurLow, groundSurHigh = 55.0, 85.0
            altitude, feet = 25.0, 7.6
        elif category == 'B2':
            opeLowTem, opeHighTem = -20.0, 70.0
            shortLow, shortHigh = -45.0, 70.0
            loss = 40.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 25.0, 7.6
        elif category == 'B3':
            opeLowTem = -45.0
            altitude, feet = 25.0, 7.6
        elif category == 'B4':
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 25.0, 7.6
        # Category C1, C2, C3, C4
        elif category == 'C1':
            opeLowTem, opeHighTem = -20.0, 55.0
            shortLow, shortHigh = -40.0, 70.0
            loss = 30.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 35.0, 10.7
        elif category == 'C2':
            opeLowTem, opeHighTem = -55.0, 70.0
            shortLow, shortHigh = -55.0, 70.0
            loss = 40.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 35.0, 10.7
        elif category == 'C3':
            opeLowTem = -55.0
            altitude, feet = 35.0, 10.7
        elif category == 'C4':
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 35.0, 10.7
        # Category D1, D2, D3
        elif category == 'D1':
            opeLowTem, opeHighTem = -20.0, 55.0
            shortLow, shortHigh = -40.0, 70.0
            loss = 30.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 50.0, 15.2
        elif category == 'D2':
            opeLowTem, opeHighTem = -55.0, 70.0
            shortLow, shortHigh = -55.0, 70.0
            loss = 40.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 50.0, 15.2
        elif category == 'D3':
            opeLowTem = -55.0
            shortLow = -55.0
            groundSurLow = -55.0
            altitude, feet = 50.0, 15.2
        # Category E1, E2
        elif category == 'E1':
            opeLowTem = -55.0
            shortLow = -55.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 70.0, 21.3
        elif category == 'E2':
            opeLowTem = -55.0
            shortLow = -55.0
            groundSurLow = -55.0
            altitude, feet = 70.0, 21.3
        # Category F1, F2, F3
        elif category == 'F1':
            opeLowTem, opeHighTem = -20.0, 55.0
            shortLow, shortHigh = -40.0, 70.0
            loss = 30.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 55.0, 16.8
        elif category == 'F2':
            opeLowTem, opeHighTem = -55.0, 70.0
            shortLow, shortHigh = -55.0, 70.0
            loss = 40.0
            groundSurLow, groundSurHigh = -55.0, 85.0
            altitude, feet = 55.0, 16.8
        elif category == 'F3':
            opeLowTem = -55.0
            shortLow = -55.0
            groundSurLow= -55.0
            altitude, feet = 55.0, 16.8


        tempData = Temperature(opeLowTem, opeHighTem, shortLow, shortHigh, loss, 
                                    groundSurLow, groundSurHigh, altitude, feet,
                                    decompression, overpression, category)
        db.session.add(tempData)

        # commit in db
        db.session.commit()

        # check if the email has already existed in the db
        # it's a int 
        # if db.session.query(Data).filter(Data.height_== height).count() == 0:
        #     data = Data(height) #create a data object
        #     db.session.add(data)
        #     db.session.commit()
        #     return render_template("success.html")
        # print(db.session.query(FuelCell))
        return render_template("success.html")

@app.route('/successful', methods=['POST', 'GET'])
def output():
  return render_template('success.html')
    
if __name__ == '__main__':
    app.debug=True
    # app.run(debug=True, port=8080)
    app.run()
    