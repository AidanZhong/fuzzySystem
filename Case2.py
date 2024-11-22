import matplotlib.pyplot as plt
from juzzyPython.generalType2zSlices.sets.GenT2MF_Gaussian import GenT2MF_Gaussian
from juzzyPython.generalType2zSlices.sets.GenT2MF_Trapezoidal import GenT2MF_Trapezoidal
from juzzyPython.generalType2zSlices.system.GenT2_Antecedent import GenT2_Antecedent
from juzzyPython.generalType2zSlices.system.GenT2_Consequent import GenT2_Consequent
from juzzyPython.generalType2zSlices.system.GenT2_Rule import GenT2_Rule
from juzzyPython.generalType2zSlices.system.GenT2_Rulebase import GenT2_Rulebase
from juzzyPython.generic.Input import Input
from juzzyPython.generic.Output import Output
from juzzyPython.generic.Plot import Plot
from juzzyPython.generic.Tuple import Tuple
from juzzyPython.intervalType2.sets.IntervalT2MF_Gaussian import IntervalT2MF_Gaussian
from juzzyPython.intervalType2.sets.IntervalT2MF_Trapezoidal import IntervalT2MF_Trapezoidal
from juzzyPython.type1.sets.T1MF_Gaussian import T1MF_Gaussian
from juzzyPython.type1.sets.T1MF_Trapezoidal import T1MF_Trapezoidal


class Case2:
    def __init__(self, unit=False) -> None:
        self.numberOfzLevels = 4

        # Inputs to the FLS
        self.temperature = Input("temperature", Tuple(24, 44))
        self.headache = Input("headache", Tuple(0, 10))
        self.age = Input("age", Tuple(0, 130))
        # Output
        self.urgency = Output(("urgency"), Tuple(0, 100))

        self.plot = Plot()

        # Set up the membership functions (MFs) for each input and output
        # Temperature
        self.OldUMF = T1MF_Trapezoidal("Upper MF for cold temperature", [24.0, 24.0, 35.001, 36.4])
        self.OldLMF = T1MF_Trapezoidal("Lower MF for cold temperature", [24.0, 24.0, 35.0, 36.4])
        self.OldIT2MF = IntervalT2MF_Trapezoidal("IT2MF for cold temperature", self.OldUMF,
                                                 self.OldLMF)
        self.OldMF = GenT2MF_Trapezoidal("GT2MF for cold temperature", primer=self.OldIT2MF,
                                         numberOfzLevels=self.numberOfzLevels)

        self.NormalUMF = T1MF_Trapezoidal("Upper MF for normal temperature", [35.0, 36.4, 36.6, 38.0])
        self.NormalLMF = T1MF_Trapezoidal("Lower MF for normal temperature", [35.001, 36.4, 36.6, 38.0])
        self.NormalIT2MF = IntervalT2MF_Trapezoidal("IT2MF for normal temperature", self.NormalUMF, self.NormalLMF)
        self.NormalMF = GenT2MF_Trapezoidal("GT2MF for normal temperature", primer=self.NormalIT2MF,
                                            numberOfzLevels=self.numberOfzLevels)

        self.HotUMF = T1MF_Trapezoidal("Upper MF for hot temperature", [36.6, 38.0, 44.0, 44.0])
        self.HotLMF = T1MF_Trapezoidal("Lower MF for hot temperature", [36.601, 38.0, 44.0, 44.0])
        self.HotIT2MF = IntervalT2MF_Trapezoidal("IT2MF for hot temperature", self.HotUMF, self.HotLMF)
        self.HotMF = GenT2MF_Trapezoidal("GT2MF for hot temperature", primer=self.HotIT2MF,
                                         numberOfzLevels=self.numberOfzLevels)

        # Headache
        self.SlightlyUMF = T1MF_Trapezoidal("Upper MF for slightly headache", [0.0, 0.0, 3.0, 5.0])
        self.SlightlyLMF = T1MF_Trapezoidal("Lower MF for slightly headache", [0.0, 0.0, 2.0, 5.0])
        self.SlightlyIT2MF = IntervalT2MF_Trapezoidal("IT2MF for slightly headache", self.SlightlyUMF, self.SlightlyLMF)
        self.SlightlyMF = GenT2MF_Trapezoidal("GT2MF for slightly headache", primer=self.SlightlyIT2MF,
                                              numberOfzLevels=self.numberOfzLevels)

        self.MildUMF = T1MF_Gaussian("Upper MF for mild headache", 5.0, 1)
        self.MildLMF = T1MF_Gaussian("Lower MF for mild headache", 5.0, 0.5)
        self.MildIT2MF = IntervalT2MF_Gaussian("IT2MF for mild headache", self.MildUMF, self.MildLMF)
        self.MildMF = GenT2MF_Gaussian("GT2MF for mild headache", primer=self.MildIT2MF,
                                       numberOfzLevels=self.numberOfzLevels)

        self.SevereUMF = T1MF_Trapezoidal("Upper MF for severe headache", [5.0, 7.0, 10.0, 10.0])
        self.SevereLMF = T1MF_Trapezoidal("Lower MF for severe headache", [5.0, 8.0, 10.0, 10.0])
        self.SevereIT2MF = IntervalT2MF_Trapezoidal("IT2MF for severe headache", self.SevereUMF, self.SevereLMF)
        self.SevereMF = GenT2MF_Trapezoidal("GT2MF for severe headache", primer=self.SevereIT2MF,
                                            numberOfzLevels=self.numberOfzLevels)

        # Age
        self.YoungUMF = T1MF_Trapezoidal("Upper MF for young age", [0.0, 0.0, 22.0, 45.0])
        self.YoungLMF = T1MF_Trapezoidal("Lower MF for young age", [0.0, 0.0, 17.0, 40.0])
        self.YoungIT2MF = IntervalT2MF_Trapezoidal("IT2MF for young age", self.YoungUMF, self.YoungLMF)
        self.YoungMF = GenT2MF_Trapezoidal("GT2MF for young age", primer=self.YoungIT2MF,
                                           numberOfzLevels=self.numberOfzLevels)

        self.MidUMF = T1MF_Trapezoidal("Upper MF for mid age", [40.0, 45.0, 60.0, 65.0])
        self.MidLMF = T1MF_Trapezoidal("Lower MF for mid age", [45.0, 45.001, 60.0, 60.001])
        self.MidIT2MF = IntervalT2MF_Trapezoidal("IT2MF for mid age", self.MidUMF, self.MidLMF)
        self.MidMF = GenT2MF_Trapezoidal("GT2MF for mid age", primer=self.MidIT2MF,
                                         numberOfzLevels=self.numberOfzLevels)

        self.OldUMF = T1MF_Trapezoidal("Upper MF for old age", [60.0, 70.0, 130.0, 130.0])
        self.OldLMF = T1MF_Trapezoidal("Lower MF for old age", [65.0, 70.0, 130.0, 130.0])
        self.OldIT2MF = IntervalT2MF_Trapezoidal("IT2MF for old age", self.OldUMF, self.OldLMF)
        self.OldMF = GenT2MF_Trapezoidal("GT2MF for old age", primer=self.OldIT2MF,
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
        Cold = GenT2_Antecedent("cold temperature", self.OldMF, self.temperature)
        Normal = GenT2_Antecedent("normal temperature", self.NormalMF, self.temperature)
        Hot = GenT2_Antecedent("hot temperature", self.HotMF, self.temperature)

        # Headache
        Slightly = GenT2_Antecedent("no headache", self.SlightlyMF, self.headache)
        Mild = GenT2_Antecedent("mild headache", self.MildMF, self.headache)
        Severe = GenT2_Antecedent("severe headache", self.SevereMF, self.headache)

        # Age
        Young = GenT2_Antecedent("young age", self.YoungMF, self.age)
        Mid = GenT2_Antecedent("mid age", self.MidMF, self.age)
        Old = GenT2_Antecedent("old age", self.OldMF, self.age)

        # Urgency
        Low = GenT2_Consequent("low", self.LowMF, self.urgency)
        Medium = GenT2_Consequent("medium", self.MediumMF, self.urgency)
        High = GenT2_Consequent("high", self.HighMF, self.urgency)
        Critical = GenT2_Consequent("critical", self.CriticalMF, self.urgency)
        Emergency = GenT2_Consequent("emergency", self.EmergencyMF, self.urgency)

        # Set up the rulebase and add rules
        self.rulebase = GenT2_Rulebase()
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Young], consequent=Low))  # Rule 1
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Mid], consequent=Low))  # Rule 2
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Old], consequent=Low))  # Rule 3
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Young], consequent=Medium))  # Rule 4
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Mid], consequent=Medium))  # Rule 5
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Old], consequent=High))  # Rule 6
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Young], consequent=High))  # Rule 7
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Mid], consequent=High))  # Rule 8
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Old], consequent=Emergency))  # Rule 9
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Young], consequent=Medium))  # Rule 10
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Mid], consequent=Medium))  # Rule 11
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Old], consequent=High))  # Rule 12
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Young], consequent=High))  # Rule 13
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Mid], consequent=High))  # Rule 14
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Old], consequent=Critical))  # Rule 15
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Young], consequent=Critical))  # Rule 16
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Mid], consequent=Emergency))  # Rule 17
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Old], consequent=Emergency))  # Rule 18
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Young], consequent=High))  # Rule 19
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Mid], consequent=High))  # Rule 20
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Old], consequent=Critical))  # Rule 21
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Young], consequent=Critical))  # Rule 22
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Mid], consequent=Critical))  # Rule 23
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Old], consequent=Emergency))  # Rule 24
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Young], consequent=Emergency))  # Rule 25
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Mid], consequent=Emergency))  # Rule 26
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Old], consequent=Emergency))  # Rule 27

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

        # Plot the Membership Function in 3D
        # self.plotGen2MF3D("Headache Membership Functions",[self.SlightlyMF, self.MildMF, self.SevereMF], self.headache.getDomain(), 100, True, True)
        # self.plotGen2MF3D("Age Membership Functions",[self.YoungMF, self.MidMF, self.OldMF], self.age.getDomain(), 100, True, True)

        # plot the Membership Function in 2D
        self.plotT1MFs("Temperature Membership Functions", [self.OldUMF, self.NormalUMF, self.HotUMF],
                       self.temperature.getDomain(),
                       200)
        self.plotGen2MF2D("Headache Membership Functions",
                          [self.SlightlyUMF, self.SlightlyLMF, self.MildUMF, self.MildLMF, self.SevereUMF,
                           self.SevereLMF], self.headache.getDomain(),
                          200)
        self.plotGen2MF2D("Age Membership Functions",
                          [self.YoungUMF, self.YoungLMF, self.MidUMF, self.MidLMF, self.OldUMF, self.OldLMF],
                          self.age.getDomain(), 200)
        self.plotT1MFs("Urgency Membership Functions",
                       [self.LowUMF, self.MediumUMF, self.HighUMF, self.CriticalUMF, self.EmergencyUMF],
                       self.urgency.getDomain(), 200)

        if not unit:
            self.plot.show()

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

        # print("Centroid of the output for TIP (based on centroid type reduction):")
        # centroid = self.rulebase.evaluateGetCentroid(1)
        # centroidUrgency = list(centroid[self.urgency])
        # centroidUrgencyXValues = centroidUrgency[0]
        # centroidUrgencyYValues = centroidUrgency[1]
        # for zLevel in range(len(centroidUrgencyXValues)):
        #     print(centroidUrgencyXValues[zLevel].toString()+" at y= "+str(centroidUrgencyYValues[zLevel]))

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


if __name__ == "__main__":
    # Case2()
    # Define intervals for temperature, headache, and age
    temperature_interval = (36.0, 37.5)
    headache_interval = (2.0, 5.0)
    age_interval = (20, 30)

    # Calculate and print the results for interval inputs
    case = Case2(unit=True)  # Initialize the fuzzy system
    case.ResultForInterval(temperature_interval, headache_interval, age_interval, samples=5)
