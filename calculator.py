from flask import Flask, render_template, request, jsonify
from calculate import Calculate

app = Flask(__name__)
# app.config.from_object(__name__)
calculator = Calculate()


@app.route('/')
def welcome():
    return render_template('calculator.html')


@app.route('/', methods=['POST'])
def result():
    data = request.get_json()  # Parse JSON data from the request
    number = int(data["input"])
    operator = data["operator"]

    if operator == "clear":
        calculator.clear()
        result = 'cleared'
    else:
        result = calculator.calculate(number, operator)
        if calculator.divided_zero:
            result = 'Cannot Divide by Zero'
            calculator.divided_zero = False
    return jsonify({"result": result})  # Return JSON response


if __name__ == '__main__':
    app.run(debug=True)
