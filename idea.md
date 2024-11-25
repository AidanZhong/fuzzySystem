 we will use bulit-in function

input: temperature(24 C to 44 C),severity of headache(0 to 10), age (0-130) 

https://en.wikipedia.org/wiki/Human_body_temperature (the lowest and highest temperature for a human body)


temperature: hot(37-39, after 39 1.0 degree), cold (34 - 36.5, before 36.1), normal (36 - 37.5, peak 36.5 -37)

https://medlineplus.gov/ency/article/001982.htm (normal temperature refs)

---------

headache: no pain*(0), mild headache(peak is 0-3, end in 10), severe headache(peak is 7-10,start in 0)

*no pain no sure to use

-------

age: young(peak 0 - 20, end in 40), mid-age(start in 25, peak 35 - 50, end at 65), old(start in 50, peak 80 - 130)

https://www.empower.com/the-currency/life/what-is-the-average-retirement-age (end of middle age refs)
------


output: degree of urgency (0 - 100)

Healthy(peak 0, end 30), mild Severe(start in 20, peak 50 , end 80), Severe(peak 100, end 70)

--------

27 Rules

| temperature | headache | age | urgency |
|-------------|----------|-----|---------|
|0|0|0|0|
|0|0|1|0|
|0|0|2|0|
|0|1|0|1|
|0|1|1|2|
|0|1|2|3|
|0|2|0|2|
|0|2|1|3|
|0|2|2|4|
|1|0|0|1|
|1|0|1|2|
|1|0|2|3|
|1|1|0|2|
|1|1|1|3|
|1|1|2|4|
|1|2|0|3|
|1|2|1|4|
|1|2|2|5|
|2|0|0|2|
|2|0|1|3|
|2|0|2|4|
|2|1|0|3|
|2|1|1|4|
|2|1|2|5|
|2|2|0|4|
|2|2|1|5|
|2|2|2|6|

# todos
week1 (8/11 - 14/11)
- [x] age -> type 2  -- Leo 
- [x] do research on headache. Adjust Linguistic terms, determine type1 or type2  -- Aidan
- [x] temperature, find the evidence  -- Aidan
- [x] skfuzzy -> JuzzyPython (case 1) -- Leo 
week2 (15/11 - 21/11)
- [x] urgency, find the evidence. But we have backup statement -- Leo
- [x] Adjust Rulebase - Leo
- [x] interval input (case 2) -- Aidan
- [x] create same sample data -- Leo 
week3 (22/11 - 26/11)
- [ ] finish the report

# Juzzy lib resources
https://github.com/LUCIDresearch/JuzzyPython/tree/main

# Age refs
young upper:
https://www.cdc.gov/mmwr/volumes/70/wr/mm7025e2.htm

young lower:
https://ils.unc.edu/courses/2020_fall/inls558_001/adultdevelopment.pdf

mid upper: 
https://dictionary.cambridge.org/dictionary/english/middle-age

mid lower: 
https://www.britannica.com/science/middle-age

old upper:
https://www.myguideforseniors.com/what-age-is-considered-senior-citizen/2020_fall

old lower:
https://pubmed.ncbi.nlm.nih.gov/1727842/

Age:
https://onlinelibrary.wiley.com/doi/full/10.1111/sji.12413

# urgency
https://www.england.nhs.uk/guidance-for-emergency-departments-initial-assessment/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5412135/
https://www.who.int/health-topics/adolescent-health#tab=tab_1
https://en.wikipedia.org/wiki/Age_of_majority

# headache
https://www.elsevier.es/en-revista-neurologia-english-edition--495-articulo-headache-what-ask-how-examine-S2173580821000134
https://link.springer.com/article/10.1186/s12873-018-0189-y?fromPaywallRec=false

# Temperature
https://www.nhs.uk/conditions/fever-in-adults/
https://my.clevelandclinic.org/health/diseases/21164-hypothermia-low-body-temperature
https://health.clevelandclinic.org/body-temperature-what-is-and-isnt-normal


# Data sample
1. T = 36.5, H = 0, A = 25
2. T = 36.5, H = 0, A = 100

3. T = 38, H = 0, A = 25
4. T = 38, H = 0, A = 70

5. T = 36.5, H = 6, A = 40
6. T = 36.5, H = 6, A = 70

7. T = 30, H = 0, A = 10
8. T = 30, H = 0, A = 55

9. T = 27, H = 9, A = 25
10. T = 36.5, H = 2, A = 60


