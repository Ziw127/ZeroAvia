from mission_profile_class import *


# Each object in routes is a full description of a mission profile (route)
#this varaible should be fairly dynamic, it is static for testings
routes =["mpr_001","mpr_002","mpr_003"]
phase_time = [15/60,10/60,5/60,20/60,60/60,10/60,10/60,10/60]
phase_pwr_ratios = [0.5,0.15,1.00,.80,.50,.20,.80,.15] 
max_power = 600
# phase_pwr_total = [(x/100)*max_pwr for x in phase_pwr_per]
#print('below phase power ratio')
#print(phase_pwr_ratio)

#mission profile components - will not change - mission profile + 8 phases
mp_components = ["mission_profile",
                    "startup_phase",
                    "taxi_phase",
                    "take_off_phase",
                    "climb_phase",
                    "cruise_phase",
                    "descent_phase",
                    "go_around_phase",
                    "land_phase"]

#for multiple routes we need to link a unique name idenifitier to each mission profile phase
# opting for "route name" + "_" + " current_phase" - such as - "route_name_current_phase"
#This creates a list that specific mission profile route can be idenifitied by
def link_routeid_mpcomponents(route_id,mp_components,linked_rid_mpc = None):
    linked_rid_mpc = []
    for i in range(len(mp_components)):
        var_to_add = route_id + "_" + mp_components[i]
        linked_rid_mpc.append(var_to_add)
    return linked_rid_mpc 

# INPUT: LIST that includes mission profile + phases
# OUTPUTS: All classes assocaited with the 'current' mission profile + phases
def init_the_route(linked_routeid_mpcomponents,phase_time,phase_pwr_ratio,max_power):
    
    linked_routeid_mpcomponents[0] = mission_profile(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[1] = mission_profile.startup_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[2] = mission_profile.taxi_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[3] = mission_profile.take_off_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[4] = mission_profile.climb_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[5] = mission_profile.cruise_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[6] = mission_profile.descent_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[7] = mission_profile.go_around_phase(phase_time,phase_pwr_ratio,max_power)
    linked_routeid_mpcomponents[8] = mission_profile.land_phase(phase_time,phase_pwr_ratio,max_power)
    return linked_routeid_mpcomponents[0], linked_routeid_mpcomponents[1], linked_routeid_mpcomponents[2], linked_routeid_mpcomponents[3], linked_routeid_mpcomponents[4], linked_routeid_mpcomponents[5], linked_routeid_mpcomponents[6], linked_routeid_mpcomponents[7], linked_routeid_mpcomponents[8]

rtest = link_routeid_mpcomponents(routes[0],mp_components,max_power)
# print(rtest)
# sets phase specific 'phase_power_requires' per phase and calculates total (summation)
def set_phase_pwr():
    mp_pwr_total = []

    current_startup_phase.phase_powertime()
    #print("current_startup_phase.phase_powertime() 1 ")
    #print(current_startup_phase.phase_powertime())
    mp_pwr_total.append(current_startup_phase.phase_pwr_rqr)

    current_taxi_phase.phase_powertime()
    mp_pwr_total.append(current_taxi_phase.phase_pwr_rqr)

    current_take_off_phase.phase_powertime()
    mp_pwr_total.append(current_take_off_phase.phase_pwr_rqr)

    current_climb_phase.phase_powertime()
    mp_pwr_total.append(current_climb_phase.phase_pwr_rqr)

    current_cruise_phase.phase_powertime()
    mp_pwr_total.append(current_cruise_phase.phase_pwr_rqr)

    current_descent_phase.phase_powertime()
    mp_pwr_total.append(current_descent_phase.phase_pwr_rqr)

    current_go_around_phase.phase_powertime()
    mp_pwr_total.append(current_go_around_phase.phase_pwr_rqr)

    current_land_phase.phase_powertime()
    mp_pwr_total.append(current_land_phase.phase_pwr_rqr)

    current_mission_profile.calc_total_power_reqr(mp_pwr_total)

    return

current_mission_profile, current_startup_phase, current_taxi_phase, current_take_off_phase, current_climb_phase, current_cruise_phase, current_descent_phase, current_go_around_phase, current_land_phase = init_the_route(rtest,phase_time,phase_pwr_ratios,max_power)
set_phase_pwr()


print(f'total power requred: {int(current_mission_profile.total_power_reqr)} kWh ')
print(f'If fuel has a specific energy of 39.4 kWh/kg: {int(current_mission_profile.total_power_reqr)/39.4} kg needed')
print(f'If fuel has a specific energy density of  of 1.479 kWh/L: {int(current_mission_profile.total_power_reqr)/1.479} L needed')





