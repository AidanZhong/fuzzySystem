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
- [x] age -> type 2  -- Leo 
- [x] do research on headache. Adjust Linguistic terms, determine type1 or type2  -- Aidan
- [x] temperature, find the evidence  -- Aidan
- [ ] urgency, find the evidence. But we have backup statement -- Leo
- [x] skfuzzy -> JuzzyPython   -- Leo 
- [ ] Adjust Rulebase - Leo
- [ ] interval input -- Aidan
- [ ] example data -- Leo 


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

urgency:
https://www.england.nhs.uk/guidance-for-emergency-departments-initial-assessment/

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

# Interval input
suppose the input is the range of [a,b]
treat the range as a set of points. Consider each point is a crispy input.
For each crispy input, compute the degree of membership function to the fuzzy system.
Aggregate the membership values of all points in the interval, using:
1. Maximum membership
2. Average membership
3. Integration
Use the aggregated value into the inference system

suppose range is [a,b], and for crispy input of a and b, the membership value will be[a_l, a_u] and [b_l, b_u]

- if the peak point is inside of the range, output should be [min(a_l, b_l), 1]
- otherwise, output should be [min(a_l, b_l), max(a_u, b_u)]

downside: if the distribution is not normal(maybe 99% of almost 0 membership value, but 1% have high membership, the upper bound of the range is still 1)