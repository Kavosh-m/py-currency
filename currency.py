import requests
from bs4 import BeautifulSoup as bs
from tkinter import *

root = Tk()
root.title('Dollor to Toman')
root.geometry('700x700')

var = StringVar()
var2 = StringVar()

def get_updated_dollor_value_in_rial():
    url = 'https://www.tgju.org/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    global dolar
    dolar = soup.findAll("li", {"id": "l-price_dollar_rl"})
    for tag in dolar:
        spanTag = tag.findAll("span", {"class": "info-price"})
        for tag in spanTag:
            dolar = tag.text
    dolar = int(dolar.replace(',', ''))
    var.set('At this moment, 1 USD is {} rial'.format(dolar))

def toman():
    label4 = Label(frame1, font='Times 12', textvariable=var2)
    label4.grid(row=2, column=3, sticky=W+E)
    var2.set('{:,} Toman'.format((dolar // 10) * int(entry1.get())))

get_dollor_button = Button(root, text='Get Dollor Value', bd=3, bg='black',
                           fg='yellow', font='Times 12', command=get_updated_dollor_value_in_rial)
get_dollor_button.pack()

frame1 = Frame(root, height=400, bd=1, relief=SUNKEN)
frame1.pack(fill=X, padx=5, pady=5)

label = Label(frame1, fg='#00b300', font='Times 15', textvariable=var)
label.grid(row=0, column=0, sticky=W+E)

label2 = Label(frame1, text='Dollor to Toman:', font='Times 12')
label2.grid(row=1, column=0, sticky=W)

entry1 = Entry(frame1)
entry1.grid(row=2, column=0, sticky=W+E)

label3 = Label(frame1, text='Dollor', font='Times 12')
label3.grid(row=2, column=1, sticky=W+E)

usd_to_toman = Button(frame1, text='is', bd=3, font='Times 13', command=toman)
usd_to_toman.grid(row=2, column=2, sticky=W+E)



root.mainloop()
