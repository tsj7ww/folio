# Covid19 Analysis
Basic analysis of Covid19 data sources from Johns Hopkins and blended with various demographics datasets.

### Overview
- Problem: create a model to forecast Covid19 deaths.
- Factors
  - IVs
    - (+ opportunities) Population
    - (- risk factor) County size (acreage)
      - Higher population density will make transmission harder to avoid (e.g. NYC)
      - Correlated with population? Eliminate this by just using the acreage in a geographic location?
    - (+ risk factor) % population undergoing hardship
        - Potential variables: % pop under US poverty line, % pop unemployed, ...
    - (- risk factor) Covid19 tests per 1,000 population
      - More tests per residents in population suggested an increased awareness and emphasis on reducing transmission
      - Reasonable to believe that this would be a proxy for the ideal input - degree of Covid19 restrictions in a geographical area
  - DV
    - Covid19 deaths per week by county

### Tech
...

### Data Sources

##### Johns Hopkins University
...

##### AWS Covid19 Data Lake
...

##### US Census Bureau
...

### Preprocessing
...

### Analysis

##### Viz
...

##### Prediction
...

---

### ToDo
1. ...
