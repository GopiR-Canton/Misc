import datetime


class Logger:

    def LogStart(self, file):
        with open(file, "a+") as f:
            f.write("Starting...\n")

    def LogEnd(self, file):
        with open(file, "a+") as f:
            f.write("Ending...\n")

    def logEntry(self, file, str):
        with open(file, "a+") as f:
            f.write(str + "\n")
