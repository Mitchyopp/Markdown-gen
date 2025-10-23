class output:
    def __init__(self):
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
