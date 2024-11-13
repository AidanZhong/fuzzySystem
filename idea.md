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
- [ ] age -> type 2  -- Leo 
- [ ] do research on headache. Adjust Linguistic terms, determine type1 or type2  -- Aidan
- [ ] temperature, find the evidence  -- Aidan
- [ ] urgency, find the evidence. But we have backup statement (Optional)
- [ ] skfuzzy -> JuzzyPython   -- Leo

# Juzzy lib resources
https://github.com/LUCIDresearch/JuzzyPython/tree/main
