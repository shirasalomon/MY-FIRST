import requests
class server():
    def __init__(self,url):
        self.date= requests.get(url,verify=False).json()['date']
        self.data=requests.get(url,verify=False).json()['rates']

    def convert(self,fromCurrency,toCurrency,amount):
        if fromCurrency != 'USD':
            amount = amount/self.data[fromCurrency]
        return amount * self.data[toCurrency]



