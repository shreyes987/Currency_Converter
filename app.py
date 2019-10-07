from flask import Flask, request
import load_config
import convert

app = Flask(__name__)

config = load_config.load('config.yaml')
#REQUEST THIS as input through postman in the body 
# Sample Request:
# {
#     "amount" : "100",
#     "src_currency" : "USD",
#     "dest_currency" : "INR",
#     "reference_date" : "2019-10-04"
# }


@app.route('/convert')
def convert_currency():
    input_data = request.get_json(force=True)
    print(input_data)
    converted_amount = convert.convert( input_data["amount"],
                                        input_data["src_currency"],
                                        input_data["dest_currency"],
                                        input_data["reference_date"])
    
    return "{'amount': " + str(converted_amount) + ", 'currency':"+ input_data["dest_currency"] +"}"
    

if __name__ == '__main__':
    app.run()