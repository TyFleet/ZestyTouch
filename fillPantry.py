import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import io
import os
import sys
import re


#Return the name of product 
def productName(product):
    productName = product.find_all('td')[1]
    if(productName == None):
        productName = "Product not found"
    else:
        productName = str(productName)
        startN = productName.find("<b>Commercial name</b>")+len("<b>Commercial name</b>")
        endN = productName.find("<br>")
        resultName = productName[startN:endN]
        resultName = resultName[3:-177]
    return resultName

#Returns amount of product
def productAmount(product):
    productAmount = product.find_all('td')[1]
    if(productAmount == None):
        productAmount = "Amount not found"
    else:
        productAmount = str(productAmount)
        startA = productAmount.find("<b>Weight</b>")+len("<b>Weight</b>")
        endA = productAmount.find("<br>")
        resultAmount = productAmount[startA:endA]
        resultAmount = resultAmount[60:-10]
    return resultAmount


#Returns URL for image of the product
def productPic(product):
    productPic = product.find('img', attrs={'itemprop':'image'})
    if(productPic == None):
        productPic = "Image not found"
    else:
        productP = productPic['src'] 
    return productP

#http://product-open-data.com/gtin/
start = "http://product-open-data.com/gtin/"
search = [] #array for UPC codes received
#Receive UPC input from C# script
search = str(sys.argv)
for s in search:
    #Test that website is accessable 
    try:
        page = requests.get(start+s, timeout=10)
    except requests.exceptions.Timeout:
        print("Timeout has occured.")
        
    soup = BeautifulSoup(page.content, 'html.parser')
    product = soup.find_all('div', attrs={'class':'container'})[2]
    resultPic = productPic(product)
    resultName = productName(product)
    resultAmount = productAmount(product)
    
    #Print results to console to check results
    print(search[0])
    print(resultPic)
    print(resultName)
    print(resultAmount)
    
