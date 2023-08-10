class YoVeganMenu:
    def __init__(self):
        self.order_items = []
        self.menu = {
            1: ("YoCombos", {
                1: ("NotChicken Burger Crispy + Juice/ Water + Seasoned Baked Potato portion", 10.99),
                2: ("NotBurger XL + Juice/ Water + Seasoned Baked Potato portion", 9.99),
                3: ("NotChicken Burger + Juice/ Water + Seasoned Baked Potato portion", 8.99),
                4: ("NotBurger Parrilla + Juice/ Water + Seasoned Baked Potato portion", 8.49),
                5: ("NotBurger + Juice/ Water + Seasoned Baked Potato portion", 7.99)
            }),
            2: ("YoBurgers", {
                1: ("NotChicken Burger Crispy", 4.99),
                2: ("NotBurger XL", 4.49),
                3: ("NotChicken Burger", 3.99),
                4: ("NotBurger Parrilla", 3.49),
                5: ("NotBurger", 2.99)
            }),
            3: ("YoComplements", {
                1: ("Seasoned Baked Potato portion", 1.49),
                2: ("NotChicken Nuggets portion", 2.49),
                3: ("NotChicken Sticks portion", 2.99)
            }),
            4: ("YoBeverages", {
                1: ("Orange Juice", 1.49),
                2: ("Pineapple Juice", 1.49),
                3: ("Grape Juice", 1.49),
                4: ("Sparkling Water", 0.99),
                5: ("Water", 0.49)
            }),
            5: ("YoDesserts", {
                1: ("NotIceCream Dulce de Leche", 3.49),
                2: ("NotIceCream Chocolate", 3.49),
                3: ("NotIceCream Strawberry", 3.49),
                4: ("NotIceCream Banana", 3.49)
            })
        }

    def get_customer_name(self):
        name = input("Please enter your name: ")
        return name
    
    def display_menu(self, category_choice=None):
        if category_choice is None:
            print(f"Choose the best YoOption for you:")
            for num, (category, items) in self.menu.items():
                print(f"{num}. {category}")
        else:
            category, items = self.menu[category_choice]
            print(f"Choose your YoItem from {category}:")
            for num, (item, price) in items.items():
                print(f"{num}. {item} - ${price:.2f}")
    
    def order(self):
        self.display_menu()
        category_choice = int(input("Enter the number of your chosen YoCategory: "))
        
        if category_choice in self.menu:
            self.display_menu(category_choice)
            item_choice = int(input("Enter the number of your chosen YoItem: "))
            
            category, items = self.menu[category_choice]
            if item_choice in items:
                selected_item, price = items[item_choice]
                self.order_items.append((selected_item, price))
                print(f"{selected_item} has been added to your YoOrder.")
            else:
                print("Invalid YoItem choice. Please select a valid option from the YoMenu.")
        else:
            print("Invalid YoCategory choice. Please select a valid option from the YoMenu.")
    
    def remove_item(self):
        print("Your current YoOrder:")
        for idx, (item, price) in enumerate(self.order_items, start=1):
            print(f"{idx}. {item}: ${price:.2f}")
        
        if self.order_items:
            item_choice = int(input("Enter the number of the YoItem you want to remove: "))
            if 1 <= item_choice <= len(self.order_items):
                removed_item = self.order_items.pop(item_choice - 1)
                print(f"{removed_item[0]} has been removed from your YoOrder.")
            else:
                print("Invalid YoItem choice. Please select a valid option from your YoOrder.")
        else:
            print("Your YoOrder is empty.")
    
    def show_order(self):
        if self.order_items:
            total_price = sum(item[1] for item in self.order_items)
            print("Your current YoOrder:")
            for idx, (item, price) in enumerate(self.order_items, start=1):
                print(f"{idx}. {item}: ${price:.2f}")
            print(f"YoTotal: ${total_price:.2f}")
        else:
            print("Your YoOrder is empty.")
    
    def confirm_order(self):
        self.show_order()
        print(f"{yo_vegan.customer_name}, select your YoPayment method:")
        print("1. YoCash")
        print("2. YoCredit Card")
        payment_choice = int(input("Enter the number of your chosen YoPayment method: "))
        
        if payment_choice == 1:
            total_price = sum(item[1] for item in self.order_items)
            print(f"Thank you for your YoOrder, {self.customer_name}! Your YoTotal is ${total_price:.2f}. Please proceed to the YoCounter for YoPayment. Enjoy your YoMeal!")
            print("YoReminder: YoVegan is a YoPartnership with the company NotCo!")
        elif payment_choice == 2:
            total_price = sum(item[1] for item in self.order_items)
            print(f"Thank you for your YoOrder, {self.customer_name}! Your YoTotal is ${total_price:.2f}. Your YoCredit Card payment has been processed. Enjoy your YoMeal!")
            print("YoReminder: YoVegan is a YoPartnership with the company NotCo!")
        else:
            print("Invalid YoPayment choice. Please select either 1 for YoCash or 2 for YoCredit Card.")

if __name__ == "__main__":
    yo_vegan = YoVeganMenu()

    yo_vegan.customer_name = yo_vegan.get_customer_name()

    print(f"Welcome to YoVegan, {yo_vegan.customer_name}!")
    
    while True:
        print("\nYoOptions:")
        print("1. Order a YoItem")
        print("2. Remove a YoItem")
        print("3. Show current YoOrder")
        print("4. Confirm YoOrder")
        print("5. YoExit")

        choice = int(input("Select an YoOption: "))

        if choice == 1:
            yo_vegan.order()
        elif choice == 2:
            yo_vegan.remove_item()
        elif choice == 3:
            yo_vegan.show_order()
        elif choice == 4:
            yo_vegan.confirm_order()
            break
        elif choice == 5:
            print(f"Thank you for visiting YoVegan, {yo_vegan.customer_name}! YoReminder: YoVegan is a YoPartnership with the company NotCo!")
            break
        else:
            print("Invalid choice! Please select a valid YoOption.")