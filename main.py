#TODO

#L'objectif de ce mini TP consite en la génération d'une facture.
import copy

productTemp={
    "name":"",
    "price":0,
    "quantity":0
}
productList=[]


print("_____Entrer liste de produit_______")
newProduct=""
newFacture=""
while newFacture != "n":

    while newProduct != "n":
        productTemp["name"]= input("==> Product Name :  ")
        productTemp["price"]= float(input("    Product Price :  "))
        productTemp["quantity"]= int(input("    Product Quantity :  "))
        newProduct=input("Enter a new product ? y/n__  ")
        curentProduct=copy.deepcopy(productTemp)
        productList.append(curentProduct)
        while newProduct!="y" and newProduct!= "n":
            newProduct=input("Enter a new product ? y/n")
        print("----------------------------------------------")
    
    newProduct=""
    totalPrice=0
    print("_______________________FACTURE_________________________")
    for product in productList:
        print("     Name : {}    Quantity : {}  Price :  {}".format(product["name"],product["quantity"],product["price"]))
        totalPrice=totalPrice + product["quantity"]*product["price"]
    print("     TOTAL : {}".format(totalPrice))
    print(" ")
    newProduct = ""
    productList.clear()

    newFacture=input("Entrer liste e produit ? y/n__  ")
    while newFacture!="y" and newFacture!= "n":
        newFacture=input("Entrer liste e produit ? y:yes or n:no__  ")
    print("----------------------------------------------")