# import streamlit as s
# import pandas as pd
# import matplotlib.pyplot as plt
# s.title("Stock Marketing App")
# s.write("Fetch and visualize stock price data")
# s.image("https://images.pexels.com/photos/31009096/pexels-photo-31009096.jpeg")

# data = pd.DataFrame({'symbol':['AAPL','OANDA','AMZN','TSLA','FXCM','SPY','BINANCE','ARKK'],'PRICE':[163.33,1.13419,2898.89,950.545,1.88693,440.96,38069.18,72.25]})

# plt.plot(data["symbol"],data["PRICE"])
# s.pyplot(plt)


import streamlit as s 
import qrcode 
s.title("QRCode Generator")
url_name = s.text_input("Enter URL : ")
file_name = s.text_input("Enter file name : ")

if s.button("submit"):
    qr_code = qrcode.make(url_name)
    qr_code.save(f"{file_name}.png")
    s.success("qrcode genertaed ")
    s.image(f"{file_name}.png")
