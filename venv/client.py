from tkinter import *
import tkinter as tk
from tkinter import ttk

class client():
    def __init__(self, converter):
        self.window=Tk()
        self.window.title = 'Currency Converter'
        self.currency_converter = converter


        self.window.geometry("2000x1000")
        self.window.header = Label(self.window, text='Welcome to Real Time Currency Convertor', fg='red', relief=tk.RAISED,
                                 borderwidth=3)
        self.window.header.config(font=('Courier', 15, 'bold'))
        self.window.date = Label(self.window,
                                text=f"1 Indian Rupee equals = {self.currency_converter.convert('INR', 'USD', 1)} USD \n Date : {self.currency_converter.date}",
                                relief=tk.GROOVE, borderwidth=5)
        self.window.header.place(x=600, y=5)
        self.window.date.place(x=700, y=50)

        valid = (self.window.register(self.restrictNumberOnly), '%d', '%P')
        self.window.amount = Entry(self.window, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key', validatecommand=valid)
        self.window.converted_amount_field_label = Label(self.window, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)


        self.window.from_currency = StringVar(self.window)
        self.window.from_currency.set("INR")
        self.window.to_currency = StringVar(self.window)
        self.window.to_currency.set("USD")
        font = ("Courier", 12, "bold")
        self.window.option_add('*TCombobox*Listbox.font', font)
        self.window.from_currency_dropdown = ttk.Combobox(self.window, textvariable=self.window.from_currency,
                                                   values=list(self.currency_converter.data.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.window.to_currency_dropdown = ttk.Combobox(self.window, textvariable=self.window.to_currency,
                                                 values=list(self.currency_converter.data.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)

        self.window.from_currency_dropdown.place(x=600, y=120)
        self.window.amount.place(x=600, y=150)
        self.window.to_currency_dropdown.place(x=900, y=120)
        self.window.converted_amount_field_label.place(x=900, y=150)
        self.window.convert_button = Button(self.window, text="Convert", fg="black", command=self.perform)
        self.window.convert_button.config(font=('Courier', 10, 'bold'))
        self.window.convert_button.place(x=750, y=200)

    def perform(self):
        amount = float(self.window.amount.get())
        from_curr = self.window.from_currency.get()
        to_curr = self.window.to_currency.get()
        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)
        self.window.converted_amount_field_label.config(text=str(converted_amount))

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))
