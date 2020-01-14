class ExerciseCategory:

    @staticmethod
    def getExerciseCategories():
        ECs = []
        ECs.append("Weightlifting")
        ECs.append("Cardio")
        ECs.append("Yoga")
        return ECs

    def __init__(self, name):
        self.name = name
