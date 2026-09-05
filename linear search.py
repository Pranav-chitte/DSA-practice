class store :
    def __init__(self,products):
        self.products  = products


    def search(self,product_name,products):
        found = False
        for  i in range (len(products)):
            if (products[i]==product_name ):
                print("product is available at index: ",i)
                found = True
                break
        if not found:
            print("product not found")
        


# starting 
store1 = store(["apple","banana","mango","grapes"])
a=input("enter product to find : ")
store1.search(a,store1.products)


