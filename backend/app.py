# app.py
from flask import Flask, request, jsonify
from web3 import Web3
import os

# Initialize Flask app
app = Flask(__name__)

# Example configuration
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your_secret_key_here")
infura_url = os.getenv("INFURA_URL", "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")
web3 = Web3(Web3.HTTPProvider(infura_url))

# Test Ethereum connection
if web3.isConnected():
    print("Connected to Ethereum node!")
else:
    print("Failed to connect to Ethereum node!")

# Sample route for portfolio data
@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    sample_portfolio = {
        "user_address": "0x123456789abcdef...",
        "assets": {
            "ETH": 1.5,
            "USDC": 500,
            "DAI": 1000
        },
        "total_value_usd": 3000
    }
    return jsonify(sample_portfolio)

# Example of an API endpoint for performing a transaction (dummy example)
@app.route('/execute_transaction', methods=['POST'])
def execute_transaction():
    data = request.get_json()
    user_address = data.get("user_address")
    token = data.get("token")
    amount = data.get("amount")
    
    # Example validation
    if not user_address or not token or not amount:
        return jsonify({"error": "Missing transaction data"}), 400
    
    # Dummy response (in a real app, you'd interact with a smart contract)
    return jsonify({
        "status": "success",
        "message": f"{amount} {token} transferred from {user_address}"
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "Healthy", "message": "API is up and running!"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
