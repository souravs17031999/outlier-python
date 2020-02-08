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
  

> Run In IDLE   


> Run on Jupyter   
Open terminal (cmd)   
```jupyter notebook```   
Create a new python3 file.     


* ```topsis_main()``` has been specifically designed to inhibit leakeage of inbuilt functions.  
* ```topsis_main(debug=True)``` use this to display all the intermediate matrices.   
* Make sure that ```filename.csv``` is in same directory where package is installed.

### OUTPUT :
Removes all the valid rows contaning outlier values from the dataset and prints the number of rows removed along with the columns which were considered for the algorithm.    
 

# TESTING : 
* The package has been extensively tested on various datasets consisting varied types of expected and unexpected input data and any preprocessing , if required has been taken care of.

