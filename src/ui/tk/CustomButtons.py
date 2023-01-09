import tkinter

import customtkinter


class CustomEntry(customtkinter.CTkEntry):
    '''A Entry widget that provides String Var'''

    def __init__(self, master=None, placeholder_text=None, **kwargs):
        self.var = tkinter.StringVar(master, placeholder_text)
        customtkinter.CTkEntry.__init__(self, master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set


class DayButton(customtkinter.CTkButton):
    def __init__(self, master=None, text=None, **kwargs):
        self.var = tkinter.StringVar(master, text)
        customtkinter.CTkButton.__init__(self, height=30, width=30, master=master, text=text, **kwargs)
        self.get, self.set = self.var.get, self.var.set
