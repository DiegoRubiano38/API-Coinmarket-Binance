from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from binance.client import Client

#------------------------------------------------------------------------------

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f5b25f40-f410-4583-8ec0-6146f31a794a',
}

session = Session()
session.headers.update(headers)

response = session.get(url, headers=headers).json()

#------------------------------------------------------------------------------

api_key = '*******************************************************'
api_secret = '*******************************************************'
client = Client(api_key, api_secret)

#------------------------------------------------------------------------------

bandera = 0
dinero_total = 0
consulta_t = ("SI","si","Si","sI")
consulta = "si"

while (consulta in consulta_t):
  counter = 0
  codigo = input("Digite el código de criptomoneda: ")
  for i in range(len(response["data"])):
    counter+=1
    if (codigo==response["data"][i]["symbol"]):
      bandera = 1
      print("Moneda valida, su nombre es: %s"%response["data"][i]["name"])
      cantidad = float(input("Digite la cantidad de moneda: "))
      price = client.get_avg_price(symbol=codigo+"USDT")
      dinero_total = float(price["price"])*cantidad
      print("Posee: %.1f dolares"%dinero_total)
      counter-=1
  if counter == (len(response["data"])):
    print("Moneda no encontrada, ingrese otra")
  
  consulta = input("¿Desea realizar otra consulta? ")
