from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=["POST"])
def total_price():
    if request.method == 'POST':
        price1 = request.json["Book"]
        price2 = request.json["pen"]
        price3 = request.json["Water bottle"]
        price4 = request.json["Mobile cover"]
        total = price1+price2+price3+price4
        final_price = 0
        if total <= 1000:
            final_price = total - (total * 0.1)
        if total <= 2000 and total > 1000:
            final_price = total - (total * 0.2)
        else:
            final_price = total - (total * 0.3)

        return f"The final price is {final_price}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)