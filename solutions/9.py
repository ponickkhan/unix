import re
class Product:
    def __init__(self,id):
        self.id = id

    def search_product(self):
        # Read lines
        file = open("products.txt" , 'r')
        Lines = file.readlines()

        Customers = []
        count = 0
        for line in Lines:
            if count > 0:
             arr = re.split("(\s+)", line.strip())
             if int(self.id) == int(arr[0]):

              print(line)



            count = count + 1





obj = Product(3423)
obj.search_product()
