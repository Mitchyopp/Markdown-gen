from InquirerPy import prompt
# I'm using the package below because its the more updated version and i found better documentation on it.
# https://inquirerpy.readthedocs.io/en/latest/

questions = [
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

result = prompt(questions)
# title = result[0]
title = result["title"]
description = result["description"]
installation = result["installation"]
usage = result["usage"]
license = result["license"]
author = result["author"]
contact = result["contact"]
file_name = result["file_name"]
print(title)
print(description)
print(installation)
print(usage)
print(license)
print(author)
print("contact")
print(contact)
print("file")
print(file_name)

# https://www.w3schools.com/python/python_file_write.asp
with open(f"{file_name}.md", "w") as file:
    file.write(f"""
{title}
---
{description}
---
{installation}
---
{usage}
---
{license}
---
{author} | {contact}""")
    print(f"{file_name} updated!")
