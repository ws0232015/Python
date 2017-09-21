
&copy; Copyright for Shuang Wu 2017<br>
Cite from the DataCamp website<br>
**Do not cite this notebook in any situation**<br>
Persenoal reference only, **do not copy** the code or others

- [Diagnose data for cleaning](#diagnose-data-for-cleaning)
    - [Loading and viewing data](#loading-and-viewing-data)
    - [Futher diagnosis](#futher-diagnosis)
- [Exploratory data analy](#exploratory-data-analy)
    - [Calculating summary statistics](#calculating-summary-statistics)
    - [Freq. counts for categorical data](#freq-counts-for-categorical-data)

# Diagnose data for cleaning

* Cleaning data
    * prepare data for analysis
    * data almost never comes in clean
    * diagnose data for cleaning
* Common data problems
    * inconsistent col. name
    * missing data
    * outliers
    * duplicate rows
    * untidy
    * need to process col.
    * col. types can single unexpected data val.
* Load data
    * panda
* Visually inspect
    * head and tail
    * columns
    * shape
    * info


## Loading and viewing data
* Load inspect the DataFrame
    * .head()
    * .tail()
    * .shape
    * .columns


```python
import pandas as pd
df = pd.read_csv('dob_job_application_filings_subset.csv')
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df_subset.head())
print(df_subset.tail())
```

## Futher diagnosis

* Unclear or missing data
    * .info()
        * provides info. about df
            * #of rows
            * #of cols
            * #of non-missing val in each col.
            * data type for each col
            * help check whether float or string
            * also check complete data or missing


```python
print(df.info())
print(df_subset.info())
```

# Exploratory data analy

* Freq. counts
    * count the # of unique values in our data
    * df.info()
    * dropna=False
* Summary statistics
    * numeric col.
    * outliers
        * considerably higher or lower
        * require further investigation
        
## Calculating summary statistics

* Use *.describe()* method to calculate summary statistics of the data
* Some columns like *Job#* are encoded as numeric col., but it does not make sense to compute summary statistics for such cols.
```python
df.describe()
```

## Freq. counts for categorical data

* *.describe()* can only be used on numeric cols. 
* *.value_counts()* can apply to categorical data
    * return the freq. counts for each unique val. in a col.
    * optional para. *dropna*
        * *True* by defalut
        * not give a freq. count for missing data in a col.
        * Set to *False* if missing in a col. and want to the freq. counts
```python {.input, n=1}
print(df['Borough'].value_counts(dropna=False))
print(df['State'].value_counts(dropna=False))
print(df['Site Fill'].value_counts(dropna=False))
```