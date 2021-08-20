from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from tkinter import *
import webbrowser

# setting the UI
main = Tk()
main.geometry("600x500")
main.title("Carros en venta")
title = Label(main, text="Carros de venta en Corotos.com.do", font=('Arial', 12, "bold"))
title.grid(row=0, column=0, columnspan=3)

#Add a line for each item
def add_car_button(brand, price, link):
    global row
    link_button = Button(text="Open", command=lambda: navigate(link))
    l_brand = Label(main, text=brand, width=50)
    l_price = Label(main, text=price, width=20)
    l_brand.grid(row=row, column=0)
    l_price.grid(row=row, column=1)
    link_button.grid(row=row, column=2)
    row += 1

#browse to the page of the specific car
def navigate(link):
    webbrowser.get()
    webbrowser.open('corotos.com.do/' + link)

row = 1

try:
    page_html = urlopen('https://www.corotos.com.do/sc/veh%C3%ADculos/carros').read()  # getting the list of items
    page_soup = soup(page_html, 'html.parser')  # parsing the list of items as HTML
    cars = page_soup.findAll("div", {"class": "listing__item"})  # selecting all cars listed

    #add a line for each car 
    for car in range(5):
        brand = cars[car].find("h3", {"class": "item__title"}).text  # get the brand/model of the car
        price = cars[car].find("a", {"class": "item__price"}).text  # get  the price of the car
        link = cars[car].find('a').get('href')  # get the link to the car selling page
        add_car_button(brand, price, link)
except:
    #error message if not able to load the page info
    l_brand = Label(main, text="Problemas cargando la información")
    l_brand.grid(row=row, column=0)
    
main.mainloop()
