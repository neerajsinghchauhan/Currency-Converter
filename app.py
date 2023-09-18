from flask import Flask , render_template , request

app = Flask(__name__)

#Exchange rates of different countries

exchange_rates = { 
    'United States Dollar (USD)': 1.0,
    'Euro (EUR)': 0.85,
    'British Pound Sterling (GBP)': 0.72,
    'Japanese Yen (JPY)': 110.08,
    'Indian Rupee (INR)': 73.47,
    'Australian Dollar (AUD)': 1.35,
    'Canadian Dollar (CAD)': 1.27,
    'Singapore Dollar (SGD)': 1.33,
    'Swiss Franc (CHF)': 0.92,
    'Chinese Yuan (CNY)': 6.45,
    'New Zealand Dollar (NZD)': 1.45,
    'Swedish Krona (SEK)': 8.63,
    'Norwegian Krone (NOK)': 8.92,
    'Danish Krone (DKK)': 6.10,
    'Hong Kong Dollar (HKD)': 7.77,
    'South Korean Won (KRW)': 1154.12,
    'Mexican Peso (MXN)': 20.00,
    'Brazilian Real (BRL)': 5.18,
    'South African Rand (ZAR)': 14.83,
    'Russian Ruble (RUB)': 74.28,
    'Pakistani Rupee (PKR)': 286.30,  
    'Chinese Yuan Renminbi (CNY)': 6.45,
    
     } 

def get_country_names():
    return list(exchange_rates.keys())

def convert_currency(amount, from_currency , to_currency):
    if from_currency == to_currency:
        return amount

    else:
        try:
            conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
            converted_amount = amount*conversion_rate
            return converted_amount

        except KeyError:
            return 'currency is not find in exchange rates'

#define routes for html
@app.route('/' , methods=['GET' , 'POST'])
def currency_converter():
    country_names = get_country_names()

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            from_country = request.form['from_country']
            to_country = request.form['to_country']
            
            converted_amount = convert_currency(amount, from_country , to_country)

            if isinstance(converted_amount, str):
                result = converted_amount
            else:
                result = f"{amount}{from_country} is equal to {converted_amount}{to_country}"

            return render_template('index.html', exchange_rates = exchange_rates , country_names=country_names, result=result, from_country=from_country, to_country=to_country )

        except ValueError:
            error_message = 'Invalid input , Please enter a valid numeric unit'
            return render_template('index.html', exchange_rates = exchange_rates, country_names = country_names, error_message = error_message)

    return render_template('index.html', exchange_rates = exchange_rates , country_names = country_names)


if __name__ == '__main__':
    app.run(debug=True)            
                  

                             



