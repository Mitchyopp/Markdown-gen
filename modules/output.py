class ShowOutput:
    def __init__(self, result):
        # https://www.w3schools.com/python/python_file_write.asp
        with open(f"{result["file_name"]}.md", "w") as file:
            file.write(f"""
# {result["title"]}

---

# description
{result["description"]}

---

# installation
{result["installation"]}

---

# usage
{result["usage"]}

---

# license
{result["license"]}

---

# author & contact
{result["author"]} | {result["contact"]}""")
            print(f"{result["file_name"]} updated!")
