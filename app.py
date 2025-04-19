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
            padding: 40px;
            max-width: 400px;
            margin: auto;
        }
        input[type="text"] {
            width: 100%%;
            padding: 10px;
            margin-bottom: 15px;
        }
        .radio-group {
            margin-bottom: 15px;
        }
        .button-row {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
        }
        .button-row button {
            flex: 1;
            padding: 10px;
        }
        .full-button {
            width: 100%%;
            padding: 10px;
        }
    </style>
</head>
<body>
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
