import pandas as pd

class Database:
    def __init__(self):
        self.inventory = pd.read_csv('data/inventory.csv')
        self.demand = pd.read_csv('data/demand.csv')
        self.products = pd.read_csv('data/products.csv')

    def get_inventory(self):
        return self.inventory

    def get_demand(self):
        return self.demand

    def get_products(self):
        return self.products

    def get_total_capacity(self):
        return 1000

    def update_inventory(self, product_id, quantity):
        self.inventory.loc[self.inventory['product_id'] == product_id, 'quantity'] = quantity
        self.inventory.to_csv('data/inventory.csv', index=False)
