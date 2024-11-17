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

class Case1:
    def __init__(self,unit = False) -> None:
        self.numberOfzLevels = 8

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
        
        NormalUMF = T1MF_Trapezoidal("Upper MF for normal temperature", [35.0, 36.4, 36.6, 38.0])
        NormalLMF = T1MF_Trapezoidal("Lower MF for normal temperature", [35.001, 36.4, 36.6, 38.0])
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
        
        MildHUMF = T1MF_Gaussian("Upper MF for mild headache", 5.0, 1)
        MildHLMF = T1MF_Gaussian("Lower MF for mild headache", 5.0, 0.5)
        MildHIT2MF = IntervalT2MF_Gaussian("IT2MF for mild headache",MildHUMF,MildHLMF)
        MildHMF = GenT2MF_Gaussian("GT2MF for mild headache", primer = MildHIT2MF, numberOfzLevels = self.numberOfzLevels)
        
        SevereHUMF = T1MF_Trapezoidal("Upper MF for severe headache", [5.0, 7.0, 10.0, 10.0])
        SevereHLMF = T1MF_Trapezoidal("Lower MF for severe headache", [5.0, 8.0, 10.0, 10.0])
        SevereHIT2MF = IntervalT2MF_Trapezoidal("IT2MF for severe headache",SevereHUMF,SevereHLMF)
        SevereHMF = GenT2MF_Trapezoidal("GT2MF for severe headache", primer = SevereHIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Age
        YoungUMF = T1MF_Trapezoidal("Upper MF for young age", [0.0, 0.0, 22.0, 45.0])
        YoungLMF = T1MF_Trapezoidal("Lower MF for young age", [0.0, 0.0, 17.0, 40.0])
        YoungIT2MF = IntervalT2MF_Trapezoidal("IT2MF for young age",YoungUMF,YoungLMF)
        YoungMF = GenT2MF_Trapezoidal("GT2MF for young age", primer = YoungIT2MF, numberOfzLevels = self.numberOfzLevels)

        MidUMF = T1MF_Trapezoidal("Upper MF for mid age", [40.0, 45.0, 60.0, 65.0])
        MidLMF = T1MF_Trapezoidal("Lower MF for mid age", [45.0, 45.0, 60.0, 60.0])
        MidIT2MF = IntervalT2MF_Trapezoidal("IT2MF for mid age",MidUMF,MidLMF)
        MidMF = GenT2MF_Trapezoidal("GT2MF for mid age", primer = MidIT2MF, numberOfzLevels = self.numberOfzLevels)

        OldUMF = T1MF_Trapezoidal("Upper MF for old age", [60.0, 70.0, 130.0, 130.0])
        OldLMF = T1MF_Trapezoidal("Lower MF for old age", [65.0, 70.0, 130.0, 130.0])
        OldIT2MF = IntervalT2MF_Trapezoidal("IT2MF for old age",OldUMF,OldLMF)
        OldMF = GenT2MF_Trapezoidal("GT2MF for old age", primer = OldIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Urgency
        number_of_labels = 5
        seg = 100 / (2 * number_of_labels - 1)
        StableUMF = T1MF_Trapezoidal("Upper MF for stable level", [0.0, 0.0, seg+0.001, 2 * seg])
        StableLMF = T1MF_Trapezoidal("Lower MF for stable level", [0.0, 0.0, seg, 2 * seg])
        StableIT2MF = IntervalT2MF_Trapezoidal("IT2MF for stable level",StableUMF,StableLMF)
        StableMF = GenT2MF_Trapezoidal("GT2MF for stable level", primer = StableIT2MF, numberOfzLevels = self.numberOfzLevels)

        MildUMF = T1MF_Trapezoidal("Upper MF for mild level", [seg, 2 * seg, 3 * seg+0.001, 4 * seg])
        MildLMF = T1MF_Trapezoidal("Lower MF for mild level", [seg, 2 * seg, 3 * seg, 4 * seg])
        MildIT2MF = IntervalT2MF_Trapezoidal("IT2MF for mild level",MildUMF,MildLMF)
        MildMF = GenT2MF_Trapezoidal("GT2MF for mild level", primer = MildIT2MF, numberOfzLevels = self.numberOfzLevels)

        ModerateUMF = T1MF_Trapezoidal("Upper MF for moderate level", [3 * seg, 4 * seg, 5 * seg+0.001, 6 * seg])
        ModerateLMF = T1MF_Trapezoidal("Lower MF for moderate level", [3 * seg, 4 * seg, 5 * seg, 6 * seg])
        ModerateIT2MF = IntervalT2MF_Trapezoidal("IT2MF for moderate level",ModerateUMF,ModerateLMF)
        ModerateMF = GenT2MF_Trapezoidal("GT2MF for moderate level", primer = ModerateIT2MF, numberOfzLevels = self.numberOfzLevels)

        SeriousUMF = T1MF_Trapezoidal("Upper MF for serious level", [5 * seg, 6 * seg, 7 * seg+0.001, 8 * seg])
        SeriousLMF = T1MF_Trapezoidal("Lower MF for serious level", [5 * seg, 6 * seg, 7 * seg, 8 * seg])
        SeriousIT2MF = IntervalT2MF_Trapezoidal("IT2MF for serious level",SeriousUMF,SeriousLMF)
        SeriousMF = GenT2MF_Trapezoidal("GT2MF for serious level", primer = SeriousIT2MF, numberOfzLevels = self.numberOfzLevels)

        SevereUMF = T1MF_Trapezoidal("Upper MF for severe level", [7 * seg, 8 * seg, 9 * seg+0.001, 10 * seg])
        SevereLMF = T1MF_Trapezoidal("Lower MF for severe level", [7 * seg, 8 * seg, 9 * seg, 10 * seg])
        SevereIT2MF = IntervalT2MF_Trapezoidal("IT2MF for severe level",SevereUMF,SevereLMF)
        SevereMF = GenT2MF_Trapezoidal("GT2MF for severe level", primer = SevereIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Life_threateningUMF = T1MF_Trapezoidal("Upper MF for life_threatening level", [9 * seg, 10 * seg, 11 * seg+0.001, 12 * seg])
        # Life_threateningLMF = T1MF_Trapezoidal("Lower MF for life_threatening level", [9 * seg, 10 * seg, 11 * seg, 12 * seg])
        # Life_threateningIT2MF = IntervalT2MF_Trapezoidal("IT2MF for life_threatening level",Life_threateningUMF,Life_threateningLMF)
        # Life_threateningMF = GenT2MF_Trapezoidal("GT2MF for life_threatening level", primer = Life_threateningIT2MF, numberOfzLevels = self.numberOfzLevels)

        # CriticalUMF = T1MF_Trapezoidal("Upper MF for critical level", [11 * seg, 12 * seg, 13 * seg+0.001, 13 * seg])
        # CriticalLMF = T1MF_Trapezoidal("Lower MF for critical level", [11 * seg, 12 * seg, 13 * seg, 13 * seg])
        # CriticalIT2MF = IntervalT2MF_Trapezoidal("IT2MF for critical level",CriticalUMF,CriticalLMF)
        # CriticalMF = GenT2MF_Trapezoidal("GT2MF for critical level", primer = CriticalIT2MF, numberOfzLevels = self.numberOfzLevels)

        # Set up the antecedents and consequents
        # Temperature
        Cold = GenT2_Antecedent("cold temperature", ColdMF, self.temperature)
        Normal = GenT2_Antecedent("normal temperature", NormalMF, self.temperature)
        Hot = GenT2_Antecedent("hot temperature", HotMF, self.temperature)

        # Headache
        Slightly = GenT2_Antecedent("no headache", SlightlyMF, self.headache)
        MildH = GenT2_Antecedent("mild headache", MildHMF, self.headache)
        SevereH = GenT2_Antecedent("severe headache", SevereHMF, self.headache)

        # Age
        Young = GenT2_Antecedent("young age", YoungMF, self.age)
        Mid = GenT2_Antecedent("mid age", MidMF, self.age)
        Old = GenT2_Antecedent("old age", OldMF, self.age)

        # Urgency
        Stable =  GenT2_Consequent("Stable", StableMF, self.urgency)
        Mild =  GenT2_Consequent("Mild", MildMF, self.urgency)
        Moderate =  GenT2_Consequent("Moderate", ModerateMF, self.urgency)
        Serious =  GenT2_Consequent("Serious",  SeriousMF, self.urgency)
        Severe =  GenT2_Consequent("Severe",  SevereMF, self.urgency)
        # Life_threatening =  GenT2_Consequent("Life_threatening",  Life_threateningMF, self.urgency)
        # Critical =  GenT2_Consequent("Critical",  CriticalMF, self.urgency)
        
        
        # Set up the rulebase and add rules
        self.rulebase = GenT2_Rulebase()
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Young], consequent = Stable)) #Rule 1
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Mid], consequent = Stable)) #Rule 2
        self.rulebase.addRule(GenT2_Rule([Normal, Slightly, Old], consequent = Stable)) #Rule 3
        self.rulebase.addRule(GenT2_Rule([Normal, MildH, Young], consequent = Mild)) # Rule 4
        self.rulebase.addRule(GenT2_Rule([Normal, MildH, Mid], consequent = Mild)) # Rule 5
        self.rulebase.addRule(GenT2_Rule([Normal, MildH, Old], consequent = Moderate)) # Rule 6
        self.rulebase.addRule(GenT2_Rule([Normal, SevereH, Young], consequent = Moderate)) # Rule 7
        self.rulebase.addRule(GenT2_Rule([Normal, SevereH, Mid], consequent = Moderate)) # Rule 8
        self.rulebase.addRule(GenT2_Rule([Normal, SevereH, Old], consequent = Severe)) # Rule 9
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Young], consequent = Mild)) # Rule 10
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Mid], consequent = Mild)) # Rule 11
        self.rulebase.addRule(GenT2_Rule([Hot, Slightly, Old], consequent = Moderate)) # Rule 12
        self.rulebase.addRule(GenT2_Rule([Hot, MildH, Young], consequent = Moderate)) # Rule 13
        self.rulebase.addRule(GenT2_Rule([Hot, MildH, Mid], consequent = Moderate)) # Rule 14
        self.rulebase.addRule(GenT2_Rule([Hot, MildH, Old], consequent = Serious)) # Rule 15
        self.rulebase.addRule(GenT2_Rule([Hot, SevereH, Young], consequent = Serious)) # Rule 16
        self.rulebase.addRule(GenT2_Rule([Hot, SevereH, Mid], consequent = Severe)) # Rule 17
        self.rulebase.addRule(GenT2_Rule([Hot, SevereH, Old], consequent = Severe)) # Rule 18
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Young], consequent = Moderate)) # Rule 19
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Mid], consequent = Moderate)) # Rule 20
        self.rulebase.addRule(GenT2_Rule([Cold, Slightly, Old], consequent = Serious)) # Rule 21
        self.rulebase.addRule(GenT2_Rule([Cold, MildH, Young], consequent = Serious)) # Rule 22
        self.rulebase.addRule(GenT2_Rule([Cold, MildH, Mid], consequent = Serious)) # Rule 23
        self.rulebase.addRule(GenT2_Rule([Cold, MildH, Old], consequent = Severe)) # Rule 24
        self.rulebase.addRule(GenT2_Rule([Cold, SevereH, Young], consequent = Severe)) # Rule 25
        self.rulebase.addRule(GenT2_Rule([Cold, SevereH, Mid], consequent = Severe)) # Rule 26
        self.rulebase.addRule(GenT2_Rule([Cold, SevereH, Old], consequent = Severe)) # Rule 27

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

        

        self.Result(Patienttemperature,Patientheadache,Patientage)
        # self.Result(36.5,0,25)
        # self.Result(36.5,0,100)
        # self.Result(38,0,25)
        # self.Result(38,0,70)
        # self.Result(36.5,6,40)
        # self.Result(36.5,6,70)
        # self.Result(30,0,10)
        # self.Result(30,0,55)
        # self.Result(27,9,25)
        # self.Result(36.5,2,60)


        # Plot the MF
        self.plotMFs("Temperature Membership Functions",[HotMF, ColdMF, NormalMF], self.temperature.getDomain(), 100, True, True)
        self.plotMFs("Headache Membership Functions",[SlightlyMF, MildHMF, SevereHMF], self.headache.getDomain(), 100, True, True)
        self.plotMFs("Age Membership Functions",[YoungMF, MidMF, OldMF], self.age.getDomain(), 100, True, True)
        self.plotMFs("Urgency Membership Functions",[StableMF, MildMF, ModerateMF, SeriousMF, SevereMF], self.urgency.getDomain(), 100, True, True)
        
        

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
        
        print("Centroid of the output for TIP (based on centroid type reduction):")
        centroid = self.rulebase.evaluateGetCentroid(1)
        centroidUrgency = list(centroid[self.urgency])
        centroidUrgencyXValues = centroidUrgency[0]
        centroidUrgencyYValues = centroidUrgency[1]
        for zLevel in range(len(centroidUrgencyXValues)):
            print(centroidUrgencyXValues[zLevel].toString()+" at y= "+str(centroidUrgencyYValues[zLevel]))
    
    def plotMFs(self,name,sets,xAxisRange,discretizationLevel,plotAsLines,plotAsSurface):
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