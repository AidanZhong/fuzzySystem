from juzzyPython.generic.Tuple import Tuple
from juzzyPython.generic.Output import Output
from juzzyPython.generic.Input import Input
from juzzyPython.generic.Plot import Plot
from juzzyPython.generalType2zSlices.system.GenT2_Rule import GenT2_Rule
from juzzyPython.generalType2zSlices.system.GenT2_Rulebase import GenT2_Rulebase
from juzzyPython.generalType2zSlices.system.GenT2_Antecedent import GenT2_Antecedent
from juzzyPython.generalType2zSlices.system.GenT2_Consequent import GenT2_Consequent
from juzzyPython.type1.sets.T1MF_Trapezoidal import T1MF_Trapezoidal
from juzzyPython.intervalType2.sets.IntervalT2MF_Trapezoidal import IntervalT2MF_Trapezoidal
from juzzyPython.generalType2zSlices.sets.GenT2MF_Trapezoidal import GenT2MF_Trapezoidal
from juzzyPython.type1.sets.T1MF_Gaussian import T1MF_Gaussian
from juzzyPython.intervalType2.sets.IntervalT2MF_Gaussian import IntervalT2MF_Gaussian
from juzzyPython.generalType2zSlices.sets.GenT2MF_Gaussian import GenT2MF_Gaussian
import matplotlib.pyplot as plt

class Case1:
    def __init__(self,unit = False) -> None:
        self.numberOfzLevels = 5
    

        # Inputs to the FLS
        self.temperature = Input("temperature",Tuple(24,44))
        self.headache = Input("headache",Tuple(0,10))
        self.age = Input("age",Tuple(0,130))
        # Output
        self.urgency = Output(("urgency"),Tuple(0,100))
        
        self.plot = Plot()

        # Set up the membership functions (MFs) for each input and output
        # Temperature
        ColdUMF = T1MF_Trapezoidal("Upper MF for cold temperature", [24.0, 24.0, 35.001, 36.4])
        ColdLMF = T1MF_Trapezoidal("Lower MF for cold temperature", [24.0, 24.0, 35.0, 36.4])
        ColdIT2MF = IntervalT2MF_Trapezoidal("IT2MF for cold temperature",ColdUMF,ColdLMF)
        ColdMF = GenT2MF_Trapezoidal("GT2MF for cold temperature", primer = ColdIT2MF, numberOfzLevels = self.numberOfzLevels)
        
        NormalUMF = T1MF_Trapezoidal("Upper MF for normal temperature", [35.0, 35.8, 36.9, 38.0])
        NormalLMF = T1MF_Trapezoidal("Lower MF for normal temperature", [35.001, 35.8, 36.9, 38.0])
        NormalIT2MF = IntervalT2MF_Trapezoidal("IT2MF for normal temperature",NormalUMF,NormalLMF)
        NormalMF = GenT2MF_Trapezoidal("GT2MF for normal temperature", primer = NormalIT2MF, numberOfzLevels = self.numberOfzLevels)
        
        HotUMF = T1MF_Trapezoidal("Upper MF for hot temperature", [36.6, 38.0, 44.0, 44.0])
        HotLMF = T1MF_Trapezoidal("Lower MF for hot temperature", [36.601, 38.0, 44.0, 44.0])
        HotIT2MF = IntervalT2MF_Trapezoidal("IT2MF for hot temperature",HotUMF,HotLMF)
        HotMF = GenT2MF_Trapezoidal("GT2MF for hot temperature", primer = HotIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Headache
        SlightlyUMF = T1MF_Trapezoidal("Upper MF for slightly headache", [0.0, 0.0, 3.0, 5.0])
        SlightlyLMF = T1MF_Trapezoidal("Lower MF for slightly headache", [0.0, 0.0, 2.0, 5.0])
        SlightlyIT2MF = IntervalT2MF_Trapezoidal("IT2MF for slightly headache",SlightlyUMF,SlightlyLMF)
        SlightlyMF = GenT2MF_Trapezoidal("GT2MF for slightly headache", primer = SlightlyIT2MF, numberOfzLevels = self.numberOfzLevels)
        
        MildUMF = T1MF_Gaussian("Upper MF for mild headache", 5.0, 1)
        MildLMF = T1MF_Gaussian("Lower MF for mild headache", 5.0, 0.5)
        MildIT2MF = IntervalT2MF_Gaussian("IT2MF for mild headache",MildUMF,MildLMF)
        MildMF = GenT2MF_Gaussian("GT2MF for mild headache", primer = MildIT2MF, numberOfzLevels = self.numberOfzLevels)
        
        SevereUMF = T1MF_Trapezoidal("Upper MF for severe headache", [5.0, 7.0, 10.0, 10.0])
        SevereLMF = T1MF_Trapezoidal("Lower MF for severe headache", [5.0, 8.0, 10.0, 10.0])
        SevereIT2MF = IntervalT2MF_Trapezoidal("IT2MF for severe headache",SevereUMF,SevereLMF)
        SevereMF = GenT2MF_Trapezoidal("GT2MF for severe headache", primer = SevereIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Age
        YoungUMF = T1MF_Trapezoidal("Upper MF for young age", [0.0, 0.0, 22.0, 45.0])
        YoungLMF = T1MF_Trapezoidal("Lower MF for young age", [0.0, 0.0, 17.0, 40.0])
        YoungIT2MF = IntervalT2MF_Trapezoidal("IT2MF for young age",YoungUMF,YoungLMF)
        YoungMF = GenT2MF_Trapezoidal("GT2MF for young age", primer = YoungIT2MF, numberOfzLevels = self.numberOfzLevels)

        MidUMF = T1MF_Trapezoidal("Upper MF for mid age", [40.0, 45.0, 60.0, 65.0])
        MidLMF = T1MF_Trapezoidal("Lower MF for mid age", [45.0, 45.001, 60.0, 60.001])
        MidIT2MF = IntervalT2MF_Trapezoidal("IT2MF for mid age",MidUMF,MidLMF)
        MidMF = GenT2MF_Trapezoidal("GT2MF for mid age", primer = MidIT2MF, numberOfzLevels = self.numberOfzLevels)

        OldUMF = T1MF_Trapezoidal("Upper MF for old age", [60.0, 70.0, 130.0, 130.0])
        OldLMF = T1MF_Trapezoidal("Lower MF for old age", [65.0, 70.0, 130.0, 130.0])
        OldIT2MF = IntervalT2MF_Trapezoidal("IT2MF for old age",OldUMF,OldLMF)
        OldMF = GenT2MF_Trapezoidal("GT2MF for old age", primer = OldIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Urgency Levels
        number_of_labels = 5
        seg = 100 / (2 * number_of_labels - 1)

        LowUMF = T1MF_Trapezoidal("Upper MF for low urgency", [0.0, 0.0, seg + 0.001, 2 * seg])
        LowLMF = T1MF_Trapezoidal("Lower MF for low urgency", [0.0, 0.0, seg, 2 * seg])
        LowIT2MF = IntervalT2MF_Trapezoidal("IT2MF for low urgency", LowUMF, LowLMF)
        LowMF = GenT2MF_Trapezoidal("GT2MF for low urgency", primer=LowIT2MF, numberOfzLevels=self.numberOfzLevels)

        MediumUMF = T1MF_Trapezoidal("Upper MF for medium urgency", [seg, 2 * seg, 3 * seg + 0.001, 4 * seg])
        MediumLMF = T1MF_Trapezoidal("Lower MF for medium urgency", [seg, 2 * seg, 3 * seg, 4 * seg])
        MediumIT2MF = IntervalT2MF_Trapezoidal("IT2MF for medium urgency", MediumUMF, MediumLMF)
        MediumMF = GenT2MF_Trapezoidal("GT2MF for medium urgency", primer=MediumIT2MF, numberOfzLevels=self.numberOfzLevels)

        HighUMF = T1MF_Trapezoidal("Upper MF for high urgency", [3 * seg, 4 * seg, 5 * seg + 0.001, 6 * seg])
        HighLMF = T1MF_Trapezoidal("Lower MF for high urgency", [3 * seg, 4 * seg, 5 * seg, 6 * seg])
        HighIT2MF = IntervalT2MF_Trapezoidal("IT2MF for high urgency", HighUMF, HighLMF)
        HighMF = GenT2MF_Trapezoidal("GT2MF for high urgency", primer=HighIT2MF, numberOfzLevels=self.numberOfzLevels)

        CriticalUMF = T1MF_Trapezoidal("Upper MF for critical urgency", [5 * seg, 6 * seg, 7 * seg + 0.001, 8 * seg])
        CriticalLMF = T1MF_Trapezoidal("Lower MF for critical urgency", [5 * seg, 6 * seg, 7 * seg, 8 * seg])
        CriticalIT2MF = IntervalT2MF_Trapezoidal("IT2MF for critical urgency", CriticalUMF, CriticalLMF)
        CriticalMF = GenT2MF_Trapezoidal("GT2MF for critical urgency", primer=CriticalIT2MF, numberOfzLevels=self.numberOfzLevels)

        EmergencyUMF = T1MF_Trapezoidal("Upper MF for emergency urgency", [7 * seg, 8 * seg, 100, 100])
        EmergencyLMF = T1MF_Trapezoidal("Lower MF for emergency urgency", [7 * seg, 8 * seg + 0.001, 100, 100])
        EmergencyIT2MF = IntervalT2MF_Trapezoidal("IT2MF for emergency urgency", EmergencyUMF, EmergencyLMF)
        EmergencyMF = GenT2MF_Trapezoidal("GT2MF for emergency urgency", primer=EmergencyIT2MF, numberOfzLevels=self.numberOfzLevels)

        # Set up the antecedents and consequents
        # Temperature
        Cold = GenT2_Antecedent("cold temperature", ColdMF, self.temperature)
        Normal = GenT2_Antecedent("normal temperature", NormalMF, self.temperature)
        Hot = GenT2_Antecedent("hot temperature", HotMF, self.temperature)

        # Headache
        Slightly = GenT2_Antecedent("no headache", SlightlyMF, self.headache)
        Mild = GenT2_Antecedent("mild headache", MildMF, self.headache)
        Severe = GenT2_Antecedent("severe headache", SevereMF, self.headache)

        # Age
        Young = GenT2_Antecedent("young age", YoungMF, self.age)
        Mid = GenT2_Antecedent("mid age", MidMF, self.age)
        Old = GenT2_Antecedent("old age", OldMF, self.age)

        # Urgency
        Low =  GenT2_Consequent("low", LowMF, self.urgency)
        Medium =  GenT2_Consequent("medium", MediumMF, self.urgency)
        High =  GenT2_Consequent("high", HighMF, self.urgency)
        Critical =  GenT2_Consequent("critical",  CriticalMF, self.urgency)
        Emergency =  GenT2_Consequent("emergency",  EmergencyMF, self.urgency)
        
        
        # Set up the rulebase and add rules
        self.rulebase = GenT2_Rulebase()
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Young], consequent = Low)) #Rule 1
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Mid], consequent = Low)) #Rule 2
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Old], consequent = Low)) #Rule 3
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Young], consequent = Medium)) # Rule 4
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Mid], consequent = Medium)) # Rule 5
        self.rulebase.addRule(GenT2_Rule([Normal, Mild, Old], consequent = High)) # Rule 6
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Young], consequent = High)) # Rule 7
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Mid], consequent = High)) # Rule 8
        self.rulebase.addRule(GenT2_Rule([Normal, Severe, Old], consequent = Emergency)) # Rule 9
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Young], consequent = Medium)) # Rule 10
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Mid], consequent = Medium)) # Rule 11
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Old], consequent = High)) # Rule 12
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Young], consequent = High)) # Rule 13
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Mid], consequent = High)) # Rule 14
        self.rulebase.addRule(GenT2_Rule([Hot, Mild, Old], consequent = Critical)) # Rule 15
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Young], consequent = Critical)) # Rule 16
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Mid], consequent = Emergency)) # Rule 17
        self.rulebase.addRule(GenT2_Rule([Hot, Severe, Old], consequent = Emergency)) # Rule 18
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Young], consequent = High)) # Rule 19
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Mid], consequent = High)) # Rule 20
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Old], consequent = Critical)) # Rule 21
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Young], consequent = Critical)) # Rule 22
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Mid], consequent = Critical)) # Rule 23
        self.rulebase.addRule(GenT2_Rule([Cold, Mild, Old], consequent = Emergency)) # Rule 24
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Young], consequent = Emergency)) # Rule 25
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Mid], consequent = Emergency)) # Rule 26
        self.rulebase.addRule(GenT2_Rule([Cold, Severe, Old], consequent = Emergency)) # Rule 27

         # input function
        while True:
            Patienttemperature = float(input("Enter patient's temperture (24-44):"))
            if  24 <= Patienttemperature <= 44:
                break
            print("Temperture must be between 24 and 44. Please try again.")

        while True:
            Patientheadache= float(input("Enter patient's headache (0-10):"))
            if  0 <= Patientheadache <= 10:
                break
            print("Headache must be between 24 and 44. Please try again.")

        while True:
            Patientage = float(input("Enter patient's age (0-130):"))
            if  0 <= Patientage <= 130:
                break
            print("Temperture must be between 24 and 44. Please try again.")

        

        # self.Result(Patienttemperature,Patientheadache,Patientage)

        # self.Result(37.8, 4.5, 31)     # Non-Peak Data Sample Rule 1
        # self.Result(37.5, 3.9, 44.5)   # Non-Peak Data Sample Rule 2
        # self.Result(35.6, 3.0, 64)     # Non-Peak Data Sample Rule 3
        # self.Result(37.8, 5.9, 24)     # Non-Peak Data Sample Rule 4
        # self.Result(37.5, 5.5, 62)     # Non-Peak Data Sample Rule 5
        # self.Result(35.6, 3.7, 66)     # Non-Peak Data Sample Rule 6
        # self.Result(37.8, 7.0, 38)     # Non-Peak Data Sample Rule 7
        # self.Result(37.5, 5.5, 43.7)   # Non-Peak Data Sample Rule 8
        # self.Result(35.6, 6.1, 68.5)   # Non-Peak Data Sample Rule 9

        # self.Result(37.3, 4.5, 31)     # Non-Peak Data Sample Rule 10
        # self.Result(37.7, 3.9, 44.5)   # Non-Peak Data Sample Rule 11
        # self.Result(36.9, 3.0, 64)     # Non-Peak Data Sample Rule 12
        # self.Result(37.3, 5.9, 24)     # Non-Peak Data Sample Rule 13
        # self.Result(37.7, 5.5, 62)     # Non-Peak Data Sample Rule 14
        # self.Result(36.9, 3.7, 66)     # Non-Peak Data Sample Rule 15
        # self.Result(37.3, 7.0, 38)     # Non-Peak Data Sample Rule 16
        # self.Result(37.7, 5.5, 43.7)   # Non-Peak Data Sample Rule 17
        # self.Result(36.9, 6.1, 68.5)   # Non-Peak Data Sample Rule 18

        self.Result(36.1, 4.5, 31)     # Non-Peak Data Sample Rule 19
        self.Result(35.3, 3.9, 44.5)   # Non-Peak Data Sample Rule 20
        self.Result(35.7, 3.0, 64)     # Non-Peak Data Sample Rule 21
        self.Result(36.1, 5.9, 24)     # Non-Peak Data Sample Rule 22
        self.Result(35.3, 5.5, 62)     # Non-Peak Data Sample Rule 23
        self.Result(35.7, 3.7, 66)   # Non-Peak Data Sample Rule 24
        self.Result(36.1, 7.0, 38)     # Non-Peak Data Sample Rule 25
        self.Result(35.3, 5.5, 43.7)   # Non-Peak Data Sample Rule 26
        self.Result(35.7, 6.1, 68.5)   # Non-Peak Data Sample Rule 27






        # Plot the Membership Function in 3D
        # self.plotGen2MF3D("Headache Membership Functions",[SlightlyMF, MildMF, SevereMF], self.headache.getDomain(), 100, True, True)
        # self.plotGen2MF3D("Age Membership Functions",[YoungMF, MidMF, OldMF], self.age.getDomain(), 100, True, True)
        
        # plot the Membership Function in 2D
        # self.plotT1MFs("Temperature Membership Functions",[ColdUMF, NormalUMF, HotUMF], self.temperature.getDomain(), 200)
        # self.plotGen2MF2D("Headache Membership Functions",[SlightlyUMF, SlightlyLMF, MildUMF, MildLMF, SevereUMF, SevereLMF], self.headache.getDomain(), 200)
        # self.plotGen2MF2D("Age Membership Functions",[YoungUMF, YoungLMF, MidUMF, MidLMF, OldUMF, OldLMF], self.age.getDomain(), 200)
        # self.plotT1MFs("Urgency Membership Functions",[LowUMF, MediumUMF, HighUMF, CriticalUMF, EmergencyUMF], self.urgency.getDomain(), 200)
        

        if not unit:
            self.plot.show()

    def Result(self,temperture_level, headache_level, age_level) -> None:
        """Calculate the output based on the two inputs"""
        self.temperature.setInput(temperture_level)
        self.headache.setInput(headache_level)
        self.age.setInput(age_level)

        print("Patient's Temperture was: "+str(self.temperature.getInput()))
        print("Patient's Headache Level was: "+str(self.headache.getInput()))
        print("Patient's Age was: "+str(self.age.getInput()))
        print("Using height center of sets type reduction, the zSlices based general type-2 FLS recommends a "
                + "urgency of: "+str(self.rulebase.evaluate(0)[self.urgency]))
        print("Using centroid type reduction, the zSlices based general type-2 FLS recommends a"
                + "urgency of: "+str(self.rulebase.evaluate(1)[self.urgency]))
        
        # print("Centroid of the output for TIP (based on centroid type reduction):")
        # centroid = self.rulebase.evaluateGetCentroid(1)
        # centroidUrgency = list(centroid[self.urgency])
        # centroidUrgencyXValues = centroidUrgency[0]
        # centroidUrgencyYValues = centroidUrgency[1]
        # for zLevel in range(len(centroidUrgencyXValues)):
        #     print(centroidUrgencyXValues[zLevel].toString()+" at y= "+str(centroidUrgencyYValues[zLevel]))


    def plotT1MFs(self,name,sets,xAxisRange,discretizationLevel):
        """Plot the lines for each membership function of the sets"""
        self.plot.figure()
        self.plot.title(name)
        for i in range(len(sets)):
            self.plot.plotMF(name.replace("Membership Functions",""),sets[i].getName(),sets[i],discretizationLevel,xAxisRange,Tuple(0.0,1.05),False)
        self.plot.legend()

    def plotGen2MF2D(self, name, sets, xAxisRange, discretizationLevel):
        """Plot the lines for each membership function of the sets"""
        self.plot.figure()
        self.plot.title(name)
        
        
        for i in range(0, len(sets), 2): 
            upper_set = sets[i] 
            lower_set = sets[i+1] 
            
            # plot the upper membership function
            self.plot.plotMF(name.replace("Membership Functions",""), upper_set.getName(), upper_set, discretizationLevel, xAxisRange, Tuple(0.0, 1.05),False)
            
            # plot the lower membership function
            self.plot.plotMF(name.replace("Membership Functions",""), lower_set.getName(), lower_set, discretizationLevel, xAxisRange, Tuple(0.0, 1.05),False)
            
            x = self.plot.discretize(upper_set.getSupport(), discretizationLevel)
            y_upper = [upper_set.getFS(xi) for xi in x]
            y_lower = [lower_set.getFS(xi) for xi in x]
            
            # fill the area between the upper and lower membership functions
            plt.fill_between(x, y_upper, y_lower, color='gray', alpha=0.5)  # Adjust color and transparency

        self.plot.legend()



    def plotGen2MF3D(self,name,sets,xAxisRange,discretizationLevel,plotAsLines,plotAsSurface):
        """Plot the lines for each membership function of the sets"""
        if plotAsLines:
            self.plot.figure3d()
            self.plot.title(name)
            for i in range(len(sets)):
                self.plot.plotMFasLines(sets[i],discretizationLevel)
        if plotAsSurface:
            self.plot.figure3d()
            self.plot.title(name)
            for i in range(len(sets)):
                self.plot.plotMFasSurface(sets[i].getName(),sets[i],xAxisRange,discretizationLevel,False)
            
if __name__ == "__main__":
        Case1()