from flask import Flask, request

app = Flask(__name__)

# Dummy product data: A list of tuples containing product ID and price
products = [
    ("101", 10.99),
    ("102", 15.49)
]

@app.route('/price', methods=['GET'])
def get_price():
    product_id = request.args.get('product_id')
    for product in products:
        if product[0] == product_id:
            return str(product[1]), 200  # Return price as plain text
    return "", 404  # Return a generic 404 error with no additional information
# Custom handler for all 404 errors
@app.errorhandler(404)
def handle_404(e):
    return "", 404  # Return a generic 404 response with no additional info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
