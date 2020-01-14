from ExerciseCategory import ExerciseCategory


__ExerciseCategory__ = None


class Exercise:

    def __init__(self, name, exerciseCategory):
        self.name = name
        self.__ExerciseCategory__ = exerciseCategory
