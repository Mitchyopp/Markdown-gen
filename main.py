from InquirerPy import prompt
# I'm using the package below because its the more updated version and i found better documentation on it.
# https://inquirerpy.readthedocs.io/en/latest/

questions = [
        { "type": "input", "message": "README title:" },
        { "type": "input", "message": "README description:" },
        { "type": "input", "message": "README installation:" },
        { "type": "input", "message": "README usage:" },
        {
            "type": "list",
            "message": "Select a lisence type.",
            "choices": [ "License 1", "License 2", "License 3" ],
        },
        { "type": "confirm", "message": "confirm" },
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

# https://www.w3schools.com/python/python_file_write.asp
with open("README.md", "w") as file:
    file.write(f"""
               {title}
               ---
               {description}
               ---
               {installation}
               ---
               {usage}
               ---
               {lisence}
               ---
               {author} | {contact}""")
    print("README updated!")
