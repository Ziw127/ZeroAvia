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
        self.specific_energy = 39.4 #kWhr/kg
        self.energy_density = 1.479 #kWhr/L

    def get_specific_energy(self, specific_energy):
        # return specific energy of tank volume
        # base value is in kWhr/kg
        return specific_energy
    
    def fuel_vol_needed(self, en_needed):
        # calculate fuel volume needed as a function of the energy needed and energy density
        # takes en_needed in kWhr
        # energy density is in kWhr/L
        # returns fuel mass in liters
        return en_needed/self.energy_density

    def fuel_mass_needed (self, en_needed):
        # calculate fuel mass needed as a function of the energy needed (mission phase or overall) and the specific energy. 
        # takes needed in kWhr
        # specific energy is in kWhr/kg 
        # returns fuel mass in kg
        return en_needed/self.specific_energy 

    def __repr__(self):
        return "fuel_tank('{}')".format(self.max)

    def __str__(self):
        return "fuel tank volume: {}".format(self.max)   
class fuel_cell:
     def __init__(self):
         self.efficiency = 99
        #loss mechanisms - 50% 
        #voltage,current, compressed air  ~ 
     def get_losses(self,phase_info):
        losses = []
        for x in range(len(phase_info)):
          losses.append(phase_info[x]*(1-self.efficiency))
        return losses
class Pow_Dis_Unt:
    def __init__(self, AWG, material, FC_cable_length,PDU_cable_length,contactor_resistance, efficiency):
        self.AWG = AWG
        self.material = material
        self.FC_cable_length = FC_cable_length
        self.PDU_cable_length = PDU_cable_length
        self.contactor_resistance = contactor_resistance
        self.efficiency = efficiency
    def get_losses(self,phase_info):
        losses = []
        for x in range(len(phase_info)):
          losses.append(phase_info[x]*(1-self.efficiency))
        return losses
class inverter:
    def __init__(self,max_power,mass, volume,efficiency):
        self.max_power = max_power
        self.mass = mass
        self.volume = volume
        self.efficiency = efficiency
        self.num_of_inverters = 0
    def get_losses(self,phase_info):
        losses = []
        for x in range(len(phase_info)):
          losses.append(phase_info[x]*(1-self.efficiency))
        return losses

class motor:
    def __init__(self, max_power,max_torque,weight,volume,nominal_speed,efficiency,num_phases):
        self.max_power = max_power
        self.max_torque = max_torque
        self.weight = weight
        self.volume = volume
        self.max_nominal_speed = nominal_speed
        self.efficiency = efficiency
        self.num_phases = num_phases
    def get_losses(self,phase_info):
        losses = []
        for x in range(len(phase_info)):
          losses.append(phase_info[x]*(1-self.efficiency))
        return losses
# conducionts loss 



# ***** TESTING BELOW

fuel_tank_1 = fuel_tank(4)
print(fuel_tank_1.specific_energy)

