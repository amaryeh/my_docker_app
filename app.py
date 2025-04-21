from flask import Flask, request

app = Flask(__name__)

# Function to read product data from a file
def read_products_from_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read lines and create a list of tuples (product_id, price)
            return [tuple(line.strip().split(',')) for line in file.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Load product data from a file
products = read_products_from_file('prices.txt')

@app.route('/price', methods=['GET'])
def get_price():
    product_id = request.args.get('product_id')
    for product in products:
        if product[0] == product_id:
            return str(product[1]), 200  # Return price as plain text
    return "", 404  # Generic 404 for unknown product

# Custom handler for all 404 errors
@app.errorhandler(404)
def handle_404(e):
    return "", 404  # Return a generic 404 response with no additional info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
