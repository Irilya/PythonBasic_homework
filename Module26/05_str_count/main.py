import os


def python_files_code(direct) -> int:
    lines = 0
    for root, dirs, files in os.walk(direct):
        for file in files:
            if file.endswith('.py'):
                name = os.path.join(root, file)
                with open(name, 'r', encoding="utf-8") as file_code:
                    for line in file_code:
                        if not line.startswith("\n") and not line.startswith('#'):
                            lines += 1
    return lines


lines_count = python_files_code(r"C:\SkillBox\Python_Basic\Python_Basic\Module24")
print('Всего непустых строк - ', lines_count)
