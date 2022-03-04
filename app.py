# import imp
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


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

class FuelCell(db.Model):
    __tablename__ = 'fuelcell'
    id = db.Column(db.Integer, primary_key=True)
    powerrating = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)
    ratedvoltage = db.Column(db.Float)
    heatleakage = db.Column(db.Float)
    consumption = db.Column(db.Float)
    efficiency = db.Column(db.Float)


    def __init__(self, PowerRating, weight, volume, ratedVoltage, heatLeakage,consumption,cellEfficiency):
        self.powerrating = PowerRating
        self.weight = weight
        self.volume = volume
        self.ratedvoltage = ratedVoltage
        self.heatleakage = heatLeakage
        self.consumption = consumption
        self.efficiency =cellEfficiency

class PowerDistro(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    hvds = db.Column(db.Float, nullable=False)
    minrating = db.Column(db.Float)
    conductor = db.Column(db.Float)
    pdu = db.Column(db.Float)
    eps = db.Column(db.Float)
    resistance = db.Column(db.Float)
    efficiency = db.Column(db.Float)


    def __init__(self, HVDC, minInRating, conductor, fuelcellToPDU, PDUtoEPS,conResistance,powerEfficiency):
        self.hvds = HVDC
        self.minrating = minInRating
        self.conductor = conductor
        self.pdu = fuelcellToPDU
        self.eps = PDUtoEPS
        self.resistance = conResistance
        self.efficiency = powerEfficiency

class Inverter(db.Model):
    __tablename__ = 'inverter'
    id = db.Column(db.Integer, primary_key=True)
    maxpower = db.Column(db.Float, nullable=False)
    maxhvdc = db.Column(db.Float)
    minhvdc = db.Column(db.Float)
    maxcoolinlet = db.Column(db.Float)
    mincoolinlet = db.Column(db.Float)
    maxcur = db.Column(db.Float)
    mass = db.Column(db.Float)
    volume = db.Column(db.Float)
    swfreqency = db.Column(db.Float)
    efficiency = db.Column(db.Float)


    def __init__(self, maxPower, maxHVDC, minHVDC, maxcoolInlet, mincoolInlet,maxHDVCcur,mass,volume,swfreqency,invEfficiency):
        self.maxpower =maxPower
        self.maxhvdc = maxHVDC
        self.minhvdc = minHVDC
        self.maxcoolinlet = maxcoolInlet
        self.mincoolinlet = mincoolInlet
        self.maxcur = maxHDVCcur
        self.mass = mass
        self.volume = volume
        self.swfreqency = swfreqency
        self.efficiency = invEfficiency

class Motor(db.Model):
    __tablename__ = 'motor'
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    maxpower = db.Column(db.Float)
    maxspeed = db.Column(db.Float)
    maxtorque = db.Column(db.Float)
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)
    nophases = db.Column(db.Integer)
    maxphase = db.Column(db.Float)
    funfreqency = db.Column(db.Float)
    efficiency = db.Column(db.Float)


    def __init__(self, numMotors, maxPower, maxSpeed, maxTorque, weight,volume,noPhases,maxPhaseCurrent,funfreqency,motorEfficiency):
        self.num = numMotors
        self.maxpower = maxPower
        self.maxspeed = maxSpeed
        self.maxtorque = maxTorque
        self.weight = weight
        self.volume = volume
        self.noPhases = noPhases
        self.maxphase = maxPhaseCurrent
        self.funfreqency = funfreqency
        self.efficiency = motorEfficiency

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

        # FuelCell
        PowerRating = request.form["fc_pow"]
        cweight = request.form["fc_m"]
        cvolume = request.form["fc_vol"]
        ratedVoltage = request.form["fc_rvol"]
        heatLeakage = request.form["fc_enth"]
        consumption = request.form["fc_cons"]
        cellEfficiency = request.form["fc_wce"]
        fuelcellData = FuelCell(PowerRating,cweight, cvolume, ratedVoltage,
                                heatLeakage, consumption, cellEfficiency)
        db.session.add(fuelcellData)

        # Power Distro
        HVDC = request.form["hvdc_diam"]
        minInRating = request.form["pd_minvolt"]
        conductor = request.form["pd_cable"]
        fuelcellToPDU = request.form["pd_from_fc"]
        PDUtoEPS = request.form["pd_to_eps"]
        conResistance = request.form["pd_contres"]
        powerEfficiency = request.form["pd_wce"]
        powerdata = PowerDistro(HVDC,minInRating,conductor,fuelcellToPDU,
                                PDUtoEPS,conResistance,powerEfficiency)
        db.session.add(powerdata)
        
        # Inverter
        inv_maxPower = request.form["inve_pow"]
        maxHVDC = request.form["inve_hvdc_max"]
        minHVDC = request.form["inve_hvdc_min"]
        maxcoolInlet = request.form["inve_cool_max"]
        mincoolInlet = request.form["inve_cool_min"]
        maxHDVCcur = request.form["inve_max_cur"]
        mass = request.form["inve_m"]
        involume = request.form["inve_vol"]
        swfreqency = request.form["inve_f"]
        invEfficiency = request.form["inve_wce"]
        inverterdata = Inverter(inv_maxPower,maxHVDC,minHVDC,maxcoolInlet,mincoolInlet,
                                maxHDVCcur,mass,involume,swfreqency,invEfficiency)
        db.session.add(inverterdata)
       

        # Motor
        numMotors = request.form["mo_n"]
        motor_maxPower = request.form["mo_pow"]
        maxSpeed = request.form["mo_sp"]
        maxTorque = request.form["mo_tor"]
        mweight = request.form["mo_m"]
        mvolume = request.form["mo_vol"]
        noPhases = request.form["mo_phases"]
        maxPhaseCurrent = request.form["mo_cur"]
        funfreqency = request.form["mo_f"]
        motorEfficiency = request.form["mo_wce"]
        motordata = Motor(numMotors, motor_maxPower,maxSpeed,maxTorque,mweight,mvolume,
                                noPhases,maxPhaseCurrent,funfreqency,motorEfficiency)
        db.session.add(motordata)

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
    