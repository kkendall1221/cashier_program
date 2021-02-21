
# kaleb Kendall, freecode camp code along
# december 2020

if __name__ == '__main__':

    inventory =  {"bread":10, "milk": 12, "cola":7, "fanta":7, "water":35, "newspaper":12, "magazine":18,
              "candy":13, "juice":7, "orange": 3, "strawberies":25, " mango": 99 }

    basket = []
    total = []
    def cashier():
        user_answer = input( " hello there what do you wish to purchase today?:  ").lower()
        while user_answer != "quit":
            if user_answer in inventory:
             basket.append(user_answer)
             user_answer = input("perfect! i will add that to you basket! anything else you wish to purchase?""(type quit to end : ").lower()
            else:
             user_answer = input(" i am sorry but we do not have that item in our store, anything else you want ""(Type quit to end) : ").lower()

    cashier()

    print(" here are all the items in your shopping cart: ", basket)

    answer = input (" do you wish to add anything else? type yes or no: ").lower()
    if answer == "yes":
        cashier()
    print("here are all the items you requested: ", basket)

    for items in basket:
        total.append(inventory[items])
        amount_to_pay = sum(total)
    else:
        for items in basket:
            total.append(inventory[items])
        amount_to_pay = sum(total)

    print(" your total amount is: ", amount_to_pay)


