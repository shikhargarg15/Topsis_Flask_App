# TOPSIS Web App for Multiple-Criteria Decision Making
Project By: **Shikhar Garg**

[Click here](http://sgarg8.pythonanywhere.com/) to view the site.

# Introduction

**What is TOPSIS?**

Technique for Order of Preference by Similarity to Ideal Solution(TOPSIS) is a multi-criteria decision analysis method. It is a method of compensatory aggregation that compares a set of alternatives by identifying weights for each criterion, normalising scores for each criterion and calculating the geometric distance between each alternative and the ideal alternative, which is the best score in each criterion.

The webiste takes the csv file as first input.

Sample Dataset -

Model | Correlation | R<sup>2</sup> | RMSE | Accuracy
------------ | ------------- | ------------ | ------------- | ------------
M1 |	0.79 | 0.62	| 1.25 | 60.89
M2 |  0.66 | 0.44	| 2.89 | 63.07
M3 |	0.56 | 0.31	| 1.57 | 62.87
M4 |	0.82 | 0.67	| 2.68 | 70.19
M5 |	0.75 | 0.56	| 1.3	 | 80.39

It then takes comma-separated impacts for each feature with (+) denoting the positive impact and (-) denoting the negative impact.
It then takes comma-separated weights for each feature.

## Output

```
Model   Topsis Score    Rank
-----  --------  ----
  M1    0.772      2
  M2    0.225      5
  M3    0.438      4
  M4    0.523      3
  M5    0.811      1
```

The rankings are displayed in this form, with the 1st rank offering us the best decision, and last rank offering the worst decision making, according to TOPSIS method.
 
# Tools & Technologies Used
* Python
* HTML
* CSS
* Pandas
* Flask
