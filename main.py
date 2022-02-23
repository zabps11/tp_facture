#TODO

#L'objectif de ce mini TP consite en la génération d'une facture.
import copy
from math import prod
productTemp={
    "name":"",
    "price":0,
    "quantity":0
}
productList=[]


print("_____Entrer liste e produit_______")
newProduct=""
while newProduct != "n":
    productTemp["name"]= input("==> Name :  ")
    productTemp["price"]= float(input("    Price :  "))
    productTemp["quantity"]= int(input("    Quantity :  "))
    newProduct=input("Enter a new product ? y/n__  ")
    curentProduct=copy.deepcopy(productTemp)
    productList.append(curentProduct)
    print("----------------------------------------------")
    while newProduct!="y" and newProduct!= "n":
        newProduct=input("Enter a new product ? y/n")
    
totalPrice=0
print("_______________________FACTURE_________________________")
for product in productList:
    print("     Name : {}    Quantity : {}  Price :  {}".format(product["name"],product["quantity"],product["price"]))
    totalPrice=totalPrice + product["quantity"]*product["price"]
print("     TOTAL : {}".format(totalPrice))