from datetime import time
from menu import Menu
from franchise import Franchise
from business import Business

def main():
    # Criando Menus
    brunch_items = {
        'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
        'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
        'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }
    brunch = Menu("Brunch", brunch_items, time(11, 0), time(14, 0))

    early_bird_items = {
        'salumeria plate': 8.00, 
        'salad and breadsticks (serves 2, no refills)': 14.00,
        'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
        'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
    }
    early_bird = Menu("Early Bird", early_bird_items, time(15, 0), time(18, 0))

    dinner_items = {
        'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
        'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
        'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
    }
    dinner = Menu("Dinner", dinner_items, time(17, 0), time(23, 0))

    kids_items = {
        'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
        'apple juice': 3.00
    }
    kids = Menu("Kids", kids_items, time(11, 0), time(21, 0))

    arepas_items = {
        'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
        'guayanes arepa': 8.00, 'jamon arepa': 7.50
    }
    arepas = Menu("Take a’ Arepa", arepas_items, time(10, 0), time(20, 0))

    # Lista de Menus
    menus = [brunch, early_bird, dinner, kids]

    # Testando o cálculo de contas
    print("Conta do Brunch:", brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
    print("Conta do Early Bird:", early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

    # Criando Franchises
    flagship_store = Franchise("1232 West End Road", menus)
    new_installment = Franchise("12 East Mulberry Street", menus)
    arepas_place = Franchise("89 Fitzgerald Avenue", [arepas])

    # Testando o método `available_menus`
    print("\nMenus disponíveis às 20:00 na Flagship Store:")
    available_menus = flagship_store.available_menus(time(20, 0))
    for menu in available_menus:
        print(menu)

    # Criando Businesses
    basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
    arepa_business = Business("Take a’ Arepa", [arepas_place])

if __name__ == "__main__":
    main()