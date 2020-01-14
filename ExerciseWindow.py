from tkinter import Toplevel, Button, Frame, Label, Text, ttk


class ExerciseWindow(Toplevel):  # Create a window

    __ExerciseWindow__ = None
    __IsAddMode__ = True

    def __init__(self, master, isAddMode=True):
        Toplevel.__init__(self, master)

        if (isAddMode):
            self.__IsAddMode__ = True
            self.title("Add Exercise")
        else:
            self.__IsAddMode__ = False
            self.title("Edit Exercise")

        self.renderMainWindowControls()

    def renderMainWindowControls(self):
        TopFrame = Frame(self)
        button_width = 15
        button_height = 10

        TopFrame.button = Button(TopFrame, text="Save")
        TopFrame.button.configure(height=button_height, width=button_width)
        TopFrame.button.grid(row=0, column=0)

    def Save(self):
        if (self.__IsAddMode__):
            print("rt")

    def ShowDialog(self):
        self.geometry("300x200+500+100")
        self.resizable(height=False, width=False)
        self.grab_set()
        self.mainloop()
