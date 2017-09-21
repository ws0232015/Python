&copy; Copyright for Shuang Wu 2017<br>
Cite from the DataCamp website<br>
**Do not cite this notebook in any situation**<br>
Persenoal reference only, **do not copy** the code or others
- [Tidy data](#tidy-data)
    - [Recognizing tidy data](#recognizing-tidy-data)
    - [Reshaping your data using melt](#reshaping-your-data-using-melt)
    - [Customizing melted data](#customizing-melted-data)


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