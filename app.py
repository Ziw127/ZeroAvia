# import imp
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# make app know where to connect to the database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre123@localhost/ZeroAvia'
db = SQLAlchemy(app) # create a SQLAlchemy object for the Flask Application

class FuelTank(db.Model):
    __tablename__ = 'fueltank'
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float)
    speEnergy = db.Column(db.Float)
    enDensity = db.Column(db.Float)
    minFuelWeight = db.Column(db.Float)
    maxFuelWeight = db.Column(db.Float)
    tankEfficiency = db.Column(db.Float)


    def __init__(self, weight, volume, speEnergy, enDensity, minFuelWeigh,maxFuelWeight,tankEfficiency):
        self.weight = weight
        self.volume = volume
        self.speEnergy = speEnergy
        self.enDensity = enDensity
        self.minFuelWeight = minFuelWeigh
        self.maxFuelWeight = maxFuelWeight
        self.tankEfficiency = tankEfficiency

class FuelCell(db.Model):
    __tablename__ = 'fuelcell'
    id = db.Column(db.Integer, primary_key=True)
    PowerRating = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)
    ratedVoltage = db.Column(db.Float)
    heatLeakage = db.Column(db.Float)
    consumption = db.Column(db.Float)
    cellEfficiency = db.Column(db.Float)


    def __init__(self, PowerRating, weight, volume, ratedVoltage, heatLeakage,consumption,cellEfficiency):
        self.PowerRating = PowerRating
        self.weight = weight
        self.volume = volume
        self.ratedVoltage = ratedVoltage
        self.heatLeakage = heatLeakage
        self.consumption = consumption
        self.cellEfficiency =cellEfficiency

@app.route("/")
def index():
    return render_template("formTest.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        tweight = request.form["ft_w"]
        tvolume = request.form["ft_vol"]
        speEnergy = request.form["spec_e"]
        enDensity = request.form["e_density"]
        minFuelWeight = request.form["ft_min"]
        maxFuelWeight = request.form["ft_max"]
        tankEfficiency = request.form["ft_wce"]
        print(tweight, tvolume, speEnergy)
        print(enDensity, minFuelWeight, maxFuelWeight)
        print(tankEfficiency)
        fueltankData = FuelTank(tweight, tvolume, speEnergy,enDensity, minFuelWeight, maxFuelWeight,tankEfficiency)
        db.session.add(fueltankData)

        PowerRating = request.form["fc_pow"]
        cweight = request.form["fc_m"]
        cvolume = request.form["fc_vol"]
        ratedVoltage = request.form["fc_rvol"]
        heatLeakage = request.form["fc_enth"]
        consumption = request.form["fc_cons"]
        cellEfficiency = request.form["fc_wce"]
        fuelcellData = FuelCell(PowerRating,cweight, cvolume, ratedVoltage,heatLeakage, consumption, cellEfficiency)
        db.session.add(fuelcellData)
        db.session.commit()
        # check if the email has already existed in the db
        # it's a int 
        # if db.session.query(Data).filter(Data.height_== height).count() == 0:
        #     data = Data(height) #create a data object
        #     db.session.add(data)
        #     db.session.commit()
        #     return render_template("success.html")
    
        return render_template("success.html")
    
if __name__ == '__main__':
    app.debug=True
    # app.run(debug=True, port=8080)
    app.run()
    