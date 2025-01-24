from flask import Flask, request, jsonify, render_template
from optimizer import InventoryOptimizer
from database import Database

app = Flask(__name__)
optimizer = InventoryOptimizer()
db = Database()

@app.route('/')
def dashboard():
    inventory = db.get_inventory()
    products = db.get_products()
    return render_template('dashboard.html', inventory=inventory.to_dict(orient='records'), products=products.to_dict(orient='records'))

@app.route('/optimize', methods=['POST'])
def optimize_inventory():
    try:
        optimization_result = optimizer.optimize_inventory()
        return jsonify({'status': 'success', 'recommendations': optimization_result}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    data = request.json
    try:
        db.update_inventory(data['product_id'], data['quantity'])
        return jsonify({'status': 'success', 'message': 'Inventory updated successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
