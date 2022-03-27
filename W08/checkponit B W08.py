class GPA:

    def __init__(self):
        self.gpa = 0.0

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, gpa):
        if gpa < 0.0:
            self._gpa = 0.0
        elif gpa >= 4.0:
            self._gpa = 4.0
        else:
            self._gpa = gpa

    @property
    def letter(self):
        if self._gpa <= 0.99:
            return "F"
        elif self._gpa <= 1.99:
            return "D"
        elif self._gpa <= 2.99:
            return "C"
        elif self._gpa <= 3.99:
            return "B"
        else:
            return "A"

    @letter.setter
    def letter(self, letter):
        if letter == "F":
            self._gpa = 0.0
        elif letter == "D":
            self._gpa = 1.0
        elif letter == "C":
            self._gpa = 2.0
        elif letter == "B":
            self._gpa = 3.0
        elif letter == "A":
            self._gpa = 4.0

def main():
    s = GPA()

    print("Initial values: ")
    print("GPA: {:.2f}".format(s.gpa))
    print("Letter: {}".format(s.letter))

    value = float(input("Enter a new GPA: "))

    s.gpa = value

    print("After setting value: ")
    print("GPA: {:.2f}".format(s.gpa))
    print("Letter: {}".format(s.letter))

    letter = input("Enter a new letter: ")

    s.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(s.gpa))
    print("Letter: {}".format(s.letter))

if __name__ == "__main__":
    main()