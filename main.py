from InquirerPy import prompt
# I'm using the package below because its the more updated version and i found better documentation on it.
# https://inquirerpy.readthedocs.io/en/latest/

questions = [
        { "type": "input", "message": "README title:" },
        { "type": "input", "message": "README description:" },
]

result = prompt(questions)
title = result[0]
description = result[1]
print(title)
print(description)
