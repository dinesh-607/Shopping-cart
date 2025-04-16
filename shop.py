class shop:
    shop_name = 'bascis'
    address = 'chrompet'
    products = {'shirts' : [10,350], 'mobiles' : [5,20000], 'laptops':[0,85000]}

    def __init__(self, name, phone_no, address):
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.cart = {}

    @staticmethod
    def line():
        print('----------------------------------------------------------------------------------')


    @classmethod
    def display_products(cls):
        cls.line()
        print('Products available in the shop are:', end='\n\n')
        print('Products name','Qty','\tprice', sep='\t')
        print('-------------','---','\t-----', sep='\t')


        for product in cls.products:
            print(product,cls.products[product][0],cls.products[product][1],sep='\t\t')
        print()
        cls.line()

    def customer_details(self):
        self.line()
        print('Customer Details:')

        print()
        print('Name:',self.name)
        print('Phone no:',self.phone_no)
        print('address:',self.address)

        print()

        if self.cart =={}:
            print('Your cart is empty.')
        else:
            print('Products name','Qty','\tSubtotal', sep='\t')
            print('-------------','---','\t-----', sep='\t')

            total = 0

            for product in self.cart:
                subtotal = self.cart[product]*shop.products[product][1]
                total += subtotal

                print(product, self.cart[product],subtotal,sep='\t\t')
            self.line()
            print('Total',total)
        self.line()


    def add_products(self):
        self.line()
        print('ADD A PRODUCT')
        print()

        product = input('Enter a product:') #shirts

        if product in shop.products:
            print()
            qty = int(input('Enter the qty:'))
            if shop.products[product][0] >= qty:
                if product in self.cart:
                  self.cart[product] += qty  
                else:
                    self.cart[product]= qty
                shop.products[product][0] -= qty
                print('Product added successfully')

            else:
                print(f'Out of stock !! only{shop.products [product][0]} left!')

        else:
            self.line()
            print('The product is not available in the shop.')


        self.line()

    def remove_product(self):
        self.line()
        if self.cart == {}:
            print('Your cart is empty ,so we cannot remove the products')
        else:
            product=input('Enter a products:')
            if product in self.cart:
                qty = int(input('Enter the qty:'))
                if self.cart[product] >= qty:
                    self.cart[product] -= qty
                    shop.products[product][0] += qty
                    if self.cart[product] == 0:
                        self.cart.pop(product)
                    print('Product removed Succsessfully')

                else:
                    print(f'Cannot remove, Since you added only{self.cart[product]} products.')

            else:
                print('This product is not available in the cart')

        self.line()


    def main(self):
        self.line()
        print('Welcome to the shop!!!')
        self.line()

        while True:
            print('Enter 1 to display all the available in the shop.')
            print('Enter 2 to display your details.')
            print('Enter 3 to add a product.')
            print('Enter 4 to remove the products')
            print('Enter 5 to exit')

            option = int(input('Enter your option:'))

            if option == 1:
                self.display_products()

            elif option == 2:
                self.customer_details()

            elif option == 3:
                self.add_products()

            elif option == 4:
                self.remove_product()

            elif option == 5:
                self.line()
                print('Thank you for visiting!!')
                self.line()
                return
            
c1=shop('dinesh',12345678898765,'chennai')
c1.main()

        
