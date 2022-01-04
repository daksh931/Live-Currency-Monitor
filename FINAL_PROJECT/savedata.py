
import json
import requests
import tkinter as tk

class datasave:

    
        def saveserver(self):  
            
            
        # CUrrencies Rate 
            
                result = requests.get('https://exchange-rates.abstractapi.com/v1/live?api_key=056c487f42bc4a72b2482471271fcf62&base=USD')
                res = result.json()
                result_INR = json.dumps(res['exchange_rates']['INR'] , indent=2)
                result_EURO = json.dumps(res['exchange_rates']['EUR'] , indent=2)
                result_CANADA = json.dumps(res['exchange_rates']['CAD'] , indent=2)
                result_Indonesia = json.dumps(res['exchange_rates']['IDR'] , indent=2)
        # Crypto Rates
                
                resultcrypto = requests.get('http://api.coinlayer.com/live?access_key=8e332150cf67b22d9698b518dd6bc1c2')
                res_crypto = resultcrypto.json()
                result_btc = json.dumps(res_crypto['rates']['BTC'] , indent=2)
                result_eth = json.dumps(res_crypto['rates']['ETH'] , indent=2)
                result_bnb = json.dumps(res_crypto['rates']['BNB'] , indent=2)
                result_xrp = json.dumps(res_crypto['rates']['XRP'] , indent=2)
                
                self.dictLiveValues = {
                        
                        "BTC" : result_btc,
                        "ETH" : result_eth,
                        "BNB" : result_bnb,
                        "XRP" : result_xrp,

                        "INR" : result_INR,
                        "EURO" : result_EURO,
                        "CANAD D" : result_CANADA,
                        "INDO Rs" : result_Indonesia
                            
                }
                
                return self.dictLiveValues


