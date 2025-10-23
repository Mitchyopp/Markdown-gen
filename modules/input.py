# I'm using the package below because its the more updated version and i found better documentation on it.
# https://inquirerpy.readthedocs.io/en/latest/

class input:
    def __init__(self):
        self.questions = [
            { "type": "input", "message": "README title:", "name": "title" },
            { "type": "input", "message": "README description:", "name": "description" },
            { "type": "input", "message": "README installation:", "name": "installation" },
            { "type": "input", "message": "README usage:", "name": "usage" },
            {
                "type": "list",
                "message": "Select a lisence type.",
                "choices": [ "License 1", "License 2", "License 3" ],
                "name": "license"
            },
            { "type": "confirm", "message": "confirm", "name": "confirm" },
            { "type": "input", "message": "README author:", "name": "author" },
            { "type": "input", "message": "README contact info:", "name": "contact" },
            { "type": "input", "message": "Markdown name:", "name": "file_name" },
    ]
