# Inventory Class problem from ProgrammingExpert.io

class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.inventory = []
        self.current_quantity = 0


    def add_item(self, name, price, quantity):
        for item in self.inventory:
            if item[0] == name:
                return False

        if (self.current_quantity + quantity) > self.max_capacity:
            return False
        else:
            self.inventory.append([name, price, quantity])
            self.current_quantity += quantity
            return True


    def delete_item(self, name):
        for item in self.inventory:
            if item[0] == name:
                self.current_quantity -= item[2]
                self.inventory.remove(item)
                return True
        return False


    def get_items_in_price_range(self, min_price, max_price):
        list_of_names = []
        for item in self.inventory:
            if item[1] >= min_price and item[1] <= max_price:
                list_of_names.append(item[0])
        return list_of_names


    def get_most_stocked_item(self):
        current_most_stock = 0
        most_stock_idx = 0
        if len(self.inventory) == 0:
            return None

        for item in range(len(self.inventory)):
            if self.inventory[item][2] > current_most_stock:
                current_most_stock = self.inventory[item][2]
                most_stock_idx = item
        return self.inventory[most_stock_idx][0]