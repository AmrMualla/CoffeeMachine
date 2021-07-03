#AmrMuallaCoffeeMachineProgram
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

is_on = True

def Charge(coffeecost, typeofcoffee):
  print("Please insert coins.")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickels = int(input("How many nickels?: "))
  pennies = int(input("How many pennies?: "))

  inserted = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

  Change = round(inserted - coffeecost, 2)
  if inserted < coffeecost:
    print("That's not enough money, your money will be refunded momentarily. ")
  elif inserted >= coffeecost:
    print(f"Here is $ {Change} in change.")
    print(f"Here is your {typeofcoffee} ☕️. Enjoy!")
    resources["money"] += coffeecost


while is_on:
  Coffee = input("What would you like? (espresso/latte/cappuccino):")

  if Coffee == "report":
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: " + "$" + str(resources["money"]))
  
  elif Coffee == "espresso":
    if resources["water"] < 50:
      print("Sorry not enough water.")
    elif resources["coffee"] < 18:
      print("Sorry not enough coffee.")
    else:
      Charge(1.5, "espresso")
      resources["water"] -= 50
      resources["coffee"] -= 18

  elif Coffee == "latte":
    if resources["water"] < 200:
      print("Sorry not enough water.")
    elif resources["milk"] < 150:
      print("Sorry not enough milk.")
    elif resources["coffee"] < 24:
      print("Sorry not enough coffee.")
    else:
      Charge(2.5, "latte")
      resources["water"] -= 200
      resources["milk"] -= 150
      resources["coffee"] -= 24


  elif Coffee == "cappuccino":
    if resources["water"] < 250:
      print("Sorry not enough water.")
    elif resources["milk"] < 100:
      print("Sorry not enough milk.")
    elif resources["coffee"] < 24:
      print("Sorry not enough coffee.")
    else:
      Charge(3.0, "cappuccino")
      resources["water"] -= 250
      resources["milk"] -= 100
      resources["coffee"] -= 24
      


  elif Coffee == "off":
    print("Powering down....")
    is_on = False
