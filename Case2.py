import matplotlib.pyplot as plt
import numpy as np
from juzzyPython.generalType2zSlices.sets.GenT2MF_Trapezoidal import GenT2MF_Trapezoidal
from juzzyPython.generalType2zSlices.system.GenT2_Antecedent import GenT2_Antecedent
from juzzyPython.generalType2zSlices.system.GenT2_Consequent import GenT2_Consequent
from juzzyPython.generalType2zSlices.system.GenT2_Rule import GenT2_Rule
from juzzyPython.generalType2zSlices.system.GenT2_Rulebase import GenT2_Rulebase
from juzzyPython.generic.Input import Input
from juzzyPython.generic.Output import Output
from juzzyPython.generic.Plot import Plot
from juzzyPython.generic.Tuple import Tuple
from juzzyPython.intervalType2.sets.IntervalT2MF_Trapezoidal import IntervalT2MF_Trapezoidal
from juzzyPython.type1.sets.T1MF_Trapezoidal import T1MF_Trapezoidal
from scipy.integrate import tplquad


class Case2:
    def __init__(self, unit=False) -> None:
        self.numberOfzLevels = 4

        # Inputs to the FLS
        self.temperature = Input("temperature", Tuple(23.99, 44.01))
        self.headache = Input("headache", Tuple(0, 10.01))
        self.age = Input("age", Tuple(0, 130.01))
        # Output
        self.urgency = Output(("urgency"), Tuple(0, 100))

        self.plot = Plot()

        # Temperature
        self.ColdUMF = T1MF_Trapezoidal("Upper MF for coldly temperature", [24.0, 24.0, 35.001, 36.4])
        self.ColdLMF = T1MF_Trapezoidal("Lower MF for coldly temperature", [24.0, 24.0, 35.0, 36.4])
        self.ColdIT2MF = IntervalT2MF_Trapezoidal("IT2MF for coldly temperature", self.ColdUMF, self.ColdLMF)
        self.ColdMF = GenT2MF_Trapezoidal("GT2MF for coldly temperature", primer=self.ColdIT2MF,
                                          numberOfzLevels=self.numberOfzLevels)

        self.NormalUMF = T1MF_Trapezoidal("Upper MF for normal temperature", [35.0, 36.4, 36.9, 38.0])
        self.NormalLMF = T1MF_Trapezoidal("Lower MF for normal temperature", [35.001, 36.4, 36.9, 38.0])
        self.NormalIT2MF = IntervalT2MF_Trapezoidal("IT2MF for normal temperature", self.NormalUMF, self.NormalLMF)
        self.NormalMF = GenT2MF_Trapezoidal("GT2MF for normal temperature", primer=self.NormalIT2MF,
                                            numberOfzLevels=self.numberOfzLevels)

        self.HotUMF = T1MF_Trapezoidal("Upper MF for hot temperature", [36.6, 38.0, 44.0, 44.0])
        self.HotLMF = T1MF_Trapezoidal("Lower MF for hot temperature", [36.601, 38.0, 44.0, 44.0])
        self.HotIT2MF = IntervalT2MF_Trapezoidal("IT2MF for hot temperature", self.HotUMF, self.HotLMF)
        self.HotMF = GenT2MF_Trapezoidal("GT2MF for hot temperature", primer=self.HotIT2MF,
                                         numberOfzLevels=self.numberOfzLevels)

        # Headache
        self.MildUMF = T1MF_Trapezoidal("Upper MF for mild headache", [0.0, 0.0, 3.0, 5.0])
        self.MildLMF = T1MF_Trapezoidal("Lower MF for mild headache", [0.0, 0.0, 2.0, 5.0])
        self.MildIT2MF = IntervalT2MF_Trapezoidal("IT2MF for mild headache", self.MildUMF, self.MildLMF)
        self.MildMF = GenT2MF_Trapezoidal("GT2MF for mild headache", primer=self.MildIT2MF,
                                          numberOfzLevels=self.numberOfzLevels)

        self.ModerateUMF = T1MF_Trapezoidal("Upper MF for moderate headache", [3.0, 4.0, 6.0, 7.0])
        self.ModerateLMF = T1MF_Trapezoidal("Upper MF for moderate headache", [3.0, 5.0, 5.0, 7.0])
        self.ModerateIT2MF = IntervalT2MF_Trapezoidal("IT2MF for moderate headache", self.ModerateUMF, self.ModerateLMF)
        self.ModerateMF = GenT2MF_Trapezoidal("GT2MF for moderate headache", primer=self.ModerateIT2MF,
                                              numberOfzLevels=self.numberOfzLevels)

        self.SevereUMF = T1MF_Trapezoidal("Upper MF for severe headache", [5.0, 7.0, 10.0, 10.0])
        self.SevereLMF = T1MF_Trapezoidal("Lower MF for severe headache", [5.0, 8.0, 10.0, 10.0])
        self.SevereIT2MF = IntervalT2MF_Trapezoidal("IT2MF for severe headache", self.SevereUMF, self.SevereLMF)
        self.SevereMF = GenT2MF_Trapezoidal("GT2MF for severe headache", primer=self.SevereIT2MF,
                                            numberOfzLevels=self.numberOfzLevels)

        # Age
        self.ChildUMF = T1MF_Trapezoidal("Upper MF for child", [0.0, 0.0, 12.0, 19.0])
        self.ChildLMF = T1MF_Trapezoidal("Lower MF for child", [0.0, 0.0, 10.0, 19.0])
        self.ChildIT2MF = IntervalT2MF_Trapezoidal("IT2MF for child", self.ChildUMF, self.ChildLMF)
        self.ChildMF = GenT2MF_Trapezoidal("GT2MF for child", primer=self.ChildIT2MF,
                                           numberOfzLevels=self.numberOfzLevels)

        self.AdultUMF = T1MF_Trapezoidal("Upper MF for adult", [10.0, 19.0, 65.0, 70.0])
        self.AdultLMF = T1MF_Trapezoidal("Lower MF for adult", [12.0, 19.0, 60.0, 70.0])
        self.AdultIT2MF = IntervalT2MF_Trapezoidal("IT2MF for adult", self.AdultUMF, self.AdultLMF)
        self.AdultMF = GenT2MF_Trapezoidal("GT2MF for adult", primer=self.AdultIT2MF,
                                           numberOfzLevels=self.numberOfzLevels)

        self.ElderlyUMF = T1MF_Trapezoidal("Upper MF for elderly", [60.0, 70.0, 130.0, 130.0])
        self.ElderlyLMF = T1MF_Trapezoidal("Lower MF for elderly", [65.0, 70.0, 130.0, 130.0])
        self.ElderlyIT2MF = IntervalT2MF_Trapezoidal("IT2MF for elderly", self.ElderlyUMF, self.ElderlyLMF)
        self.ElderlyMF = GenT2MF_Trapezoidal("GT2MF for elderly", primer=self.ElderlyIT2MF,
                                             numberOfzLevels=self.numberOfzLevels)

        # Urgency Levels
        number_of_labels = 5
        seg = 100 / (2 * number_of_labels - 1)

        self.LowUMF = T1MF_Trapezoidal("Upper MF for low urgency", [0.0, 0.0, seg + 0.001, 2 * seg])
        self.LowLMF = T1MF_Trapezoidal("Lower MF for low urgency", [0.0, 0.0, seg, 2 * seg])
        self.LowIT2MF = IntervalT2MF_Trapezoidal("IT2MF for low urgency", self.LowUMF, self.LowLMF)
        self.LowMF = GenT2MF_Trapezoidal("GT2MF for low urgency", primer=self.LowIT2MF,
                                         numberOfzLevels=self.numberOfzLevels)

        self.MediumUMF = T1MF_Trapezoidal("Upper MF for medium urgency", [seg, 2 * seg, 3 * seg + 0.001, 4 * seg])
        self.MediumLMF = T1MF_Trapezoidal("Lower MF for medium urgency", [seg, 2 * seg, 3 * seg, 4 * seg])
        self.MediumIT2MF = IntervalT2MF_Trapezoidal("IT2MF for medium urgency", self.MediumUMF, self.MediumLMF)
        self.MediumMF = GenT2MF_Trapezoidal("GT2MF for medium urgency", primer=self.MediumIT2MF,
                                            numberOfzLevels=self.numberOfzLevels)

        self.HighUMF = T1MF_Trapezoidal("Upper MF for high urgency", [3 * seg, 4 * seg, 5 * seg + 0.001, 6 * seg])
        self.HighLMF = T1MF_Trapezoidal("Lower MF for high urgency", [3 * seg, 4 * seg, 5 * seg, 6 * seg])
        self.HighIT2MF = IntervalT2MF_Trapezoidal("IT2MF for high urgency", self.HighUMF, self.HighLMF)
        self.HighMF = GenT2MF_Trapezoidal("GT2MF for high urgency", primer=self.HighIT2MF,
                                          numberOfzLevels=self.numberOfzLevels)

        self.CriticalUMF = T1MF_Trapezoidal("Upper MF for critical urgency",
                                            [5 * seg, 6 * seg, 7 * seg + 0.001, 8 * seg])
        self.CriticalLMF = T1MF_Trapezoidal("Lower MF for critical urgency", [5 * seg, 6 * seg, 7 * seg, 8 * seg])
        self.CriticalIT2MF = IntervalT2MF_Trapezoidal("IT2MF for critical urgency", self.CriticalUMF, self.CriticalLMF)
        self.CriticalMF = GenT2MF_Trapezoidal("GT2MF for critical urgency", primer=self.CriticalIT2MF,
                                              numberOfzLevels=self.numberOfzLevels)

        self.EmergencyUMF = T1MF_Trapezoidal("Upper MF for emergency urgency", [7 * seg, 8 * seg, 100, 100])
        self.EmergencyLMF = T1MF_Trapezoidal("Lower MF for emergency urgency", [7 * seg, 8 * seg + 0.001, 100, 100])
        self.EmergencyIT2MF = IntervalT2MF_Trapezoidal("IT2MF for emergency urgency", self.EmergencyUMF,
                                                       self.EmergencyLMF)
        self.EmergencyMF = GenT2MF_Trapezoidal("GT2MF for emergency urgency", primer=self.EmergencyIT2MF,
                                               numberOfzLevels=self.numberOfzLevels)

        # Set up the antecedents and consequents
        # Temperature
        Cold = GenT2_Antecedent("cElderly temperature", self.ColdMF, self.temperature)
        Normal = GenT2_Antecedent("normal temperature", self.NormalMF, self.temperature)
        Hot = GenT2_Antecedent("hot temperature", self.HotMF, self.temperature)

        # Headache
        Mild = GenT2_Antecedent("mild headache", self.MildMF, self.headache)
        Moderate = GenT2_Antecedent("moderate headache", self.ModerateMF, self.headache)
        Severe = GenT2_Antecedent("severe headache", self.SevereMF, self.headache)

        # Age
        Child = GenT2_Antecedent("child", self.ChildMF, self.age)
        Adult = GenT2_Antecedent("adult", self.AdultMF, self.age)
        Elderly = GenT2_Antecedent("elderly", self.ElderlyMF, self.age)

        # Urgency
        Low = GenT2_Consequent("low", self.LowMF, self.urgency)
        Medium = GenT2_Consequent("medium", self.MediumMF, self.urgency)
        High = GenT2_Consequent("high", self.HighMF, self.urgency)
        Critical = GenT2_Consequent("critical", self.CriticalMF, self.urgency)
        Emergency = GenT2_Consequent("emergency", self.EmergencyMF, self.urgency)

        # Set up the rulebase and add rules
        self.rulebase = GenT2_Rulebase()
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Child], consequent=Low))  # Rule 1
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Adult], consequent=Low))  # Rule 2
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Elderly], consequent=Low))  # Rule 3
        self.rulebase.addRule(GenT2_Rule([Normal, Moderate, Child], consequent=Medium))  # Rule 4
        self.rulebase.addRule(GenT2_Rule([Normal, Moderate, Adult], consequent=Medium))  # Rule 5
        self.rulebase.addRule(GenT2_Rule([Normal, Moderate, Elderly], consequent=High))  # Rule 6
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Child], consequent=Critical))  # Rule 7
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Adult], consequent=Critical))  # Rule 8
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Elderly], consequent=Critical))  # Rule 9
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Child], consequent=Medium))  # Rule 10
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Adult], consequent=Medium))  # Rule 11
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Elderly], consequent=High))  # Rule 12
        self.rulebase.addRule(GenT2_Rule([Hot, Moderate, Child], consequent=High))  # Rule 13
        self.rulebase.addRule(GenT2_Rule([Hot, Moderate, Adult], consequent=High))  # Rule 14
        self.rulebase.addRule(GenT2_Rule([Hot, Moderate, Elderly], consequent=Critical))  # Rule 15
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Child], consequent=Emergency))  # Rule 16
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Adult], consequent=Critical))  # Rule 17
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Elderly], consequent=Emergency))  # Rule 18
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Child], consequent=High))  # Rule 19
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Adult], consequent=Medium))  # Rule 20
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Elderly], consequent=High))  # Rule 21
        self.rulebase.addRule(GenT2_Rule([Cold, Moderate, Child], consequent=Emergency))  # Rule 22
        self.rulebase.addRule(GenT2_Rule([Cold, Moderate, Adult], consequent=Critical))  # Rule 23
        self.rulebase.addRule(GenT2_Rule([Cold, Moderate, Elderly], consequent=Emergency))  # Rule 24
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Child], consequent=Emergency))  # Rule 25
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Adult], consequent=Emergency))  # Rule 26
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Elderly], consequent=Emergency))  # Rule 27

    def run(self, unit=False):

        # input function
        while True:
            Patienttemperature = float(input("Enter patient's temperture (24-44):"))
            if 24 <= Patienttemperature <= 44:
                break
            print("Temperture must be between 24 and 44. Please try again.")

        while True:
            Patientheadache = float(input("Enter patient's headache (0-10):"))
            if 0 <= Patientheadache <= 10:
                break
            print("Headache must be between 24 and 44. Please try again.")

        while True:
            Patientage = float(input("Enter patient's age (0-130):"))
            if 0 <= Patientage <= 130:
                break
            print("Temperture must be between 24 and 44. Please try again.")

        self.Result(Patienttemperature, Patientheadache, Patientage)

    def ResultForInterval(self, temperature_interval, headache_interval, age_interval, samples=10):
        """
        Calculate the output based on interval inputs by sampling and aggregating.
        :param temperature_interval: Tuple (min_temp, max_temp)
        :param headache_interval: Tuple (min_headache, max_headache)
        :param age_interval: Tuple (min_age, max_age)
        :param samples: Number of samples to take within each interval
        """
        # Discretize each interval into `samples` points
        temp_samples = self.discretize_interval(temperature_interval, samples)
        headache_samples = self.discretize_interval(headache_interval, samples)
        age_samples = self.discretize_interval(age_interval, samples)

        results = []

        # Evaluate the fuzzy system for each combination of sampled values
        for temp in temp_samples:
            for headache in headache_samples:
                for age in age_samples:
                    self.temperature.setInput(temp)
                    self.headache.setInput(headache)
                    self.age.setInput(age)
                    output = self.rulebase.evaluate(1)[self.urgency]  # Using centroid type reduction
                    results.append(output)

        # Aggregate the results average and max
        average_result = sum(results) / len(results)
        max_result = max(results)

        print(f"Interval Input Results:")
        print(f"Average Urgency: {average_result}")
        print(f"Maximum Urgency: {max_result}")

    def discretize_interval(self, interval, samples):
        """
        Discretize an interval into evenly spaced sample points.
        :param interval: Tuple (min_value, max_value)
        :param samples: Number of samples to generate
        :return: List of sampled points
        """
        min_val, max_val = interval
        return [min_val + i * (max_val - min_val) / (samples - 1) for i in range(samples)]

    def Result_for_interval_using_centroid(self, function, temperature_interval, headache_interval, age_interval):
        """
        Calculate the centroid of the output f(x, y, z) over the given input intervals.
        :param function: The function defining the output (f(x, y, z)).
        :param temperature_interval: A tuple of intervals ((a_x, b_x), (a_y, b_y), (a_z, b_z)).
        :param headache_interval: Tuple (min_headache, max_headache)
        :param age_interval: Tuple (min_age, max_age)
        :return: The centroid of the output (ans_centroid).
        """
        (a_x, b_x), (a_y, b_y), (a_z, b_z) = temperature_interval, headache_interval, age_interval

        # Numerator: Total output
        total_output, _ = tplquad(
            function,
            a_z, b_z,  # z limits (innermost)
            lambda z: a_y, lambda z: b_y,  # y limits (middle)
            lambda z, y: a_x, lambda z, y: b_x,  # x limits (outermost)
        )

        # Denominator: Input volume
        input_volume = (b_x - a_x) * (b_y - a_y) * (b_z - a_z)

        # Output centroid
        ans_centroid = total_output / input_volume

        return ans_centroid

    def Result_for_interval_using_fixed_step(self, function, temperature_interval, headache_interval, age_interval,
                                             total_steps_for_each_var):
        """
        Calculate the centroid of the output f(x, y, z) over the given input intervals using fixed step size.
        :param function: The function defining the output (f(x, y, z)).
        :param temperature_interval: Interval for temperature (a_x, b_x).
        :param headache_interval: Interval for headache (a_y, b_y).
        :param age_interval: Interval for age (a_z, b_z).
        :param total_steps_for_each_var: total_steps_for_each_var
        :return: The centroid of the output (ans_centroid).
        """
        (a_x, b_x), (a_y, b_y), (a_z, b_z) = temperature_interval, headache_interval, age_interval
        step_x = (b_x - a_x) / total_steps_for_each_var
        step_y = (b_y - a_y) / total_steps_for_each_var
        step_z = (b_z - a_z) / total_steps_for_each_var

        # Create the grid points for each interval with the specified step size
        x_points = np.arange(a_x, b_x, step_x)
        y_points = np.arange(a_y, b_y, step_y)
        z_points = np.arange(a_z, b_z, step_z)

        # Step sizes for the intervals
        dx, dy, dz = step_x, step_y, step_z

        # Initialize total output and total volume
        total_output = 0.0
        total_volume = 0.0

        # Perform nested summation to approximate the integral
        for x in x_points:
            for y in y_points:
                for z in z_points:
                    volume_element = dx * dy * dz  # Volume of each small cuboid
                    total_output += function(x, y, z) * volume_element
                    total_volume += volume_element

        # Compute the centroid
        ans_centroid = total_output / total_volume

        return ans_centroid

    def Result(self, temperture_level, headache_level, age_level) -> None:
        """Calculate the output based on the two inputs"""
        self.temperature.setInput(temperture_level)
        self.headache.setInput(headache_level)
        self.age.setInput(age_level)

        print("Patient's Temperture was: " + str(self.temperature.getInput()))
        print("Patient's Headache Level was: " + str(self.headache.getInput()))
        print("Patient's Age was: " + str(self.age.getInput()))
        print("Using height center of sets type reduction, the zSlices based general type-2 FLS recommends a "
              + "urgency of: " + str(self.rulebase.evaluate(0)[self.urgency]))
        print("Using centroid type reduction, the zSlices based general type-2 FLS recommends a"
              + "urgency of: " + str(self.rulebase.evaluate(1)[self.urgency]))

    def Result_with_height_center_type_reduction(self, temperture_level, headache_level, age_level):
        """Calculate the output based on the two inputs"""
        self.temperature.setInput(temperture_level)
        self.headache.setInput(headache_level)
        self.age.setInput(age_level)
        return self.rulebase.evaluate(0)[self.urgency]

    def Result_with_centroid_type_reduction(self, temperture_level, headache_level, age_level):
        """Calculate the output based on the two inputs"""
        self.temperature.setInput(temperture_level)
        self.headache.setInput(headache_level)
        self.age.setInput(age_level)
        ans = self.rulebase.evaluate(1)[self.urgency]
        # print(temperture_level, headache_level, age_level, ans)
        return ans

    def plotT1MFs(self, name, sets, xAxisRange, discretizationLevel):
        """Plot the lines for each membership function of the sets"""
        self.plot.figure()
        self.plot.title(name)
        for i in range(len(sets)):
            self.plot.plotMF(name.replace("Membership Functions", ""), sets[i].getName(), sets[i], discretizationLevel,
                             xAxisRange, Tuple(0.0, 1.05), False)
        self.plot.legend()

    def plotGen2MF2D(self, name, sets, xAxisRange, discretizationLevel):
        """Plot the lines for each membership function of the sets"""
        self.plot.figure()
        self.plot.title(name)

        for i in range(0, len(sets), 2):
            upper_set = sets[i]
            lower_set = sets[i + 1]

            # plot the upper membership function
            self.plot.plotMF(name.replace("Membership Functions", ""), upper_set.getName(), upper_set,
                             discretizationLevel, xAxisRange, Tuple(0.0, 1.05), False)

            # plot the lower membership function
            self.plot.plotMF(name.replace("Membership Functions", ""), lower_set.getName(), lower_set,
                             discretizationLevel, xAxisRange, Tuple(0.0, 1.05), False)

            x = self.plot.discretize(upper_set.getSupport(), discretizationLevel)
            y_upper = [upper_set.getFS(xi) for xi in x]
            y_lower = [lower_set.getFS(xi) for xi in x]

            # fill the area between the upper and lower membership functions
            plt.fill_between(x, y_upper, y_lower, color='gray', alpha=0.5)  # Adjust color and transparency

        self.plot.legend()

    def plotGen2MF3D(self, name, sets, xAxisRange, discretizationLevel, plotAsLines, plotAsSurface):
        """Plot the lines for each membership function of the sets"""
        if plotAsLines:
            self.plot.figure3d()
            self.plot.title(name)
            for i in range(len(sets)):
                self.plot.plotMFasLines(sets[i], discretizationLevel)
        if plotAsSurface:
            self.plot.figure3d()
            self.plot.title(name)
            for i in range(len(sets)):
                self.plot.plotMFasSurface(sets[i].getName(), sets[i], xAxisRange, discretizationLevel, False)


def peak_data():
    # Peak intervals for each input
    temperature_intervals = [
        (24, 35),  # Cold
        (36.4, 36.9),  # Normal
        (38, 44)  # Hot
    ]
    headache_intervals = [
        (0, 2),  # Mild
        (4, 6),  # Moderate
        (8, 10)  # Severe
    ]
    age_intervals = [
        (0, 10),  # Child
        (19, 60),  # Adult
        (70, 130)  # Elderly
    ]
    case = Case2(unit=False)
    for temp in temperature_intervals:
        for head in headache_intervals:
            for age in age_intervals:
                try:
                    res = case.Result_for_interval_using_fixed_step(case.Result_with_centroid_type_reduction, temp,
                                                                    head,
                                                                    age,
                                                                    total_steps_for_each_var=5)
                    print(f"Temperature:{temp}, Headache:{head}, Age:{age}, result: {res}")
                except Exception as e:
                    print(e)
                    continue


if __name__ == "__main__":
    peak_data()
    # Case2()
    # Define intervals for temperature, headache, and age
    # temperature_interval = (36.4, 36.6)
    # headache_interval = (0.0, 2.0)
    # age_interval = (16, 17)
    #
    # # Calculate and print the results for interval inputs
    # case = Case2(unit=True)  # Initialize the fuzzy system
    # print(case.Result_for_interval_using_fixed_step(case.Result_with_centroid_type_reduction, temperature_interval,
    #                                                 headache_interval, age_interval, total_steps_for_each_var=5))
    # # print(case.Result_for_interval_using_centroid(case.Result_with_height_center_type_reduction, temperature_interval,
    # #                                               headache_interval, age_interval))
