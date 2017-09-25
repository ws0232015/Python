&copy; Copyright for Shuang Wu 2017<br>
Cite from the DataCamp website<br>
**Do not cite this notebook in any situation**<br>
Persenoal reference only, **do not copy** the code or others
- [Tidy data](#tidy-data)
    - [Recognizing tidy data](#recognizing-tidy-data)
    - [Reshaping your data using melt](#reshaping-your-data-using-melt)
    - [Customizing melted data](#customizing-melted-data)
- [Pivoting data](#pivoting-data)
    - [Pivot data](#pivot-data)
    - [Resetting the index of a DataFrame](#resetting-the-index-of-a-dataframe)
    - [Pivoting duplicate values](#pivoting-duplicate-values)
- [Beyond melt and pivot](#beyond-melt-and-pivot)
    - [Splitting a col with _.str_](#splitting-a-col-with-str)
    - [Splitting a col w/ _.split()_ and _.get()_](#splitting-a-col-w-split-and-get)


# Tidy data

* Tidy data
    * Formalize the way we describle the shape of data
    * Gives us goal when formatting our data
    * Standard way to organize data val. within a dataset
* Principles of tidy data
    * cols represent separate variables
    * rows represent individual observations
    * Observational units form tables
* Converting to tidy data
    * Better for reporting vs. better for analysis
    * Tidy data makes it easier to fix common data problems
    * The data problem we are trying to fix:
        * Cols. containing values, instead of variables
    * solution: pd.melt()

## Recognizing tidy data

* For data to be tidy, must have:
    * Each variable as a separate col.
    * Each row as a separate obs.
* its important to be able to recognize tidy or untidy data

## Reshaping your data using melt

* Melting data is the process turning cols. of data into rows of data.
* *pd.melt()*
    * _id_vars_
        * represent the cocls. of the data you **do not** want to melt
    * _value_vars_
        * represent the cocls. of the data you **do** wish to melt into rows
    * by default, if no _value_vars_ are provided, all cols. not set in the _id_vars_ will be melted.
```python {.input}
print(airquality.head())
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'])
print(airquality_melt.head())
```

Index | Ozone | Solar.R | Wind | Temp | Month | Day
------|-------|---------|------|------|-------|----
0 | 41.0 | 190.0 | 7.4 | 67 | 5 | 1
1 | 36.0 | 118.0 | 8.0 | 72 | 5 | 2
2 | 12.0 | 149.0 | 12.6 | 74 | 5 | 3
3 | 18.0 | 313.0 | 11.5 | 62 | 5 | 4
4 | NaN | NaN | 14.3 | 56 | 5 | 5

Index | Month | Day | variable | value
------|-------|-----|----------|------
0 | 5 | 1 | Ozone | 41.0
1 | 5 | 2 | Ozone | 36.0
2 | 5 | 3 | Ozone | 12.0
3 | 5 | 4 | Ozone | 18.0
4 | 5 | 5 | Ozone | NaN

## Customizing melted data

* Have col. names more meaningful than _variable_ and _value_
* Can rename the _variable_ col. by specifying an arg. to the _var_name_ parameter, and the _value_ col. by specifying an arg. to the _value_name_ parameter

```python {.input}
print(airquality.head())
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')
print(airquality_melt.head())
```

Index | Ozone | Solar.R | Wind | Temp | Month | Day
------|-------|---------|------|------|-------|----
0 | 41.0 | 190.0 | 7.4 | 67 | 5 | 1
1 | 36.0 | 118.0 | 8.0 | 72 | 5 | 2
2 | 12.0 | 149.0 | 12.6 | 74 | 5 | 3
3 | 18.0 | 313.0 | 11.5 | 62 | 5 | 4
4 | NaN | NaN | 14.3 | 56 | 5 | 5

Index | Month | Day | measurement | reading
------|-------|-----|-------------|--------
0 | 5 | 1 | Ozone | 41.0
1 | 5 | 2 | Ozone | 36.0
2 | 5 | 3 | Ozone | 12.0
3 | 5 | 4 | Ozone | 18.0
4 | 5 | 5 | Ozone | NaN

# Pivoting data

* Pivot: un-melting data
    * Opposite of melting
    * In melting, we turned columns into rows
    * Pivoting: turn unique values into separate columns
    * Analysis friendly shape to reporting friendly shape
    * Violates tidy data principle: rows contain observations
        * Multiple variables stored in the same column
* Pivot table
    * Has a parameter that specifies how to deal w/ duplicate values
    * E.g.: can aggregate the duplicate values by taking their average

## Pivot data

* Pivoting data is the opposite of melting it. 
    * _.pivot_table()_ method
        * _index_ parameter
            * uese to specify the cols **dont** want pivoted
        * _columns_ parameter
            * the name of the col. want to pivot
        * _values_ parameter
            * the values to be used when the col is pivoted
    * While melting takes a set of columns and turns it into a single column, pivoting will create a new col. for each unique value in a specified col.

```python {.input}
print(airquality_melt.head())
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')
print(airquality_pivot.head())
```

Index | Month | Day | measurement | reading
------|-------|-----|-------------|--------
0 | 5 | 1 | Ozone | 41.0
1 | 5 | 2 | Ozone | 36.0
2 | 5 | 3 | Ozone | 12.0
3 | 5 | 4 | Ozone | 18.0
4 | 5 | 5 | Ozone | NaN

Index | measurement | Ozone | Solar.R | Temp | Wind
------|-------------|-------|---------|------|-----
Month | Day | 
5 | 1 | 41.0 | 190.0 | 67.0 | 7.4
 | 2 | 36.0 | 118.0 | 72.0 | 8.0
 | 3 | 12.0 | 149.0 | 74.0 | 12.6
 | 4 | 18.0 | 313.0 | 62.0 | 11.5
 | 5 | NaN | NaN | 56.0 | 14.3

 ## Resetting the index of a DataFrame

 * The previous table was a pandas DataFrame w/ a [hierarchical index ](http://pandas.pydata.org/pandas-docs/stable/advanced.html)(also known as a MultiIndex)
 * Hierarchical indexes are covered in depth in [Manipulating DataFrames w/ pandas](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas)
 * In essence, they allow to group cols. or rows by another variable
 * Method to get back to orginal DF
    * _.reset_index()_

```python {.input}
print(airquality_pivot.index)
airquality_pivot = airquality_pivot.reset_index()
print(airquality_pivot.index())
print(airquality_pivot.head())
```

    MultiIndex(levels=[[5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]],
               labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]],
               names=['Month', 'Day'])
    
    RangeIndex(start=0, stop=153, step=1)
measurement | Month | Day | Ozone | Solar.R | Temp | Wind
------------|-------|-----|-------|---------|------|-----
0 | 5 | 1 | 41.0 | 190.0 | 67.0 | 7.4
1 | 5 | 2 | 36.0 | 118.0 | 72.0 | 8.0
2 | 5 | 3 | 12.0 | 149.0 | 74.0 | 12.6
3 | 5 | 4 | 18.0 | 313.0 | 62.0 | 11.5
4 | 5 | 5 | NaN | NaN | 56.0 | 14.3

## Pivoting duplicate values

* Use pivot tables to deal w/ duplicate vals. by providing an aggregation func. through the _aggfunc_ parameter.
* Can not only reshape data, but also remove duplicates.
* Cam flatten the cols. of the pivoted DF using _.reset_index()_

```python {.input}
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)
airquality_pivot = airquality_pivot.reset_index()
print(airquality_pivot.head())
print(airquality.head())
```

measurement | Month | Day | Ozone | Solar.R | Temp | Wind
------------|-------|-----|-------|---------|------|-----
0 | 5 | 1 | 41.0 | 190.0 | 67.0 | 7.4
1 | 5 | 2 | 36.0 | 118.0 | 72.0 | 8.0
2 | 5 | 3 | 12.0 | 149.0 | 74.0 | 12.6
3 | 5 | 4 | 18.0 | 313.0 | 62.0 | 11.5
4 | 5 | 5 | NaN | NaN | 56.0 | 14.3

Index | Ozone | Solar.R | Wind | Temp | Month | Day
------|-------|---------|------|------|-------|----
0 | 41.0 | 190.0 | 7.4 | 67 | 5 | 1
1 | 36.0 | 118.0 | 8.0 | 72 | 5 | 2
2 | 12.0 | 149.0 | 12.6 | 74 | 5 | 3
3 | 18.0 | 313.0 | 11.5 | 62 | 5 | 4
4 | NaN | NaN | 14.3 | 56 | 5 | 5

# Beyond melt and pivot

* Beyond melt and pivot
    * Melting and pivoting are basic tools
    * Another common problem:
        * Cols. contain multiple bits of infomation
* Melting and parsing
    * Nothing inherently wrong about original data shape
    * Not conducive for analysis

## Splitting a col with _.str_

```python {.input}
tb_melt = pd.melt(tb, id_vars=['country', 'year'])
tb_melt['gender'] = tb_melt.variable.str[0]
tb_melt['age_group'] = tb_melt.variable.str[1:]
print(tb_melt.head())
```

Index | country | year | variable | value | gender | age_group
------|---------|------|----------|-------|--------|----------
0 | AD | 2000 | m014 | 0.0 | m | 014
1 | AE | 2000 | m014 | 2.0 | m | 014
2 | AF | 2000 | m014 | 52.0 | m | 014
3 | AG | 2000 | m014 | 0.0 | m | 014
4 | AL | 2000 | m014 | 2.0 | m | 014

## Splitting a col w/ _.split()_ and _.get()_

* Another common way multiple variables are stored in cols is with a delimiter
* Use python's built-in string method _.split()_
    * by default, this method will split a string into parts separated by a space
    * can specify the delimiter like _.split('\_')_

```python {.input}
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')
ebola_melt['str_split'] = ebola_melt['type_country'].str.split('_')
ebola_melt['type'] = ebola_melt['str_split'].str.get(0)
ebola_melt['country'] = ebola_melt['str_split'].str.get(1)
print(ebola_melt.head())
```

Index | Date | Day | type_country | counts | str_split | type | country
------|------|-----|--------------|--------|-----------|------|--------
0 | 1/5/2015 | 289 | Cases_Guinea | 2776.0 | [Cases, Guinea] | Cases | Guinea
1 | 1/4/2015 | 288 | Cases_Guinea | 2775.0 | [Cases, Guinea] | Cases | Guinea
2 | 1/3/2015 | 287 | Cases_Guinea | 2769.0 | [Cases, Guinea] | Cases | Guinea
3 | 1/2/2015 | 286 | Cases_Guinea | NaN | [Cases, Guinea] | Cases | Guinea
4 | 12/31/2014 | 284 | Cases_Guinea | 2730.0 | [Cases, Guinea] | Cases | Guinea