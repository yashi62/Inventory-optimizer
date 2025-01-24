import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum
from database import Database

class InventoryOptimizer:
    def __init__(self):
        self.db = Database()

    def optimize_inventory(self):
        inventory = self.db.get_inventory()
        demand = self.db.get_demand()
        products = self.db.get_products()

        prob = LpProblem("Inventory_Optimization", LpMaximize)

        order_vars = {row['product_id']: LpVariable(f"Order_{row['product_id']}", lowBound=0, cat='Continuous') for _, row in inventory.iterrows()}

        prob += lpSum(order_vars[product_id] * products.loc[products['product_id'] == product_id, 'profit_per_unit'].values[0]
                      for product_id in order_vars)

        for _, row in demand.iterrows():
            product_id = row['product_id']
            prob += order_vars[product_id] >= row['forecasted_demand'], f"Demand_{product_id}"

        total_inventory = lpSum(order_vars[product_id] for product_id in order_vars)
        prob += total_inventory <= self.db.get_total_capacity(), "Capacity"

        prob.solve()

        recommendations = []
        for product_id, var in order_vars.items():
            recommendations.append({
                'product_id': product_id,
                'recommended_order': var.value()
            })

        return recommendations
