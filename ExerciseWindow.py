from tkinter import Toplevel, Button, Frame, Label, Text, ttk
from ExerciseCategory import ExerciseCategory


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
        TopFrame = Frame(self, name="topFrame")
        TopFrame.grid(row=0, column=0)

        Label(TopFrame, text="Exercise").grid(row=1, column=1)
        Text(TopFrame, name="txtExercise", height=1,
             width=30).grid(row=1, column=2)
        Label(TopFrame, text="Category").grid(row=2, column=1)
        ttk.Combobox(TopFrame, name="cboCategory", height=1,
                     width=28, values=ExerciseCategory.getExerciseCategories()).grid(row=2, column=2)
        b = Button(TopFrame, text="Save", command=self.Save)
        b.configure(height=1, width=5)
        b.grid(row=3, column=1)

    def Save(self):
        if (self.__IsAddMode__):
            print("rt")

    def ShowDialog(self):
        self.geometry("300x80+500+100")
        self.resizable(height=False, width=False)
        self.grab_set()
        self.mainloop()
