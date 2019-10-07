import load_xml
import load_config

config = load_config.load('config.yaml')

def get_convert_rates_for_reference_date(reference_date):
    load_xml.check_existing_xml_and_download_latest_xml()
    convert_rate_xml = load_xml.load()
    for item in convert_rate_xml:
        if item["@time"] == reference_date:
            return item[config["xmlRoot4"]]

def get_convert_rate_for_currency(convert_rates,currency):
    for item in convert_rates:
        if item["@currency"] == currency:
            return item["@rate"]


def convert(amount, src_currency, dest_currency, reference_date):
    # conversion logic here
    convert_rates_for_date = get_convert_rates_for_reference_date(reference_date)
    convert_rate_for_destcurrency = get_convert_rate_for_currency(convert_rates_for_date, dest_currency)
    convert_rate_for_srccurrency = get_convert_rate_for_currency(convert_rates_for_date, src_currency)
    print(convert_rate_for_destcurrency)
    print(convert_rate_for_srccurrency)
    if(convert_rate_for_destcurrency > convert_rate_for_srccurrency):
        print("inside")
        return int(amount) * convert_rate_for_destcurrency
    if(convert_rate_for_destcurrency < convert_rate_for_srccurrency):
        print("inside now")
        return int(amount) / convert_rate_for_destcurrency

    
if __name__ == "__main__":
    convert_rates = get_convert_rates_for_reference_date("2019-10-04")
    convert_rate_jpy = get_convert_rate_for_currency(convert_rates, "JPY")