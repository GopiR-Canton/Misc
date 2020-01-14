import datetime
import tkinter
import tkinter.messagebox
import Config
from Exercise import Exercise
from ExerciseCategory import ExerciseCategory
from ExerciseWindow import ExerciseWindow
from Logger import Logger

__Logger__ = None
__LOGFILE__ = Config.LogFile
__MSGBOXTITLE__ = "Message"
__MainWindow__ = None
__Exercises__ = []


def initlog(filename):
    logstr = "Log initialized: " + datetime.datetime.now().strftime(
        "%a, %d %b %Y %H:%M:%S")
    __Logger__.logEntry(filename, logstr)


def newMenuClicked():
    tkinter.messagebox.showinfo(__MSGBOXTITLE__, "The New menu was clicked!")


def buildMainWindowMenubar():
    __Logger__.logEntry(__LOGFILE__, "Starting to build menubar...")
    menuBar = tkinter.Menu(__MainWindow__)

    fileMenu = tkinter.Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newMenuClicked)
    fileMenu.add_command(label="Exit", command=__MainWindow__.quit)
    menuBar.add_cascade(label="File", menu=fileMenu)

    __MainWindow__.config(menu=menuBar)
    __Logger__.logEntry(__LOGFILE__, "Finished building menubar")


def createExercise(exerciseName, exerciseCategory):
    __Exercises__.append(
        Exercise(exerciseName, ExerciseCategory(exerciseCategory)))


def listExercises(printToLog):
    for exercise in __Exercises__:

        strExercise = "Exercise: " + exercise.name + \
            ", Category: " + exercise.__ExerciseCategory__.name

        if printToLog:
            __Logger__.logEntry(__LOGFILE__, strExercise)
        else:
            print(strExercise)  # Test change


def loadExercisesToList():
    lstExers = __MainWindow__.nametowidget(
        "topFrame").nametowidget("lstExercises")
    position = 0

    for exercise in __Exercises__:
        lstExers.insert(position,
                        exercise.name + " (" + exercise.__ExerciseCategory__.name + ")")
        position += 1


def renderMainWindowControls():
    TopFrame = tkinter.Frame(__MainWindow__, name="topFrame")
    TopFrame.grid(row=0, column=0)
    TopFrame.pack(side="top", fill="both", expand=True)

    tkinter.Label(TopFrame, name="lblExercises",
                  text="Exercises").grid(row=1, column=0)

    lst = tkinter.Listbox(
        TopFrame, name="lstExercises", selectmode="SINGLE")
    lst.bind('<<ListboxSelect>>', lstExercises_ItemSelected)
    lst.grid(row=2, column=0, sticky="w")

    tkinter.Button(TopFrame, name="btnAddExercise",
                   text="Add Exercise...", command=btnAddExercise_Click).grid(row=3, column=0)
    tkinter.Button(TopFrame, name="btnEditExercise", state="disabled",
                   text="Edit Exercise...", command=btnEditExercise_Click).grid(row=3, column=1)


def lstExercises_ItemSelected(event):
    widget = event.widget
    selection = widget.curselection()
    # value = widget.get(selection[0])
    if (selection[0] >= 0):
        __MainWindow__.nametowidget("topFrame").nametowidget(
            "btnEditExercise").config(state="normal")


def btnAddExercise_Click():
    addWindow = ExerciseWindow(__MainWindow__, True)
    addWindow.ShowDialog()


def btnEditExercise_Click():
    addWindow = ExerciseWindow(__MainWindow__, False)
    addWindow.ShowDialog()


try:
    __Logger__ = Logger()
    initlog(__LOGFILE__)
    __Logger__.LogStart(__LOGFILE__)
    __Logger__.logEntry(__LOGFILE__, "Loading Main window...")

    __MainWindow__ = tkinter.Tk()
    __MainWindow__.title("First Python App")
    __MainWindow__.geometry("500x500+500+100")

    buildMainWindowMenubar()

    renderMainWindowControls()

    __Logger__.logEntry(__LOGFILE__, "Creating exercises...")

    createExercise("Squat", "Weightlifting")
    createExercise("Deadlift", "Weightlifting")
    createExercise("Military Press", "Weightlifting")
    createExercise("Prowler push/pull", "Cardio")
    createExercise("Treadmill Walk", "Cardio")

    __Logger__.logEntry(__LOGFILE__, "Finished creating exercises")

    __Logger__.logEntry(__LOGFILE__, "Printing exercises...")

    listExercises(False)
    loadExercisesToList()

    __Logger__.logEntry(__LOGFILE__, "Finished printing exercises...")

    __MainWindow__.mainloop()

    __Logger__.logEntry(__LOGFILE__, "Main window closed")
    __Logger__.LogEnd(__LOGFILE__)

except PermissionError:
    tkinter.messagebox.showerror(
        __MSGBOXTITLE__, "Permission denied, man. Ok?")
