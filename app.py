from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Replace these with your provider panel's details
API_URL = "https://growwsmmpanel.com/api/v2"
API_KEY = "b3a1c4c4725e1114a8831e1835240ead"
SERVICE_LIKES = 2771
SERVICE_VIEWS = 4505

# Function to get live balance from the provider's panel
def get_balance():
    balance_url = f"{API_URL}/api/v2"
    params = {
        "key": API_KEY,
        "action": "balance"
    }
    
    try:
        response = requests.get(balance_url, params=params)
        balance_data = response.json()
        
        # Check if balance is present in the response
        if "balance" in balance_data:
            return f"₹{balance_data['balance']}"  # Convert USD to INR if needed
        else:
            return "Balance not available"
    except Exception as e:
        return f"Error fetching balance: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    # Get live balance from the provider
    balance = get_balance()

    if request.method == 'POST':
        # Handle the order creation here
        link = request.form['post_link']
        quantity = request.form['quantity']
        service_type = request.form['service_type']
        
        # Check if quantity is entered (it must be a valid number)
        if quantity.isdigit():
            quantity = int(quantity)
            
            if service_type == 'Likes':
                service_id = SERVICE_LIKES
            else:
                service_id = SERVICE_VIEWS
            
            # Now, create the order using the API
            order_url = f"{API_URL}/api/v2/order"
            order_params = {
                "key": API_KEY,
                "service": service_id,
                "link": link,
                "quantity": quantity
            }

            # Debugging: Check the order_params being sent
            print("Order parameters:", order_params)
            
            order_response = requests.post(order_url, data=order_params)
            order_data = order_response.json()

            # Debugging: Check the response from the API
            print("API Response:", order_data)

            if order_data.get("status") == "success":
                return render_template_string(html_template, balance=balance, success="Order created successfully!")
            else:
                error_message = order_data.get("message", "Failed to create order.")
                return render_template_string(html_template, balance=balance, error=f"Error: {error_message}")
        else:
            return render_template_string(html_template, balance=balance, error="Please enter a valid quantity.")

    return render_template_string(html_template, balance=balance)


# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Creation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 10px;
            text-align: center;
        }

        .balance {
            font-size: 20px;
            font-weight: bold;
        }

        .form-container {
            margin-top: 20px;
        }

        input, select {
            margin: 10px;
            padding: 10px;
            width: 100%;
            max-width: 300px;
            font-size: 16px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            margin-top: 10px;
        }

        button:disabled {
            background-color: #ddd;
        }

        .quantity-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }

        .quantity-buttons button {
            padding: 10px 15px;
            font-size: 14px;
        }

        .error, .success {
            font-size: 18px;
            color: red;
            margin-top: 10px;
        }

        .success {
            color: green;
        }
    </style>
</head>
<body>

    <h1>Create Order</h1>
    <p class="balance">Live Balance: {{ balance }}</p>

    <div class="form-container">
        <form method="POST">
            <input type="url" name="post_link" placeholder="Enter Post/Reel Link" required>

            <div class="quantity-buttons">
                <button type="button" onclick="setQuantity(1000)">1k</button>
                <button type="button" onclick="setQuantity(2000)">2k</button>
                <button type="button" onclick="setQuantity(3000)">3k</button>
                <button type="button" onclick="setQuantity(5000)">5k</button>
                <button type="button" onclick="setQuantity(10000)">10k</button>
            </div>

            <input type="number" id="quantityInput" name="quantity" placeholder="Enter Custom Quantity" required oninput="toggleCreateOrderButton()">
            
            <select name="service_type" required>
                <option value="Likes">Likes</option>
                <option value="Views">Views</option>
            </select>

            <button type="submit" id="createOrderButton" disabled>Create Order</button>
        </form>

        {% if error %}
            <p class="error">{{ error }}</p>
        {% elif success %}
            <p class="success">{{ success }}</p>
        {% endif %}
    </div>

    <script>
        function setQuantity(quantity) {
            document.getElementById('quantityInput').value = quantity;
            toggleCreateOrderButton();
        }

        function toggleCreateOrderButton() {
            var quantity = document.getElementById('quantityInput').value;
            var createOrderButton = document.getElementById('createOrderButton');
            if (quantity && !isNaN(quantity) && quantity > 0) {
                createOrderButton.disabled = false;
            } else {
                createOrderButton.disabled = true;
            }
        }
    </script>

</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
