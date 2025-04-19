from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        .balance {
            text-align: center;
            font-size: 18px;
            margin-bottom: 20px;
            color: #333;
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
        <div class="balance">
            <p><strong>Live Balance: ₹{{ balance }}</strong></p>
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
        {% if response %}
            <p><strong>Response:</strong> {{ response }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

API_URL = "https://growwsmmpanel.com/api/v2"
API_KEY = "b3a1c4c4725e1114a8831e1835240ead"

# Function to get live balance from the provider's panel
def get_balance():
    balance_url = f"{API_URL}/get_balance"  # Assuming API has a get_balance endpoint
    params = {
        "key": API_KEY
    }
    try:
        response = requests.get(balance_url, params=params)
        balance_data = response.json()
        if "balance" in balance_data:
            return balance_data["balance"]
        else:
            return "0"
    except Exception as e:
        return "Error fetching balance"

@app.route("/", methods=["GET", "POST"])
def index():
    balance = get_balance()  # Get live balance
    response = None
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

if __name__ == "__main__":
    app.run(debug=True, port=7860)
