from InquirerPy import prompt
# I'm using the package below because its the more updated version and i found better documentation on it.
# https://inquirerpy.readthedocs.io/en/latest/

class TakeInput:
    def __init__(self):
        self.questions = [
            { "type": "input", "message": "Markdown title:", "name": "title" },
            { "type": "input", "message": "Markdown description:", "name": "description" },
            { "type": "input", "message": "Markdown installation:", "name": "installation" },
            { "type": "input", "message": "Markdown usage:", "name": "usage" },
            {
                "type": "list",
                "message": "Select a lisence type.",
                "choices": [ "MIT license", "GNU GPLv3", "None" ],
                "name": "license"
            },
            { "type": "confirm", "message": "confirm", "name": "confirm" },
            { "type": "input", "message": "Markdown author:", "name": "author" },
            { "type": "input", "message": "Markdown contact info:", "name": "contact" },
            { "type": "input", "message": "Markdown name:", "name": "file_name" },
    ]
    
    def PrintQuestions(self):
        result = prompt(self.questions)
        return result
