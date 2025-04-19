<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Order</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        .title {
            text-align: center;
            margin-bottom: 20px;
        }
        .input-group {
            margin-bottom: 15px;
        }
        .input-group label {
            font-size: 14px;
            color: #333;
        }
        .input-group input {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .input-group input:focus {
            outline: none;
            border-color: #007bff;
        }
        .button-group {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .button-group button {
            width: 48%;
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .button-group button:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        .order-btn {
            background-color: #007bff;
            color: white;
        }
        .quantity-btn {
            background-color: #f1f1f1;
            color: #007bff;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="title">
            <h2>Create Order</h2>
        </div>
        <div class="input-group">
            <label for="postLink">Enter Post/Reel Link:</label>
            <input type="text" id="postLink" placeholder="Enter your post link here">
        </div>
        <div class="input-group">
            <label for="quantity">Enter Quantity:</label>
            <input type="number" id="quantity" min="1" placeholder="Enter quantity" oninput="checkQuantity()">
        </div>
        <div class="button-group">
            <button class="quantity-btn" id="1k" onclick="selectQuantity(1000)">1k</button>
            <button class="quantity-btn" id="2k" onclick="selectQuantity(2000)">2k</button>
            <button class="quantity-btn" id="3k" onclick="selectQuantity(3000)">3k</button>
            <button class="quantity-btn" id="5k" onclick="selectQuantity(5000)">5k</button>
            <button class="quantity-btn" id="10k" onclick="selectQuantity(10000)">10k</button>
        </div>
        <div class="button-group">
            <button id="createOrderBtn" class="order-btn" disabled onclick="createOrder()">Create Order</button>
        </div>
    </div>

    <script>
        // Function to select the quantity from predefined buttons
        function selectQuantity(quantity) {
            document.getElementById('quantity').value = quantity;
            checkQuantity(); // Check if the quantity field is valid
        }

        // Function to check if quantity is entered
        function checkQuantity() {
            const quantity = document.getElementById('quantity').value;
            const createOrderBtn = document.getElementById('createOrderBtn');
            // Enable or disable the Create Order button based on quantity
            if (quantity && quantity > 0) {
                createOrderBtn.disabled = false;
            } else {
                createOrderBtn.disabled = true;
            }
        }

        // Function to create the order
        function createOrder() {
            const postLink = document.getElementById('postLink').value;
            const quantity = document.getElementById('quantity').value;

            // Check if post link and quantity are provided
            if (!postLink || !quantity) {
                alert("Please enter both post link and quantity.");
                return;
            }

            // Call API or handle the order creation logic here
            console.log(`Creating order for post: ${postLink}, Quantity: ${quantity}`);

            // You can add an API call here to create the order
            // Example: 
            // fetch('your-api-endpoint', { method: 'POST', body: JSON.stringify({ link: postLink, quantity: quantity }) })
        }
    </script>
</body>
</html>
