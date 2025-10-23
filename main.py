from InquirerPy import prompt
# I'm using the package below because its the more updated version and i found better documentation on it.
# https://inquirerpy.readthedocs.io/en/latest/

questions = [
        { "type": "input", "message": "README title:" },
        { "type": "input", "message": "README description:" },
        { "type": "input", "message": "README installation:" },
        { "type": "input", "message": "README usage:" },
        { "type": "input", "message": "README lisence:" },
        { "type": "input", "message": "README author:" },
        { "type": "input", "message": "README contact info:" },
]

result = prompt(questions)
title = result[0]
description = result[1]
installation = result[2]
usage = result[3]
lisence = result[4]
author = result[5]
contact = result[6]
print(title)
print(description)
print(installation)
print(usage)
print(lisence)
print(author)
print(contact)
