from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "A well-running e-commerce app delivers a smooth user experience with fast navigation, personalized recommendations, and clear product information. It relies on secure payments, real-time inventory updates, and reliable backend infrastructure to handle traffic and orders. Features like order tracking, notifications, and analytics improve engagement and business decisions, while strong security and compliance protect user data. Continuous performance monitoring and updates ensure the app stays efficient, trustworthy, and competitive."

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
