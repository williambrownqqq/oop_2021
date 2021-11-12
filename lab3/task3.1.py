# from colorama import Fore, init
# from colorama import Style
# init(autoreset=True)
#
# from random import randint
# import json
#
# def withdraw():
#     print(f"\t\t\t\t\t\t\t\t\t{Fore.LIGHTMAGENTA_EX} TICKETS {Style.RESET_ALL}")
#     print(f"{Fore.CYAN}\t\t{Ticket.data[0]}{Style.RESET_ALL} ticket\t\t\t\t\t\t\t\t\t\t\t\t\t"
#           f" Price: {Fore.CYAN}{Ticket.prices[0]}{Style.RESET_ALL} $\t\t"
#           f"Amount:  {Fore.CYAN}{Ticket.amount[0]}{Style.RESET_ALL}")
#     print(f"{Fore.CYAN}\t\t{Ticket.data[1]}{Style.RESET_ALL} ticket - purchased 60 or more days before the event\t\t"
#           f" Price: {Fore.CYAN}{Ticket.prices[1]}{Style.RESET_ALL} $\t\t"
#           f"Amount:  {Fore.CYAN}{Ticket.amount[1]}{Style.RESET_ALL}")
#     print(f"{Fore.CYAN}\t\t{Ticket.data[2]}{Style.RESET_ALL} ticket - purchased fewer than 10 days before the event\t\t"
#           f" Price: {Fore.CYAN}{Ticket.prices[2]}{Style.RESET_ALL} $\t\t"
#           f"Amount:  {Fore.CYAN}{Ticket.amount[2]}{Style.RESET_ALL}")
#     print(f"{Fore.CYAN}\t\t{Ticket.data[3]}{Style.RESET_ALL} ticket\t\t\t\t\t\t\t\t\t\t\t\t\t"
#           f" Price: {Fore.CYAN}{Ticket.prices[3]}{Style.RESET_ALL} $\t\t"
#           f"Amount:  {Fore.CYAN}{Ticket.amount[3]}{Style.RESET_ALL}")
#
#
# def TicketsLists(ids):
#     ids = [i for i in ids if i is not None]  # delete None - not created ticket
#     with open("TicketIDs.json", "w") as IDS:  # rewrite list without None values
#         json.dump(ids, IDS)
#     print(ids)
#
#
# def Check(ids):
#     print("Enter ticket ID: ")
#     while True:
#         id = input()
#         if id in ids:
#             break
#         else:
#             print("Id hasn't been found!")
#             continue
#
#     if id in ids:
#         if "0A" in id:
#             print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
#                   f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[1]}{Style.RESET_ALL}\n"
#                   f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[1]}{Style.RESET_ALL} $\n")
#         elif "0L" in id:
#             print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
#                   f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[2]}{Style.RESET_ALL}\n"
#                   f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[2]}{Style.RESET_ALL} $\n")
#         elif "0R" in id:
#             print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
#                   f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[0]}{Style.RESET_ALL}\n"
#                   f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[0]}{Style.RESET_ALL} $\n")
#         elif "0S" in id:
#             print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
#                   f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[3]}{Style.RESET_ALL}\n"
#                   f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[3]}{Style.RESET_ALL} $\n")
#
#
# class Ticket:
#     # ticketValues = ["regular", "advance", "late", "student"]
#     # price = [100, 60, 110, 50]
#     # amount = [20, 10, 30, 5]
#
#     # with open("amount.json", "w") as :
#     # json.dump(amount, )
#     data = []
#     prices = []
#     amount = []
#     # with open("database.json", "w") as database:
#     # json.dump(ticketValues, database)
#     # jsonString = json.dumps(ticketValues, indent=4)
#     # print(database)
#     # print(jsonString)
#
#     with open("database.json", "r") as readNames:
#         data = json.load(readNames)
#     with open("prices.json", "r") as readPrice:
#         prices = json.load(readPrice)
#     with open("amount.json", "r") as readAmount:
#         amount = json.load(readAmount)
#
#     def __init__(self, ticket):
#         self.ticket = ticket
#         self.price = 0
#         self.code = ""
#         self.amount = 0
#
#     @property
#     def ticket(self):
#         return self.__ticket
#
#     @ticket.setter
#     def ticket(self, ticket):
#         if not isinstance(ticket, str):
#             raise TypeError("ticket must be \"String\" type!")
#         if not ticket:
#             raise ValueError("ticket mustn't be empty!")
#         if not ticket in Ticket.data:
#             raise ValueError("ticket must be: regular, advance, late, student!")
#         self.__ticket = ticket
#
#     def ticketType(self):
#         code = ""
#         if self.ticket == Ticket.data[0]:  # regular
#             if Ticket.amount[0] > 0:
#                 Ticket.amount[0] -= 1
#                 self.amount = Ticket.amount[0]
#                 for count in range(5):
#                     code += str(randint(0, 9))
#                 self.code = "0R" + code
#             else:
#                 print("no one ticket left")
#                 return
#         elif self.ticket == Ticket.data[1]:  # advance
#             if Ticket.amount[1] > 0:
#                 Ticket.amount[1] -= 1
#                 self.amount = Ticket.amount[1]
#                 for count in range(5):
#                     code += str(randint(0, 9))
#                 self.code = "0A" + code
#             else:
#                 print("no one ticket left")
#                 return
#         elif self.ticket == Ticket.data[2]:  # late
#             if Ticket.amount[2] > 0:
#                 Ticket.amount[2] -= 1
#                 self.amount = Ticket.amount[2]
#                 for count in range(5):
#                     code += str(randint(0, 9))
#                 self.code = "0L" + code
#             else:
#                 print("no one ticket left")
#                 return
#         elif self.ticket == Ticket.data[3]:  # student
#             if Ticket.amount[3] > 0:
#                 Ticket.amount[3] -= 1
#                 self.amount = Ticket.amount[3]
#                 for count in range(5):
#                     code += str(randint(0, 9))
#                 self.code = "0S" + code
#             else:
#                 print("no one ticket left")
#                 return
#         return self.code
#
#     def priceTicket(self):
#         if self.ticket == Ticket.data[0]:  # regular
#             self.price = Ticket.prices[0]  # price
#         elif self.ticket == Ticket.data[1]:
#             self.price = Ticket.prices[1]
#         elif self.ticket == Ticket.data[2]:
#             self.price = Ticket.prices[2]
#         elif self.ticket == Ticket.data[3]:
#             self.price = Ticket.prices[3]
#         return self.price
#
#     def __str__(self):
#         return f"\n\t\tPRINT\n" \
#                f"Your ticket:{Fore.LIGHTMAGENTA_EX} {self.__ticket}{Style.RESET_ALL}\n" \
#                f"Your ticket ID:{Fore.LIGHTMAGENTA_EX} {self.code}{Style.RESET_ALL}\n" \
#                f"{Fore.LIGHTMAGENTA_EX}{self.price}{Style.RESET_ALL} $ for pay\n"
#
#
# def main():
#     ids = []
#     withdraw()
#     ticket = ""
#     indT = True
#
#     """buying tickets"""
#     while indT:
#
#         """checking type"""
#         while True:
#             print(f"{Fore.BLUE}select 1 ticket:{Style.RESET_ALL}")
#             ticket = input()
#             if ticket.lower() in Ticket.data:
#                 break
#             else:
#                 print(f"ticket must be: regular, advance, late, student!")
#
#         ticket1 = Ticket(ticket.lower())
#         ID = ticket1.ticketType()
#         ids.append(ID)
#         print(f"ticket ID: {Fore.LIGHTMAGENTA_EX}{ID}{Style.RESET_ALL} ")
#         with open("TicketIDs.json", "w") as TicketIDs:
#             json.dump(ids, TicketIDs)
#
#         print(f"price: {Fore.LIGHTMAGENTA_EX}{ticket1.priceTicket()}{Style.RESET_ALL} $")
#         print(f"left: {Fore.LIGHTMAGENTA_EX}{ticket1.amount}{Style.RESET_ALL}")
#
#         """ ask user to continue buy tickets """
#
#         print("Would u want to continue? yes/no")
#         while True:
#             choice = input()
#             if choice == "no":
#                 indT = False
#                 break
#             elif choice == "yes":
#                 indT = True
#                 break
#             else: continue
#
#     """ withdraw all tickets """
#     print("would u want to see all tickets? yes/no")
#     while True:
#         choice = input()
#         if choice == "no":
#             break
#         elif choice == "yes":
#             TicketsLists(ids)
#             break
#         else:
#             continue
#
#     """ info about ticket """
#
#     print("would u want to see info about ticket? yes/no")
#     while True:
#         choice = input()
#         if choice == "no":
#             break
#         elif choice == "yes":
#             Check(ids)
#             break
#         else:
#             continue
#
#
# main()
import json
from colorama import Fore, init
from colorama import Style
init(autoreset=True)
from random import randint


def withdraw():
    print(f"\t\t\t\t\t\t\t\t\t{Fore.LIGHTMAGENTA_EX} TICKETS {Style.RESET_ALL}")
    print(f"{Fore.CYAN}\t\t{Ticket.data[0]}{Style.RESET_ALL} ticket\t\t\t\t\t\t\t\t\t\t\t\t\t"
          f" Price: {Fore.CYAN}{Ticket.prices[0]}{Style.RESET_ALL} $\t\t"
          f"Amount:  {Fore.CYAN}{Ticket.amount[0]}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}\t\t{Ticket.data[1]}{Style.RESET_ALL} ticket - purchased 60 or more days before the event\t\t"
          f" Price: {Fore.CYAN}{Ticket.prices[1]}{Style.RESET_ALL} $\t\t"
          f"Amount:  {Fore.CYAN}{Ticket.amount[1]}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}\t\t{Ticket.data[2]}{Style.RESET_ALL} ticket - purchased fewer than 10 days before the event\t\t"
          f" Price: {Fore.CYAN}{Ticket.prices[2]}{Style.RESET_ALL} $\t\t"
          f"Amount:  {Fore.CYAN}{Ticket.amount[2]}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}\t\t{Ticket.data[3]}{Style.RESET_ALL} ticket\t\t\t\t\t\t\t\t\t\t\t\t\t"
          f" Price: {Fore.CYAN}{Ticket.prices[3]}{Style.RESET_ALL} $\t\t"
          f"Amount:  {Fore.CYAN}{Ticket.amount[3]}{Style.RESET_ALL}")

def factory(ticket):
    """ factory method """
    if ticket.lower() == "regular":
        return Ticket(ticket.lower())
    elif ticket.lower() == "student":
        return StudentTicket(ticket.lower())
    elif ticket.lower() == "advance":
        return AdvanceTicket(ticket.lower())
    elif ticket.lower() == "late":
        return LateTicket(ticket.lower())
    else:
        return None



def OneMoreTicket(indT):
    """buying tickets"""
    print("Would u want to continue? yes/no")
    while True:
        choice = input()
        if choice.lower() == "no":
            indT = False
            break
        elif choice.lower() == "yes":
            indT = True
            break
        else:
            continue
    return indT


class Ticket:
    data = []
    prices = []
    amount = []
    with open("database.json", "r") as readNames:
        data = json.load(readNames)
    with open("prices.json", "r") as readPrice:
        prices = json.load(readPrice)
    with open("amount.json", "r") as readAmount:
        amount = json.load(readAmount)

    def __init__(self, ticket):
        self.ticket = ticket
        self.price = 0
        self.code = ""
        self.amount = 0

    @property
    def ticket(self):
        return self.__ticket

    @ticket.setter
    def ticket(self, ticket):
        if not isinstance(ticket, str):
            raise TypeError("ticket must be \"String\" type!")
        if not ticket:
            raise ValueError("ticket mustn't be empty!")
        if not ticket in Ticket.data:
            raise ValueError("ticket must be: regular, advance, late, student!")
        self.__ticket = ticket

    def TicketType(self):
        code = ""
        if self.__ticket == Ticket.data[0]:  # regular
            if Ticket.amount[0] > 0:
                Ticket.amount[0] -= 1
                self.amount = Ticket.amount[0]
                for count in range(5):
                    code += str(randint(0, 9))
                self.code = "0R" + code
            else:
                print("no one ticket left")
                return
        return self.code

    def priceTicket(self):
        if self.__ticket == Ticket.data[0]:  # regular
            self.price = Ticket.prices[0]  # price
        return self.price

    def __str__(self):
        return f"\n\t\tPRINT\n" \
               f"Your ticket:{Fore.LIGHTMAGENTA_EX} {self.__ticket}{Style.RESET_ALL}\n" \
               f"Your ticket ID:{Fore.LIGHTMAGENTA_EX} {self.code}{Style.RESET_ALL}\n" \
               f"{Fore.LIGHTMAGENTA_EX}{self.price}{Style.RESET_ALL} $ for pay\n" \
               f"left: {Fore.LIGHTMAGENTA_EX}{self.amount}{Style.RESET_ALL}\n"


class StudentTicket(Ticket):
    def __init__(self, ticket):
        super().__init__(ticket)

    def TicketType(self):
        code = ""
        if self.ticket == Ticket.data[3]:  # student
            if Ticket.amount[3] > 0:
                Ticket.amount[3] -= 1
                self.amount = Ticket.amount[3]
                for count in range(5):
                    code += str(randint(0, 9))
                self.code = "0S" + code
            else:
                print("no one ticket left")
                return
        return self.code

    def priceTicket(self):
        if self.ticket == Ticket.data[3]:  # student
            self.price = Ticket.prices[3]  # price
        return self.price

    def __str__(self):
        return super().__str__()


class AdvanceTicket(Ticket):
    def __init__(self, ticket):
        super().__init__(ticket)

    def TicketType(self):
        code = ""
        if self.ticket == Ticket.data[1]:  # advance
            if Ticket.amount[1] > 0:
                Ticket.amount[1] -= 1
                self.amount = Ticket.amount[1]
                for count in range(5):
                    code += str(randint(0, 9))
                self.code = "0A" + code
            else:
                print("no one ticket left")
                return
        return self.code

    def priceTicket(self):
        if self.ticket == Ticket.data[1]:  # advance
            self.price = Ticket.prices[1]  # price
        return self.price

    def __str__(self):
        return super().__str__()


class LateTicket(Ticket):
    def __init__(self, ticket):
        super().__init__(ticket)

    def TicketType(self):
        code = ""
        if self.ticket == Ticket.data[2]:  # late
            if Ticket.amount[2] > 0:
                Ticket.amount[2] -= 1
                self.amount = Ticket.amount[2]
                for count in range(5):
                    code += str(randint(0, 9))
                self.code = "0L" + code
            else:
                print("no one ticket left")
                return
        return self.code

    def priceTicket(self):
        if self.ticket == Ticket.data[2]:  # late
            self.price = Ticket.prices[2]  # price
        return self.price

    def __str__(self):
        return super().__str__()


class Event:
    def __init__(self, ids):
        self.ids = ids

    def TicketsLists(self):
        self.ids = [i for i in self.ids if i is not None]  # delete None - not created ticket
        with open("TicketIDs.json", "w") as IDS:  # rewrite list without None values
            json.dump(self.ids, IDS)
        print(self.ids)

    def Check(self):
        print("Enter ticket ID: ")
        while True:
            id = input()
            if id in self.ids:
                break
            else:
                print("Id hasn't been found!")
                continue

        if id in self.ids:
            if "0A" in id:
                print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
                      f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[1]}{Style.RESET_ALL}\n"
                      f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[1]}{Style.RESET_ALL} $\n")
            elif "0L" in id:
                print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
                      f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[2]}{Style.RESET_ALL}\n"
                      f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[2]}{Style.RESET_ALL} $\n")
            elif "0R" in id:
                print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
                      f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[0]}{Style.RESET_ALL}\n"
                      f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[0]}{Style.RESET_ALL} $\n")
            elif "0S" in id:
                print(f"Your ticket ID: {Fore.LIGHTMAGENTA_EX}{id}{Style.RESET_ALL}\n"
                      f"Your ticket type: {Fore.LIGHTMAGENTA_EX}{Ticket.data[3]}{Style.RESET_ALL}\n"
                      f"Price: {Fore.LIGHTMAGENTA_EX}{Ticket.prices[3]}{Style.RESET_ALL} $\n")




def main():
    ids = []
    indT = True
    withdraw()
    """buying tickets"""
    while indT:

        """checking type"""
        while True:
            print(f"{Fore.BLUE}select 1 ticket:{Style.RESET_ALL}")
            ticket = input()
            if ticket.lower() in Ticket.data:
                break
            else:
                print(f"ticket must be: regular, advance, late, student!")

        # event = Event(ticket)
        # event.TicketType()
        # event.priceTicket()
        # print(event)

        # if ticket.lower() == "regular":
        #     ticket1 = Ticket(ticket.lower())
        # elif ticket.lower() == "student":
        #     ticket1 = StudentTicket(ticket.lower())
        # elif ticket.lower() == "advance":
        #     ticket1 = AdvanceTicket(ticket.lower())
        # elif ticket.lower() == "late":
        #     ticket1 = LateTicket(ticket.lower())

        ticket1 = factory(ticket)


        ID = ticket1.TicketType()
        ticket1.priceTicket()
        print(ticket1)

        ids.append(ID)
        #print(f"ticket ID: {Fore.LIGHTMAGENTA_EX}{ID}{Style.RESET_ALL} ")
        with open("TicketIDs.json", "w") as TicketIDs:
            json.dump(ids, TicketIDs)
        #print(f"price: {Fore.LIGHTMAGENTA_EX}{ticket1.priceTicket()}{Style.RESET_ALL} $")
        #print(f"left: {Fore.LIGHTMAGENTA_EX}{ticket1.amount}{Style.RESET_ALL}")

        """ ask user to continue buy tickets """

        print("Would u want to continue? yes/no")
        while True:
            choice = input()
            if choice.lower() == "no":
                indT = False
                break
            elif choice.lower() == "yes":
                indT = True
                break
            else:
                continue

    """ withdraw all tickets """

    print("would u want to see all tickets? yes/no")
    event = Event(ids)
    while True:
        choice = input()
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            event.TicketsLists()
            break
        else:
            continue

    """ search info about ticket """

    print("would u want to see info about ticket? yes/no")
    while True:
        choice = input()
        if choice.lower() == "no":
            break
        elif choice.lower() == "yes":
            event.Check()
            break
        else:
            continue



main()



