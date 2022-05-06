# 4.5 Temperature Tests
from re import S
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('tester program running')

#table_4_1 = pd.read_csv('table_4_1_Pressure_Values_for_Various_Pressure_Alt-Sheet1.csv', index_col=0)
table_4_1 = pd.read_csv('table_4_1_temp_and_alt_criteria-Sheet1.csv', index_col=0)
# print(table_4_1['A1'])


class temperature_tests:
    def __init__(self, equipment_category):
        #each value below pulls from table_4_1 based on the equipment category
        self.equipment_category = equipment_category
        self.operating_low_temp = table_4_1.at['operating_low_temp', self.equipment_category]
        self.operating_high_temp = table_4_1.at['operating_high_temp', equipment_category]
        self.short_time_operating_low_temp = table_4_1.at['short_time_operating_low_temp', equipment_category]
        self.short_time_operating_high_temp = table_4_1.at['short_time_operating_high_temp', equipment_category]
        self.ground_survival_low_temp = table_4_1.at['ground_survival_low_temp', equipment_category]
        self.ground_survival_high_temp = table_4_1.at['ground_survival_high_temp', equipment_category]
        self.loss_of_cooling_test = table_4_1.at['loss_of_cooling_test', equipment_category]
        self.altitude_thousands_of_meters = table_4_1.at['altitude_thousands_of_meters', equipment_category]
        self.altitude_thousands_of_feet = table_4_1.at['altitude_thousands_of_feet', equipment_category]
        self.decompression_test = table_4_1.at['decompression_test', equipment_category]
        self.overpressure_test = table_4_1.at['overpressure_test', equipment_category]

        #parameter_dict is important for updating "notes" that are in the database instead of values
        self.parameter_dict = {'operating_low_temp' : self.operating_low_temp,
                        'operating_high_temp' :self.operating_high_temp,
                        'short_time_operating_low_temp': self.short_time_operating_low_temp,
                        'short_time_operating_high_temp':self.short_time_operating_high_temp,
                        'ground_survival_low_temp': self.ground_survival_low_temp,
                        'ground_survival_high_temp':self.ground_survival_high_temp,
                        'loss_of_cooling_test' : self.loss_of_cooling_test,
                        'altitude_thousands_of_meters':self.altitude_thousands_of_meters,
                        'altitude_thousands_of_feet':self.altitude_thousands_of_feet,
                        'decompression_test': self.decompression_test,
                        'overpressure_test': self.overpressure_test}

        #manually enter values based on Notes in tables
        self.check_for_notes()

        #Test specific time varables, will change depending on test preformed
        """
        self.figure_4_1_key_value_pairs = {self.T0 : None, T1: None, T2: None, T3: None, T4:None, T5: None}
        self.T0 #Time0 var
        self.T1 #Time1 var
        self.T2 #Time2 var
        self.T3 #Time3 var
        self.T4 #Time4 var
        self.T5 #Time5 var
        self.roc_T0T1 #rate of change between Time0 and Time1
        self.roc_T1T2 #rate of change between Time1 and Time2
        self.roc_T2T3 #rate of change between Time2 and Time3
        self.roc_T3T4 #rate of change between Time3 and Time4
        self.roc_T4T5 #rate of change between Time4 and Time5
        """

    def check_for_notes(self,*args, input = ''): #pass in the necessary variables
        list = []
        for key in args:
            if "Note" in str(self.parameter_dict[key]):
                # #print({key}, "->", {self.parameter_dict[key]})
                # #self.parameter_dict[key] =
                # val = input(f"For Category: {key} and equipment_category {self.equipment_category}. Values are supplied by the manufacturer. Please enter an manufacuturer's value for: {key} now: ")
                # #print({key}, "->", {self.parameter_dict[key]})
                # list.append(val)
                list.append(str(input))
                print(list)
            else:
                val = self.parameter_dict[key]
                list.append(val)
        return list

# tester = temperature_tests("A4", 'short_time_operating_low_temp')
tester = temperature_tests("A4")

############################################################################################################
############################################################################################################
############################################################################################################
# Baseline Requirements
# The goal for baseline requirements is to have a set of (X,Y) values that will aid in
# the plotting of the test.  Values that are ambigious will default to minimum viable requirements.

    #Ground Survival Low Temperature and Short Time Operating Low Temp Test
def figure_4_1_test_baseline_requirements(stab_time = 30*60,int_stab_time=2100, category = "", input1 = '', input2 = ''):
    print('called')
    note1 =temperature_tests(category).check_for_notes('short_time_operating_low_temp', input=input1)
    note2 =temperature_tests(category).check_for_notes('ground_survival_low_temp', input=input2)
    dT0,temp0,op0 = 0,22,0
    dT1,temp1,op1 = 30*60, float(note2[0]), 0
    dT2,temp2,op2 = stab_time + 3*3600,float(note2[0]), 0
    dT3,temp3,op3 = 60*(float(note1[0]) - float(note2[0]))/2.,float(note1[0]), 0
    dT4,temp4,op4 = int_stab_time,float(note1[0]), 0
    dT5,temp5,op5 = 3600, float(note1[0]), 1
    dt = [dT0,dT1,dT2,dT3,dT4,dT5]
    temps = [temp0,temp1,temp2,temp3,temp4,temp5]
    f = plt.figure()
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Ground Survival Low Temperature And Short Time Operating Low Temp Test Requirements')
    plt.savefig('groundandoperatinglow.jpg')
    plt.close()
    pass

    #Operating Low Temperature Test
def figure_4_2_test_baseline_requirements(stab_time = 30*60,  category = "", input =''):
    note = temperature_tests(category).check_for_notes('operating_low_temp', input=input)
    dT0,temp0,op0 = 0,22, 1
    dT1,temp1,op1 = 30*60, float(note[0]), 1
    dT2,temp2,op2 = stab_time, float(note[0]), 1
    dT3,temp3,op3 = 7200,float(note[0]), 1
    dt = [dT0,dT1,dT2,dT3]
    temps = [temp0,temp1,temp2,temp3]
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Operating Low Temp Test Requirements')
    plt.savefig('operatinglow.jpg')
    plt.close()
    pass

    #Ground Survival High Temperature and Short Time Operating High Temp Test
def figure_4_3_test_baseline_requirements(stab_time = 30*60,int_stab_time=2100, category = "", input1 = '', input2 = ''):
    note1 = temperature_tests(category).check_for_notes('short_time_operating_high_temp', input=input1)
    note2 = temperature_tests(category).check_for_notes('ground_survival_high_temp', input=input2)
    dT0,temp0,op0 = 0,22,0
    dT1,temp1,op1 = 30*60, float(note2[0]), 0
    dT2,temp2,op2 = stab_time + 3*3600,float(note2[0]), 0
    dT3,temp3,op3 = (float(note1[0]) - float(note2[0]))/2.,float(note1[0]), 0
    dT4,temp4,op4 = int_stab_time,float(note1[0]), 0
    dT5,temp5,op5 = 1800, float(note1[0]), 1
    dt = [dT0,dT1,dT2,dT3,dT4,dT5]
    temps = [temp0,temp1,temp2,temp3,temp4,temp5]
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Ground Survival High Temperature and Short Time Operating High Temp Test')
    plt.savefig('groundandoperatinghigh.jpg')
    plt.close()
    pass

     #Operating High Temperature Test
def figure_4_4_test_baseline_requirements(stab_time = 30*60, category="", input =''):
    note = temperature_tests(category).check_for_notes('operating_high_temp', input=input)
    dT0,temp0,op0 = 0,22, 1
    dT1,temp1,op1 = 30*60, float(note[0]), 1
    dT2,temp2,op2 = stab_time, float(note[0]), 1
    dT3,temp3,op3 = 7200,float(note[0]), 1
    dt = [dT0,dT1,dT2,dT3]
    temps = [temp0,temp1,temp2,temp3]
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Operating High Temperature')
    plt.savefig('operatinghigh.jpg')
    plt.close()
    pass

    #In-Flight Loss of Cooling Test
def figure_4_5_test_baseline_requirements(cooling_category = '', stab_time = 30*60,  category = "", input =''):
    #WE MUST TAKE AN INPUT HERE FOR THE LOSS OF COOLING CATEGORY
    # Category V - 30 minutes minimum
    # Category W - 90 minutes minimum
    # Category P - 180 minutes minimum
    # Category Y - 300 minutes minimum
    # Category Z - As defined in the equipment specification
    # if cooling_category == '':
    #     cooling_category = input("Select cooling category of V,W,P,Y,or Z now: ")
    cats = ['V','W','P','Y','Z']
    durations = [ 30*60, 90*60,180*60,300*60,0]
    print(cooling_category)
    idx = cats.index(cooling_category)
    category_time = durations[idx]
    note = temperature_tests(category).check_for_notes('loss_of_cooling_test', input=input)
    dT0,temp0,op0 = 0,22, 1
    dT1,temp1,op1 = 30*60, float(note[0]), 1
    dT2,temp2,op2 = stab_time, float(note[0]), 1
    dT3,temp3,op3 = category_time,float(note[0]), 1
    dt = [dT0,dT1,dT2,dT3]
    temps = [temp0,temp1,temp2,temp3]
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (C)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('In-flight loss of cooling Test')
    plt.savefig('LoC.jpg')
    plt.close()
    pass

    #Altitude Test
def figure_4_6_test_baseline_requirements(stab_time = 30*60,  category = "", input =''):
    tester.altitude_thousands_of_meters = tester.check_for_notes('altitude_thousands_of_meters', input=input)
    alts = [-4572,-457,0,2438,4572,7620,10668,15240,16764,21336] #in meters
    pressures = [169.73,106.94,101.32,75.2,57.18,37.6,23.84,11.6,9.12,4.44] # in KPa
    print(tester.altitude_thousands_of_meters)
    idx = alts.index(tester.altitude_thousands_of_meters)
    print(idx)
    target_pressure = pressures[idx]
    dT0,p0,op0 = 0,101.32, 1
    dT1,p1,op1 = 30*60, target_pressure, 1
    dT2,p2,op2 = stab_time ,target_pressure, 1
    dT3,p3,op3 = 7200,target_pressure, 1
    dt = [dT0,dT1,dT2,dT3]
    temps = [p0,p1,p2,p3]
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (kPa)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Altitude Test')
    plt.savefig('Alt.jpg')
    plt.close()
    pass

    #Decompression Test
def figure_4_7_test_baseline_requirements(stab_time = 30*60,  category = "", input =''):
    note = temperature_tests(category).check_for_notes('decompression_test', input=input)
    dT0,p0,op0 = 0,101.32, 1
    dT1,p1,op1 = 10*60, 75.26, 1
    dT2,p2,op2 = stab_time, 75.26, 1
    dT3,p3,op3 = 15,float(note[0]), 1
    dT4,p4,op3 = 600,float(note[0]), 1
    dt = [dT0,dT1,dT2,dT3,dT4]
    temps = [p0,p1,p2,p3,p4]
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (kPa)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Decompression Test')
    plt.savefig('decomp.jpg')
    plt.close()
    pass

    #Overpressure Test
def figure_4_8_test_baseline_requirements(category = "", input =''):
    note = temperature_tests(category).check_for_notes('overpressure_test', input=input)
    dT0,p0,op0 = 0,101.32, 1
    dT1,p1,op1 = 10*60, 170, 1
    dT2,p2,op2 = 600, 170, 1
    dT3,p3,op3 = 10*60,float(note[0]), 1
    dT4,p4,op3 = 10*60,float(note[0]), 1
    dt = [dT0,dT1,dT2,dT3,dT4]
    temps = [p0,p1,p2,p3,p4]
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure (kPa)')
    plt.plot(np.cumsum(dt),temps)
    plt.title('Overpressure Test')
    plt.savefig('overpressure.jpg')
    plt.close()
    pass


############################################################################################################
############################################################################################################
############################################################################################################
    #VALIDATION BELOW
    #Validation occurs after data input. These functions will go through, idenifity key time points and validate the code against requirements.
    #Ground Survival Low Temperature and Short Time Operating Low Temp Test
    def figure_4_1_test_validation():
        pass

    #Operating Low Temperature Test
    def figure_4_2_test_validation():
        pass

    #Ground Survival High Temperature and Short Time Operating Low Temp Test
    def figure_4_3_test_validation():
        pass

     #Operating High Temperature Test
    def figure_4_4_test_validation():
        pass

    #In-Flight Loss of Cooling Test
    def figure_4_5_test_validation():
        pass

    #Altitude Test
    def figure_4_6_test_validation():
        pass

    #Decompression Test
    def figure_4_7_test_validation():
        pass

    #Overpressure Test
    def figure_4_8_test_validation():
        pass

############################################################################################################

# m = figure_4_1_test_baseline_requirements()

"""
out = figure_4_1_baseline_requirements
print(type(tester.short_time_operating_low_temp))
stab_time = 30*60
int_stab_time=2100
tester.check_for_notes('short_time_operating_low_temp','ground_survival_low_temp')
dT0,temp0,op0 = 0,22,0
dT1,temp1,op1 = 30*60, float(tester.ground_survival_low_temp), 0
dT2,temp2,op2 = float(stab_time) + 3*3600,float(tester.ground_survival_low_temp), 0
dT3,temp3,op3 = (float(tester.short_time_operating_low_temp) - float(tester.ground_survival_low_temp))/2.,float(tester.short_time_operating_low_temp), 0
dT4,temp4,op4 = float(int_stab_time),float(tester.short_time_operating_low_temp), 0
dT5,temp5,op5 = 1800, float(tester.short_time_operating_low_temp), 1
dt = [dT0,dT1,dT2,dT3,dT4,dT5]
temps = [temp0,temp1,temp2,temp3,temp4,temp5]
plt.plot(np.cumsum(dt),temps)
plt.savefig('test.jpg')
"""