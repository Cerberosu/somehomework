from tkinter import Entry, Button, Tk, Label
from Config import Config
from Object import Object as ob
from OutPut import Output

c = Config()
field_list = c.field_list
ou = Output()
row = 0

'''Creating window and its objects'''


class Window(object):

    def __init__(self):
        self.name = None
        self.window = None
        self.lbl = None
        self.txt = None
        self.save_btn = None
        self.quit_btn = None
        self.input_list = []
        self.objectList = []
        self.temp_dict = {}

    def show(self):
        self.create_window()
        self.widgets()
        self.save_button()
        self.exit_button()
        self.window.mainloop()

    def create_window(self):
        self.window = Tk()
        self.window.title("Main Window")
        self.window.geometry("450x150")

    def widgets(self):
        global row
        for item in field_list:
            # labels
            self.lbl = Label(self.window, text=item["label"])
            self.lbl.grid(column=0, row=row)
            # entries
            self.txt = Entry(self.window, width=60)
            self.txt.grid(column=1, row=row)
            self.input_list.append(ob(item["field_name"], self.txt))
            row += 1

    def save_button(self):
        global row
        # save button
        self.save_btn = Button(self.window)
        self.save_btn["text"] = "Save"
        self.save_btn["command"] = self.__save_handler
        self.save_btn.grid(column=0, row=row)

    def exit_button(self):
        global row
        # exit button
        self.quit_btn = Button(self.window, text="Exit", fg="red", command=self.__quit_handler)
        self.quit_btn.grid(column=1, row=row)

    # save event

    def __save_handler(self):
        self.temp_dict = {}
        for item in self.input_list:
            self.temp_dict.update({item.get_key(): item.value.get()})
            item.value.delete(0, "end")
        self.objectList.append(self.temp_dict)

    # quit event

    def __quit_handler(self):
        ou.create_json(self.objectList)
        self.window.destroy()
