import bs4
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from tkinter import *

root = Tk()
root.title('Bazaar')
root.geometry('500x635')

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

def get_updated():
    
    # Resetting Price Info
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")

    url = 'https://www.tgju.org/'
    try:
        page = urlopen(url)
    except:
        print('Error opening the URL')
    
    soup = bs4.BeautifulSoup(page,'html.parser')
    
    # Dollar in Rial
    dolar = soup.findAll("li", {"id": "l-price_dollar_rl"})
    for tag in dolar:
        spanTag = tag.findAll("span", {"class": "info-price"})
        for tag in spanTag:
            dolar = tag.text
    dolar = int(dolar.replace(',', ''))
    var1.set('{:,} Rials'.format(dolar))
    dollarLabel = Label(frame1, width=20, font='Helvetica 20', textvariable=var1).grid(row=0, column=1, sticky=E)
    
    # Coin in Rial
    coin = soup.findAll("li", {"id": "l-irec_future"})
    for tag in coin:
        spanTag = tag.findAll("span", {"class": "info-price"})
        for tag in spanTag:
            coin = tag.text
    coin = int(coin.replace(',', ''))
    var2.set('{:,} Rials'.format(coin))
    coinLabel = Label(frame1, width=20, font='Helvetica 20', textvariable=var2).grid(row=1, column=1, sticky=E)
    
    # Gold in Rial
    gold = soup.findAll("li", {"id": "l-geram18"})
    for tag in gold:
        spanTag = tag.findAll("span", {"class": "info-price"})
        for tag in spanTag:
            gold = tag.text
    gold = int(gold.replace(',', ''))
    var3.set('{:,} Rials'.format(gold))
    goldLabel = Label(frame1, width=20, font='Helvetica 20', textvariable=var3).grid(row=2, column=1, sticky=E)
    
    # bitcoin in Rial
    bitcoin = soup.findAll("li", {"id": "l-crypto-bitcoin"})
    for tag in bitcoin:
        spanTag = tag.findAll("span", {"class": "info-price"})
        for tag in spanTag:
            bitcoin = tag.text
    bitcoin = float(bitcoin)
    var4.set('{:,} Dollars'.format(bitcoin))
    goldLabel = Label(frame1, width=20, font='Helvetica 20', textvariable=var4).grid(row=3, column=1, sticky=E)
    
    
    


updateSign = PhotoImage(file="update72x72.png")
update_button = Button(root, image=updateSign, command=get_updated)
update_button.pack(pady=10)

frame1 = Frame(root, height=400, bd=1, relief=SUNKEN)
frame1.pack(fill=X, padx=5, pady=5)

dollarSign = PhotoImage(file="dollar.png")
dollar_label = Label(frame1, image=dollarSign).grid(row=0, column=0, sticky=W)

coinSign = PhotoImage(file="coin.png")
coin_label = Label(frame1, image=coinSign).grid(row=1, column=0, sticky=W)

goldSign = PhotoImage(file="gold.png")
gold_label = Label(frame1, image=goldSign).grid(row=2, column=0, sticky=W)

bitcoinSign = PhotoImage(file="bitcoin.png")
bitcoin_label = Label(frame1, image=bitcoinSign).grid(row=3, column=0, sticky=W)


root.mainloop()
