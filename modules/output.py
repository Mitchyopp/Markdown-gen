class ShowOutput:
    def __init__(self):
        # https://www.w3schools.com/python/python_file_write.asp
        with open(f"{file_name}.md", "w") as file:
            file.write(f"""
        # {title}

        ---

        # description
        {description}

        ---

        # installation
        {installation}

        ---

        # usage
        {usage}

        ---

        # license
        {license}

        ---

        # author & contact
        {author} | {contact}""")
            print(f"{file_name} updated!")
