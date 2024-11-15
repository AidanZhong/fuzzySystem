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
- [x] do research on headache. Adjust Linguistic terms, determine type1 or type2  -- Aidan
- [x] temperature, find the evidence  -- Aidan
- [ ] urgency, find the evidence. But we have backup statement (Optional)
- [ ] skfuzzy -> JuzzyPython   -- Leo

## headache research
Subjective, so need type2 fuzzy set!
1. Visual Analog Scale (VAS)

	•	A simple scale where patients rate their headache intensity on a scale of 0 to 10, with:
	•	0: No pain
	•	10: Worst possible pain
	•	This is subjective but widely used to understand the patient’s perception of pain.

2. Numeric Rating Scale (NRS)

	•	Similar to VAS but uses integers (e.g., 0–10 or 0–100) to rate the pain.
	•	Commonly used in clinical and research settings for simplicity.

3. Headache Diaries

	•	Patients record details about their headaches, including:
	•	Intensity
	•	Frequency
	•	Duration
	•	Triggers
	•	Medication usage
	•	Useful for identifying patterns and treatment efficacy.

4. Headache Impact Test (HIT-6)

	•	A questionnaire assessing the impact of headaches on daily life, including:
	•	Social functioning
	•	Work productivity
	•	Emotional well-being
	•	Scores range from 36 to 78, with higher scores indicating greater impact.

5. Migraine Disability Assessment Test (MIDAS)

	•	Focuses on the disability caused by migraines.
	•	Patients answer questions about missed work or school, reduced productivity, and missed social events due to migraines over the past 3 months.
	•	The score categorizes the level of disability (mild, moderate, or severe).

6. International Classification of Headache Disorders (ICHD)

	•	A diagnostic tool by the International Headache Society (IHS).
	•	Helps classify headaches into primary (e.g., migraine, tension-type headache) and secondary types based on specific criteria.

7. Pain Quality Assessment Scale (PQAS)

	•	Evaluates the quality of headache pain (e.g., throbbing, stabbing, dull).
	•	Useful for understanding the nature of the pain.

8. Functional Disability Scale (FDS)

	•	Assesses how much headaches interfere with daily activities (e.g., personal care, work, leisure).

Objective Measurements (Rare)

Although headaches are subjective, in some cases, objective measurements like neuroimaging (MRI/CT) or EEG may help identify underlying causes, particularly for secondary headaches due to structural or neurological issues.

These methods are often combined to provide a comprehensive understanding of the headache and guide treatment plans effectively.

## temperature evidence

Normal Body Temperature: [link](https://health.clevelandclinic.org/body-temperature-what-is-and-isnt-normal)

-	Average Range: Traditionally, the average normal body temperature is considered to be 98.6°F (37°C). However, recent studies suggest that the average body temperature has decreased over time, with current averages around 97.5°F to 97.9°F (36.4°C to 36.6°C). (Cleveland Clinic Health)
-	Measurement Variations:
-	Oral: Approximately 97.8°F (36.6°C). (Healthgrades Resources)
-	Rectal: Slightly higher than oral readings, around 98.6°F (37°C).
-	Axillary (underarm): Slightly lower than oral readings, around 96.8°F (36°C).

Cold (Hypothermia): [link](https://www.uptodate.com/contents/hypothermia-the-basics)

-	Definition: Hypothermia occurs when body temperature drops below 95°F (35°C). (UpToDate)
-	Severity Levels:
-	Mild Hypothermia: 32°C to 35°C (89.6°F to 95°F). (MSD Manuals)
-	Moderate Hypothermia: 28°C to 32°C (82.4°F to 89.6°F).
-	Severe Hypothermia: Below 28°C (82.4°F).

Hot (Fever and Hyperthermia): [link](https://www.webmd.com/first-aid/normal-body-temperature)

-	Fever: Generally defined as a body temperature above 100.4°F (38°C). (WebMD)
-	Hyperthermia: An abnormally high body temperature not caused by a fever, often due to external factors like heat exposure. Hyperthermia can be classified as:
-	Mild: 37.5°C to 38°C (99.5°F to 100.4°F).
-	Moderate: 38.1°C to 38.5°C (100.6°F to 101.3°F).
-	Severe: Above 38.5°C (101.3°F). (EmCrit)