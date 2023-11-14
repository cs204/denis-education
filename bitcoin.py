import requests
import sys
import json


if __name__ == "__main__":
        if len(sys.argv) == 1:
             print("Пропущен аргумент командной строки")
        elif len(sys.argv) == 2:
            try:
                 input = float(sys.argv[1])
                 try:
                    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
                    resp = req.text
                    json_resp = json.loads(resp)
                    bitcoin = json_resp['bpi']
                    bitcoin_usd = bitcoin['USD']
                    bitcoin_rate = bitcoin_usd['rate_float']
                    result = bitcoin_rate * input
                    print(f"${result:,.4f}")
                 except requests.RequestException:
                      sys.exit("Ошибка в запросе")
            except ValueError:
                 sys.exit("Аргумент командной строки не число")