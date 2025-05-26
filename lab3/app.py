from flask import Flask, render_template, request

app = Flask(__name__)


RATES = {
    'USD': {'RUB': 75.50, 'EUR': 0.92},
    'EUR': {'RUB': 82.30, 'USD': 1.09},
    'RUB': {'USD': 0.013, 'EUR': 0.012}
}


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    amount = 0

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_curr = request.form['from']
            to_curr = request.form['to']
            result = round(amount * RATES[from_curr][to_curr], 2)
        except ValueError:
            result = "Ошибка: введите число!"
        except KeyError:
            result = "Ошибка: выберите валюту!"

    return render_template('index.html',
                           result=result,
                           amount=amount,
                           currencies=RATES.keys())


if __name__ == '__main__':
    app.run(debug=True)
