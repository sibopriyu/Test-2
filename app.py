
from flask import Flask, request, jsonify
import razorpay

app = Flask(__name__)

# Razorpay Test Keys
razorpay_client = razorpay.Client(auth=("rzp_test_0ULm1xlSdVxdAa", "CNTbnDDSNzM28PVJqsiafohp"))

@app.route("/")
def home():
    return "LIGHTNING OTP Backend is Running!"

@app.route("/create_order", methods=["POST"])
def create_order():
    data = request.json
    amount = int(data.get("amount", 1)) * 100  # Convert to paise
    payment = razorpay_client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })
    return jsonify(payment)

if __name__ == "__main__":
    app.run(debug=True)
