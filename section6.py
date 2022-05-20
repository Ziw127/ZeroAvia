# Testing for section 6 Humidity
# Info:
# 3 specific categories (A,B,C)
# Three types of humidity tests
import matplotlib.pyplot as plt


class humidity_test():
    def __init__(self, equipment_category_input):
        self.equipment_category = equipment_category_input  # A,C or C
        # self.rate_of_change  # = get from table  or function (need to create)
        self.relative_humidity_sp1 = int  # set via cat. selection *** sp1 - set point 1
        self.relative_humidity_sp2 = int  # set via cat. selection **** sp2 - set point 2
        self.temp_sp1 = int  # tempature at which to stablizate
        self.temp_sp2 = int  #
        self.title_for_plot = str
        self.num_of_cyles = int
        # title_for_plot
        # Category A = Standard Humidity Enviorment
        # Category B = Severe Humidity Enviroment
        # Category C = External Humidity Enviroment

    def set_category_variables(self):
        if self.equipment_category == "A":
            self.relative_humidity_sp1 = 85  # +/-4
            self.relative_humidity_sp2 = 95  # +/-4
            self.temp_sp1 = 38  # +/- 2
            self.temp_sp2 = 50  # +/- 2
            self.title_for_plot = "Standard Humidity Enviorment"
            self.num_of_cyles = 2  # 48 hours

        elif self.equipment_category == "B":
            self.relative_humidity_sp1 = 85  # +/-4
            self.relative_humidity_sp2 = 95  # +/-4
            self.temp_sp1 = 38  # +/- 2
            self.temp_sp2 = 65  # +/- 2
            self.title_for_plot = "Severe Humidity Enviroment"
            self.num_of_cyles = 10  # 240 hours

        elif self.equipment_category == "C":
            self.relative_humidity_sp1 = 85  # +/-4
            self.relative_humidity_sp2 = 95  # +/-4
            self.temp_sp1 = 38  # +/- 2
            self.temp_sp2 = 55  # +/- 2
            self.title_for_plot = "External Humidity Enviroment"
            self.num_of_cyles = 6  # 144 hours

    def plot_equipment_category(self):

        f = plt.figure()
        plt.xlabel('Time (hours)')
        plt.ylabel('Temperature and Humidity')
        temp_time = [0, 2, 8, 24]
        temperature_levels = [self.temp_sp1,
                              self.temp_sp2, self.temp_sp2, self.temp_sp1]
        humidity_time = [0, 2, 8, 24]
        humidity_levels = [self.relative_humidity_sp1, self.relative_humidity_sp2,
                           self.relative_humidity_sp2, self.relative_humidity_sp1]
        plt.plot(temp_time, temperature_levels, label="Temperature")
        plt.plot(humidity_time, humidity_levels, label="Humidity")

        plt.legend()
        plt.title(self.title_for_plot)
        plt.savefig('humidity_testa.jpg')


humidity_test_active = humidity_test("A")
# this needs to change to accomindate different inputs A,B or C.
humidity_test_active.set_category_variables()
humidity_test_active.plot_equipment_category()
