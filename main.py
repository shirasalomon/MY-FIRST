
from server import server
from client import client
from tkinter import *



if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = server(url)
    client(converter)
    mainloop()
