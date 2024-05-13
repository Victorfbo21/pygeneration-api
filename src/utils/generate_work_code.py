import random

def generate_work_code():
    code = ""
    for _ in range(6):
        code += str(random.randint(0, 9))

    return code