#import test


# goal:
# each subcomponent will have
        # indepdant parameters
        # equation definitions that describe constraints
        # note: optmization 

class fuel_tank:
    def __init__(self,tank_volume):
        self.max = tank_volume
        self.min = 0
        self.specific_energy = 0

    def specific_energy(self, tank_volume):
        # calculate specific energy from tank_volume
        specific_energy = self.specific_energy + 1 
        return specific_energy

    def __repr__(self):
        return "fuel_tank('{}')".format(self.tank_volume)

    def __str__(self):
        return "fuel tank volume: {}".format(self.tank_volume)   
class fuel_cell:
     def __init__(self):
         self.efficiency = 99
        #loss mechanisms - 50% 
        #voltage,current, compressed air  ~ 
class Pow_Dis_Unt:
    def __init__(self, AWG, material, FC_cable_length,PDU_cable_length,contactor_resistance):
        self.AWG = AWG
        self.material = material
        self.FC_cable_length = FC_cable_length
        self.PDU_cable_length = PDU_cable_length
        self.contactor_resistance = contactor_resistance
class inverter:
    def __init__(self,max_power,mass, volume,efficiency):
        self.max_power = max_power
        self.mass = mass
        self.volume = volume
        self.efficiency = efficiency
        self.num_of_inverters = 0

class motor:
    def __init__(self, max_power,max_torque,weight,volume,nominal_speed,worst_efficincy,num_phases):
        self.max_power = max_power
        self.max_torque = max_torque
        self.weight = weight
        self.volume = volume
        self.max_nominal_speed = nominal_speed
        self.worst_efficiency = worst_efficincy
        self.num_phases = num_phases
# conducionts loss 



# ***** TESTING BELOW

fuel_tank_1 = fuel_tank(4)
print(fuel_tank_1.specific_energy)

