import json
from colorama import Fore, init
from colorama import Style
init(autoreset=True)

def DayPick(day):
    if day.lower() == "monday":
        Pizza = Monday(day)
        print(Pizza)
    elif day.lower() == "tuesday":
        Pizza = Tuesday(day)
        print(Pizza)
    elif day.lower() == "wednesday":
        Pizza = Wednesday(day)
        print(Pizza)
    elif day.lower() == "thursday":
        Pizza = Thursday(day)
        print(Pizza)
    elif day.lower() == "friday":
        Pizza = Friday(day)
        print(Pizza)
    elif day.lower() == "saturday":
        Pizza = Saturday(day)
        print(Pizza)
    elif day.lower() == "sunday":
        Pizza = Sunday(day)
        print(Pizza)
    return Pizza

def ExtraIngram(Pizza):
    print("\nwould you like to add some extra ingredients? yes/no")
    while True:
        choice = input()
        if choice.lower() == "no":
            print("\t\tYour order: ")
            print(Pizza)
            break
        elif choice.lower() == "yes":
            Pizza.withdrawIngrem()
            Pizza.chooseIngrem()
            print("\t\tYour order: ")
            print(Pizza)
            break
        else:
            continue

class Pizza:
    def __init__(self, day):
        self.day = day
        self.daypizz = ''
        self.pizzprice = 0
        self.choice = []
        with open("ingredients.json", "r") as ingram:
            self.ingredient = json.load(ingram)
        with open("pizzas.json", "r") as pizzaName:
            self.daypizza = json.load(pizzaName)
        with open("pizzaPrice.json", "r") as pizzaPrice:
            self.price = json.load(pizzaPrice)

    @property
    def day(self):
        return self.__day

    @property
    def ingredient(self):
        return self.__ingredient

    @property
    def daypizza(self):
        return self.__daypizza

    @property
    def price(self):
        return self.__price

    @property
    def choice(self):
        return self.__choice

    @day.setter
    def day(self, day):
        if not isinstance(day, str):
            raise Exception
        self.__day = day

    @choice.setter
    def choice(self, choice):
        if not isinstance(choice, list):
            raise Exception
        self.__choice = choice

    @daypizza.setter
    def daypizza(self, daypizza):
        if not isinstance(daypizza, list):
            raise Exception
        self.__daypizza = daypizza

    @price.setter
    def price(self, price):
        if not isinstance(price, list):
            raise Exception
        self.__price = price

    @ingredient.setter
    def ingredient(self, ingredient):
        if not isinstance(ingredient, list):
            raise Exception
        self.__ingredient = ingredient

    def withdrawIngrem(self):
        print(f"Ingredients: {self.ingredient}")

    def chooseIngrem(self):
        print(f"pick ingredients:\t\t q - quite")
        choice = []
        pick = ""
        while True:
            pick = input()
            if pick.lower() in self.ingredient:
                if pick not in self.choice:
                    self.choice.append(pick)
            elif pick.lower() == "q":
                break
            else:
                print(f"wrong, try again")
        return self.choice


    def __str__(self):
        if self.choice:
            return f"Pizza of {Fore.LIGHTMAGENTA_EX}{self.day}{Style.RESET_ALL} is {Fore.LIGHTMAGENTA_EX}{self.daypizz}{Style.RESET_ALL}!\n" \
                   f"Price: {Fore.LIGHTMAGENTA_EX}{self.pizzprice}{Style.RESET_ALL} $\n" \
                   f"Extra Ingredients: {Fore.LIGHTMAGENTA_EX}{self.choice}{Style.RESET_ALL}"
        else:
            return f"Pizza of {Fore.LIGHTMAGENTA_EX}{self.day}{Style.RESET_ALL} is {Fore.LIGHTMAGENTA_EX}{self.daypizz}{Style.RESET_ALL}!\n" \
                   f"Price: {Fore.LIGHTMAGENTA_EX}{self.pizzprice}{Style.RESET_ALL} $\n"

class Monday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[0] # price list
        self.daypizz = self.daypizza[0] # pizza's days

    def __str__(self):
        return super().__str__()

class Tuesday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[1] # price list
        self.daypizz = self.daypizza[1] # pizza's days

    def __str__(self):
        return super().__str__()

class Wednesday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[2] # price list
        self.daypizz = self.daypizza[2] # pizza's days

    def __str__(self):
        return super().__str__()

class Thursday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[3] # price list
        self.daypizz = self.daypizza[3] # pizza's days

    def __str__(self):
        return super().__str__()

class Friday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[4] # price list
        self.daypizz = self.daypizza[4] # pizza's days

    def __str__(self):
        return super().__str__()

class Saturday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[5] # price list
        self.daypizz = self.daypizza[5] # pizza's days

    def __str__(self):
        return super().__str__()

class Sunday(Pizza):
    def __init__(self, day):
        super().__init__(day)
        self.pizzprice = self.price[6] # price list
        self.daypizz = self.daypizza[6] # pizza's days

    def __str__(self):
        return super().__str__()

def main():
    with open("weekDays.json", "r") as weekDay:
        days = json.load(weekDay)

    print(f"{Fore.BLUE}enter the day of week:{Style.RESET_ALL}")

    """ enter the day """
    while True:
        day = input()
        if day.lower() in days:
            break
        else:
            print(f"wrong day, try again")

    """ create a pizza of day """
    Pizza = DayPick(day)

    """ add extra ingredients """
    ExtraIngram(Pizza)






    # writing
    # pizzassss = ["pepperoni", "4 cheeses", "4 meats", "barbecue", "hawaiian", "manhattan", "margherita"]
    # with open("pizzas.json", "w") as pizzaName:
    #     json.dump(pizzassss, pizzaName)
    #
    # junkFood = ["mushrooms", "Cheese", "Tomato", "fish", "bear", "deer", "pineapple", "lemons", "ankle", "coffee"]
    # with open("ingredients.json", "w") as ingredientsName:
    #     json.dump(junkFood, ingredientsName)
    #
    # price = [70, 111, 2000, 90, 60, 133, 154]
    # with open("pizzaPrice.json", "w") as pizzaPrice:
    #     json.dump(price, pizzaPrice)
    #
    # days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    # with open("weekDays.json", "w") as weekDay:
    #     json.dump(days, weekDay)


main()
