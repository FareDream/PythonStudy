class Student:
    @property
    def score(self):
        return self._score
    #
    # @score.setter
    # def score(self, value):
    #     self._score = value

s = Student()

s.score = 75

print(s.score)