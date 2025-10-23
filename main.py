from modules.input import TakeInput
from modules.output import ShowOutput
from InquirerPy import prompt

if __name__ == "__main__":
    UserInput = TakeInput().PrintQuestions()
    ShowOutput(UserInput)
