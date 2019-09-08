import requests
import json
import numpy as np
import pandas as pd

def get_data(ticker,startDate,endDate):
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_SECRET_ID'

    auth_data = {
        "grant_type"    : "client_credentials",
        "client_id"     : client_id,
        "client_secret" : client_secret,
        "scope"         : "read_product_data
    }

    session = requests.Session()

    auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data = auth_data)
    access_token_dict = json.loads(auth_request.text)
    access_token = access_token_dict["access_token"]

    session.headers.update({"Authorization":"Bearer "+ access_token})

    request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

    request_query = {
            "where": {
                    "ticker" : ticker
                    },
            "startDate": startDate,
            "endDate": endDate
    }
    req = session.post(url = request_url, json = request_query)
    data = json.loads(req.text)
    data = data['data']
    df = pd.DataFrame(data)
    print(df)
    return df

assets = pd.read_csv("marquee_companies.csv")
tickers = assets['ticker']
gsids = assets['gsid']

og = pd.DataFrame()
for i in range(0,len(tickers)):
    print(i)
    df = get_data(tickers[i],"2000-01-01","2019-09-06")
    og = pd.concat([og,df])
og.to_csv("marquee_data.csv")