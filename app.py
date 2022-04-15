# import Flask class and create an instance for this class
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# define the name of the application's module - app
app = Flask(__name__)
# make app know where to connect to the database
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgre123@localhost/ZeroAvia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # create a SQLAlchemy object for the Flask Application


class FuelTank(db.Model):
    __tablename__ = 'fueltank'
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float)
    energy = db.Column(db.Float)
    density = db.Column(db.Float)
    minfuelweight = db.Column(db.Float)
    maxfuelweight = db.Column(db.Float)
    efficiency = db.Column(db.Float)


    def __init__(self, weight, volume, speEnergy, enDensity, minFuelWeigh,maxFuelWeight,tankEfficiency):
        self.weight = weight
        self.volume = volume
        self.energy = speEnergy
        self.density = enDensity
        self.minfuelweight = minFuelWeigh
        self.maxfuelweight = maxFuelWeight
        self.efficiency = tankEfficiency




@app.route("/")
def index():
    return render_template("formTest.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        # FuelTank
        tweight = request.form["ft_m"]
        tvolume = request.form["ft_vol"]
        speEnergy = request.form["spec_e"]
        enDensity = request.form["e_density"]
        minFuelWeight = request.form["ft_min"]
        maxFuelWeight = request.form["ft_max"]
        tankEfficiency = request.form["ft_wce"]
        print(tweight, tvolume, speEnergy)
        print(enDensity, minFuelWeight, maxFuelWeight)
        print(tankEfficiency)
        fueltankData = FuelTank(tweight, tvolume, speEnergy,enDensity, 
                                minFuelWeight, maxFuelWeight,tankEfficiency)
        db.session.add(fueltankData)

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
    
if __name__ == '__main__':
    app.debug=True
    # app.run(debug=True, port=8080)
    app.run()
    