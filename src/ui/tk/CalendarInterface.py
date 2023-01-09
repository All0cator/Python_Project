from PIL import Image
from CustomButtons import DayButton, CustomEntry
import customtkinter
from datetime import datetime

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def findKey(dict, value):
    for x, y in dict.items():
        if y == value:
            return x


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.current_day = datetime.now().day

        self.month_dict = {1: 'January', 2: 'February', 3: 'March',
                           4: 'April', 5: 'May', 6: 'June',
                           7: 'July', 8: 'August', 9: 'September',
                           10: 'October', 11: 'November', 12: 'December'}

        """ configure window """
        self.title("Calendar")
        self.geometry(f"{300}x{300}")
        self.resizable(False, False)

        """ Main Calendar frame """
        self.calendar_frame = customtkinter.CTkFrame(self, width=270, height=270, corner_radius=5)
        self.calendar_frame.grid(row=0, column=0, padx=(15, 15), pady=(14, 16), sticky="nsew")
        self.calendar_frame.grid_propagate(False)
        self.calendar_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, minsize=38)  # choose appropriate size
        self.calendar_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1, minsize=30)  # here minsize is optional

        """ Year Label """
        self.year_entry = CustomEntry(self.calendar_frame, width=45, height=25,
                                      placeholder_text=datetime.now().year,
                                      font=customtkinter.CTkFont(size=10, weight="bold"))
        self.year_entry.grid(row=0, column=1, columnspan=3, padx=(20, 0))
        self.year_entry.bind("<Return>", self.validate)

        """ Month Label """
        self.month_entry = CustomEntry(self.calendar_frame,
                                       width=130,
                                       height=25,
                                       font=customtkinter.CTkFont(size=9, weight="bold"),
                                       placeholder_text=self.month_dict[datetime.now().month]
                                       )
        self.month_entry.grid(row=0, column=0, padx=(10, 2), columnspan=2)
        self.month_entry.configure(state="disabled")

        """ Month Switch Buttons """
        self.back_button = customtkinter.CTkButton(self.calendar_frame,
                                                   width=15,
                                                   height=15,
                                                   text="",
                                                   image=customtkinter.CTkImage(Image.open("src/ui/tk/left-arrow.png"),
                                                                                size=(15, 15)),
                                                   fg_color="#2b2b2f",
                                                   border_width=2,
                                                   command=self.backwardDate
                                                   )
        self.back_button.grid(row=0, column=4, padx=(10, 2), columnspan=2)

        self.forward_button = customtkinter.CTkButton(self.calendar_frame,
                                                      width=15,
                                                      height=15,
                                                      text="",
                                                      image=customtkinter.CTkImage(Image.open("src/ui/tk/right-arrow.png"),
                                                                                   size=(15, 15)),
                                                      fg_color="#2b2b2f",
                                                      border_width=2,
                                                      command=self.forwardDate
                                                      )
        self.forward_button.grid(row=0, column=5, padx=(10, 2), columnspan=2)

        """
        self.button_1 = DayButton(self.calendar_frame, "31", hover_color="white", border_color="black", border_width=2,
                                  anchor="center")
        self.button_1.grid(row=7, column=6)
        """
        """ Days Labels """
        self.monday_label = customtkinter.CTkLabel(self.calendar_frame, text="Mo", width=30, height=30,
                                                   font=customtkinter.CTkFont(size=10, weight="bold"))
        self.monday_label.grid(row=1, column=0)

        self.tuesday_label = customtkinter.CTkLabel(self.calendar_frame, text="Tu", width=30, height=30,
                                                    font=customtkinter.CTkFont(size=10, weight="bold"))
        self.tuesday_label.grid(row=1, column=1)
        self.wednesday_label = customtkinter.CTkLabel(self.calendar_frame, text="We", width=30, height=30,
                                                      font=customtkinter.CTkFont(size=10, weight="bold"))
        self.wednesday_label.grid(row=1, column=2)
        self.thursday_label = customtkinter.CTkLabel(self.calendar_frame, text="Th", width=30, height=30,
                                                     font=customtkinter.CTkFont(size=10, weight="bold"))
        self.thursday_label.grid(row=1, column=3)
        self.friday_label = customtkinter.CTkLabel(self.calendar_frame, text="Fr", width=30, height=30,
                                                   font=customtkinter.CTkFont(size=10, weight="bold"))
        self.friday_label.grid(row=1, column=4)
        self.saturday_label = customtkinter.CTkLabel(self.calendar_frame, text="Sa", width=30, height=30,
                                                     font=customtkinter.CTkFont(size=10, weight="bold"))
        self.saturday_label.grid(row=1, column=5)
        self.sunday_label = customtkinter.CTkLabel(self.calendar_frame, text="Su", width=30, height=30,
                                                   font=customtkinter.CTkFont(size=10, weight="bold"))
        self.sunday_label.grid(row=1, column=6)

    """ FUNCTIONS """

    def validate(self, *args):
        x = self.year_entry.var.get()
        if len(x) > 4:
            self.year_entry.var.set(datetime.now().year)
            self.month_entry.var.set(self.month_dict[int(datetime.now().month)])
            return
        if not x.isdigit():
            z = ''.join([i for i in x if i.isdigit()])
            if z == '' or (z := int(z)) < 0:
                self.year_entry.var.set(datetime.now().year)
                self.month_entry.var.set(self.month_dict[int(datetime.now().month)])
            else:
                self.year_entry.var.set(z)
        self.syncValues()

    def forwardDate(self):
        if self.current_year + 1 > 9999 and self.current_month == 12:
            return
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
            self.year_entry.var.set(self.current_year)
        else:
            self.current_month += 1
        self.month_entry.var.set(self.month_dict[self.current_month])

    def backwardDate(self):
        if self.current_year - 1 < 0 and self.current_month == 1:
            return
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
            self.year_entry.var.set(self.current_year)
        else:
            self.current_month -= 1
        self.month_entry.var.set(self.month_dict[self.current_month])

    def syncValues(self):
        self.current_month = findKey(self.month_dict, self.month_entry.var.get())
        self.current_year = int(self.year_entry.var.get())


app = App()
app.mainloop()
