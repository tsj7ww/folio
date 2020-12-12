# Baseball Analyis
Analysis on baseball data provided by Sean Lahman.
---

### Data Extract
[Extract data from SQLite database into zipped Apache Parquet files for storage in S3 and further processing.](./extract.ipynb)
1. ```select * from table``` into Pandas DataFrame
2. Save data to zipped (snappy?) Parquet file
3. Load table into S3
4. Repeat for all tables in the database

### Data Viz
[Graph the disparity in salary of Pitchers vs Catchers over time.][./viz.ipynb]
1. steps...
![Salary (USD in M) by Position over Time](./viz/salary_by_pos.svg)
