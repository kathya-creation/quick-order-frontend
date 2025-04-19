from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Auto Order Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            margin: 0;
            background-color: #f7f7f7;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        .container {
            max-width: 500px;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        input[type="text"], button {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .radio-group {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        .radio-group label {
            flex: 1;
            text-align: center;
        }
        .button-row {
            display: flex;
            gap: 10px;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .button-row button {
            flex: 1;
            padding: 10px;
            margin: 5px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .button-row button:hover {
            background-color: #0056b3;
        }
        .full-button {
            background-color: #28a745;
            margin-top: 10px;
        }
        .full-button:hover {
            background-color: #218838;
        }
        @media (max-width: 600px) {
            .radio-group {
                flex-direction: column;
                align-items: stretch;
            }
            .button-row {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Auto Order Tool</h2>
        <form method="POST">
            <input type="text" name="link" placeholder="Enter post/reel link" required />
            <div class="radio-group">
                <label><input type="radio" name="service" value="2771" required> Likes</label>
                <label><input type="radio" name="service" value="4505"> Views</label>
            </div>
            <div class="button-row">
                <button type="submit" name="quantity" value="1000">1k</button>
                <button type="submit" name="quantity" value="2000">2k</button>
            </div>
            <div class="button-row">
                <button type="submit" name="quantity" value="3000">3k</button>
                <button type="submit" name="quantity" value="5000">5k</button>
            </div>
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

@app.route("/", methods=["GET", "POST"])
def index():
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

    return render_template_string(HTML_PAGE, response=response)

if __name__ == "__main__":
    app.run(debug=True, port=7860)
