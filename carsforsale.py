from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from tkinter import *
import webbrowser

main = Tk()
main.geometry("550x400")
main.configure(bg = "#313186")
main.title("Cars")
title = Label(main,text = "Latest cars uploaded to Corotos.com.do", font = ('Arial',12,"bold"),fg = "white",bg = "#313186")
title.grid(row = 0, column = 0, columnspan = 4)


my_url = 'https://www.corotos.com.do/sc/veh%C3%ADculos/carros'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'html.parser')

def navigate():
    webbrowser.get()
    webbrowser.open('corotos.com.do/' + link)

links = []
cars = page_soup.findAll("a",{"class":"listing__item"})
row = 1

for car in cars:
    brand = car.find("h3", {"class":"item__title"}).text
    price = car.find("h3", {"class":"item__price"}).text
    link = car.attrs['href']
    links.append(link)
    hidden = Label(main, text = link ,width = 2,fg = "#313186", bg = "#313186")

    link_button = Button(text = "Open", command = navigate , padx = 15)

    l_brand = Label(main, text = "Marca: " + brand, bg = "#313186", fg = "white")
    l_price = Label(main, text = "Precio: " + price, bg = "#313186", fg = "white")

    l_brand.grid(row = row, column = 0)
    l_price.grid(row = row, column = 1)
    hidden.grid(row = row, column = 2)
    link_button.grid(row = row, column = 3)
    row += 1




main.mainloop()
