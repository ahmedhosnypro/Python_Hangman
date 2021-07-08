pizza = "Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad"
soup = "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"

input_ = input()

if input_ == "pizza":
    print(pizza)
elif input_ == "salad":
    print(salad)
elif input_ == "soup":
    print(soup)
else:
    print("Sorry, we don't have it in the menu")
