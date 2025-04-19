from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- For mobile optimization -->
    <title>Auto Order Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f1f1f1;
        }
        h2 {
            text-align: center;
            color: #333;
            margin-top: 20px;
            font-size: 24px;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }
        input[type="text"] {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        .radio-group {
            display: block;
            margin-bottom: 20px;
            padding: 0;
        }
        .radio-group label {
            display: block;
            text-align: center;
            margin-bottom: 10px;
            font-size: 18px;
        }
        button {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            font-size: 18px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .full-button {
            background-color: #28a745;
        }
        .full-button:hover {
            background-color: #218838;
        }
        .balance-info {
            font-size: 18px;
            margin-bottom: 20px;
            color: #333;
            text-align: center;
        }
        .add-funds {
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
        }
        .add-funds a {
            color: #007bff;
            text-decoration: none;
        }
        @media (max-width: 480px) {
            h2 {
                font-size: 22px;
            }
            .container {
                margin: 5px;
            }
            button {
                font-size: 18px;
                padding: 18px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Auto Order Tool</h2>
        <div class="balance-info">
            <p><strong>Live Balance:</strong> ₹{{ balance }}</p>
        </div>
        <form method="POST">
            <input type="text" name="link" placeholder="Enter post/reel link" required />
            <div class="radio-group">
                <label><input type="radio" name="service" value="2771" required> Likes</label>
                <label><input type="radio" name="service" value="4505"> Views</label>
            </div>
            <button type="submit" name="quantity" value="1000">1k</button>
            <button type="submit" name="quantity" value="2000">2k</button>
            <button type="submit" name="quantity" value="3000">3k</button>
            <button type="submit" name="quantity" value="5000">5k</button>
            <button class="full-button" type="submit" name="quantity" value="10000">10k</button>
        </form>
        <div class="add-funds">
            <p>If your balance is low, <a href="YOUR_PAYMENT_URL" target="_blank">add funds</a></p>
        </div>
        {% if response %}
            <p><strong>Response:</strong> {{ response }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

API_URL = "https://growwsmmpanel.com/api/v2"
API_KEY = "b3a1c4c4725e1114a8831e1835240ead"

# API endpoint to get the current balance (Assuming API provides it)
BALANCE_API_URL = "https://growwsmmpanel.com/api/v2/get_balance"

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    balance = get_balance()  # Fetch live balance

    if request.method == "POST":
        link = request.form.get("link")
        service = request.form.get("service")
        quantity = request.form.get("quantity")

        data = {
            "key": API_KEY,
            "action": "add",
            "service": service,
            "link": link,
            "quantity": quantity
        }

        try:
            r = requests.post(API_URL, data=data)
            response = r.json()
        except Exception as e:
            response = f"Error: {str(e)}"

    return render_template_string(HTML_PAGE, response=response, balance=balance)

def get_balance():
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(BALANCE_API_URL, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("balance", "0")
        else:
            return "Error fetching balance"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, port=7860)
