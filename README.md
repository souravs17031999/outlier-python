# outlier-python

# Package Description :
Python package for Outlier Removal Algorithm using z_score or iqr.   
# Motivation :   
This is a part of project - II made for UCS633 - Data analytics and visualization at TIET.     
@Author : Sourav Kumar    
@Roll no. : 101883068    
# Algorithm :       
* Z-SCORE : If the population mean and population standard deviation are known, the standard score of a raw score x is calculated as:     
z = (x - mean) / std.          
mean : is the mean of the sample.     
std : is the standard deviation of the sample.    

* Interquartile range : interquartile range (IQR), also called the midspread, middle 50%, or H‑spread, is a measure of statistical dispersion, being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles.     
IQR = Q3 −  Q1       
The IQR of a set of values is calculated as the difference between the upper and lower quartiles, Q3 and Q1. Each quartile is a median calculated as follows :     
Given an even 2n or odd 2n+1 number of values.      
first quartile Q1 = median of the n smallest values          
third quartile Q3 = median of the n largest values       
The second quartile Q2 is the same as the ordinary median.        

### Getting started Locally :  
> Run On Terminal       
```python -m outlier.outlier inputFilePath outputFilePath z_score```     
or
```python -m outlier.outlier inputFilePath outputFilePath iqr```       
ex. python -m outlier outlier C:/Users/DELL/Desktop/train.csv C:/Users/DELL/Desktop/output.csv z_score     

> Run In IDLE   
```from outlier import outlier```   
```o = outlier.outlier(inputFilePath, outputFilePath)```     
```o.outlier_main('z_score')```
or    
```o.outlier_main('iqr')```     

> Run on Jupyter   
Open terminal (cmd)   
```jupyter notebook```   
Create a new python3 file.     
```from outlier import outlier```   
```o = outlier.outlier(inputFilePath, outputFilePath)```
```o.outlier_main('z_score')```
or    
```o.outlier_main('iqr')```       

* NOTE : ```outlier_main()``` doesn't necessarily require any ```method``` argument , if no argument is provided, it uses ```z_score``` by default as the algorithm for removal of outliers from the dataset.    
* The algorithm only reports missing data containing columns and not handles them, it assumes that it has been handled already.   
Also in case of z-score method, it will not affect much, but it may be possible to give wrong output in case of IQR if missing values are found.    
### OUTPUT :
Removes all the valid rows contaning outlier values from the dataset and prints the number of rows removed along with the columns which were considered for the algorithm.    
Also , the final dataframe will be written to the output file path you provided.
 
![output result on jupyter](/test_images/t.JPG)
![output result on idle](/test_images/t1.JPG)
![output result on cmd](/test_images/t2.JPG) 

# TESTING : 
* The package has been extensively tested on various datasets consisting varied types of expected and unexpected input data and any preprocessing , if required has been taken care of.

