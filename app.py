<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Panel</title>
    <style>
        /* Add your existing CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 100%;
            max-width: 400px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 16px;
        }

        .quantity {
            width: 70%;
            display: inline-block;
        }

        .price-display {
            margin: 20px 0;
            font-size: 18px;
            font-weight: bold;
        }

        button:disabled {
            background-color: #ccc;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Link Input -->
        <label for="post-link">Enter Post Link:</label>
        <input type="text" id="post-link" placeholder="Enter Post/Reel Link">

        <!-- Select Service -->
        <label for="service-type">Select Service:</label>
        <select id="service-type">
            <option value="likes">Likes</option>
            <option value="views">Views</option>
        </select>

        <!-- Predefined Quantity Buttons -->
        <div>
            <button onclick="setQuantity(1000)">1k</button>
            <button onclick="setQuantity(2000)">2k</button>
            <button onclick="setQuantity(3000)">3k</button>
            <button onclick="setQuantity(5000)">5k</button>
            <button onclick="setQuantity(10000)">10k</button>
        </div>

        <!-- Manual Quantity Input -->
        <div>
            <input type="number" id="manual-quantity" class="quantity" placeholder="Enter Custom Quantity" oninput="calculatePrice()">
        </div>

        <!-- Price Display -->
        <div class="price-display" id="price-display">Price: ₹0</div>

        <!-- Create Order Button -->
        <button id="create-order" disabled onclick="createOrder()">Create Order</button>
    </div>

    <script>
        // Prices per 1k for Likes and Views
        const prices = {
            likes: 15,  // Price for 1k Likes
            views: 20   // Price for 1k Views
        };

        let currentQuantity = 0;
        let currentService = "likes"; // Default to Likes

        // Set quantity from predefined buttons
        function setQuantity(quantity) {
            currentQuantity = quantity;
            document.getElementById("manual-quantity").value = quantity;
            calculatePrice();
        }

        // Calculate price based on quantity
        function calculatePrice() {
            const quantity = document.getElementById("manual-quantity").value;
            if (quantity > 0) {
                currentQuantity = quantity;
                document.getElementById("create-order").disabled = false;
                const price = (prices[currentService] * currentQuantity) / 1000;
                document.getElementById("price-display").innerText = `Price: ₹${price}`;
            } else {
                document.getElementById("create-order").disabled = true;
                document.getElementById("price-display").innerText = "Price: ₹0";
            }
        }

        // Handle the service type change (Likes or Views)
        document.getElementById("service-type").addEventListener("change", function() {
            currentService = this.value;
            calculatePrice();
        });

        // Create Order function (you can link this to your backend)
        function createOrder() {
            const postLink = document.getElementById("post-link").value;
            if (!postLink || currentQuantity <= 0) {
                alert("Please enter a valid link and quantity.");
                return;
            }
            
            // Here you can call your API to create an order
            alert(`Order created for ${currentQuantity} ${currentService} on post ${postLink}.`);

            // Optionally, you can reset the form after successful order
            document.getElementById("post-link").value = "";
            document.getElementById("manual-quantity").value = "";
            document.getElementById("create-order").disabled = true;
            document.getElementById("price-display").innerText = "Price: ₹0";
        }
    </script>
</body>
</html>
