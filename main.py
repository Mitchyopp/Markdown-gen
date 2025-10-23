import modules.input
import modules.output
from InquirerPy import prompt


# https://www.w3schools.com/python/python_file_write.asp
with open(f"{file_name}.md", "w") as file:
    file.write(f"""
# {title}

---

# Description
{description}

---

# installation
{installation}

---

# Usage
{usage}

---

# License
{license}

---

# Author & Contact
{author} | {contact}""")
    print(f"{file_name} updated!")
