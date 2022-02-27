class mp_phase: #mission profile phase each phase will have these same variabless
    def __init__(self,phase_time, phase_pwr_ratios,max_power):
        self.phase_pwr_ratio = 0. 
        self.duration = None 
        self.altitude_start = None
        self.altitude_end = None
        self.coolant_upper = None
        self.coolant_lower = None
        self.phase_duration = 0.
        self.duration_min = None
        self.duration_max = None
        self.phase_number = int
        self.max_power = max_power
        self.phase_pwr_rqr = 0.
        self.phase_energy_rqr = 0.

    def phase_powertime(self):
        #print("PHASE POWER LOCATION")
        #print(self)
        #print(self.phase_duration)
        #print(self.phase_pwr_ratio)
        self.phase_pwr_rqr = self.phase_duration * self.max_power * self.phase_pwr_ratio * (1./(.98))
        #print(self.phase_pwr_rqr)
        return self.phase_pwr_rqr

    def phase_energy(self):
        phase_energy_rqr = self.phase_duration * self.phase_pwr_ratio * self.max_power * (1./0.98)
        return phase_energy_rqr

class mission_profile():
    def __init__(self,phase_time,phase_pwr_ratios,max_power):
        self.total_power_reqr = float

    def calc_total_power_reqr(self,mp_pwr_total):
        self.total_power_reqr = 0
        self.total_power_reqr = sum(mp_pwr_total)
        return self.total_power_reqr
        
    class startup_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios,max_power):
            super().__init__(phase_time,phase_pwr_ratios, max_power)
            self.phase_number = 0
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
    class taxi_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 1
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
    class take_off_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 2
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]            
    class climb_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 3
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
    class cruise_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 4
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
    class descent_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 5
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
    class go_around_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 6
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
    class land_phase(mp_phase):
        def __init__(self,phase_time,phase_pwr_ratios, max_power ):
            super().__init__(phase_time,phase_pwr_ratios, max_power )
            self.phase_number = 7
            self.init_values(phase_time, phase_pwr_ratios)

        def init_values(self,phase_time, phase_pwr_ratios):
            #print('phase number')
            #print(self)
            #print(self.phase_number)
            self.phase_duration = phase_time[self.phase_number]
            self.phase_pwr_ratio = phase_pwr_ratios[self.phase_number]
