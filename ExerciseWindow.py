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
        TopFrame.grid(row=0, column=0)
        TopFrame.pack(side="top", fill="both", expand=True)

        b = Button(TopFrame, text="Save", command=self.Save)
        b.configure(height=2, width=5)
        b.grid(row=0, column=1)

    def Save(self):
        if (self.__IsAddMode__):
            print("rt")

    def ShowDialog(self):
        self.geometry("300x200+500+100")
        self.resizable(height=False, width=False)
        self.grab_set()
        self.mainloop()
