import random
import string
import pyperclip

apps = ["Tiger's Treasure Quest", "Fortune Feline Frenzy", "Tiger's Luck Odyssey"]
server_type = "Policy+TD ATR"
parameters = ["ad_id", "vers", "local", "id", "mod", "refer"]

result = ""

def create_random_word():
    word = ""
    word_length = random.randint(5, 10)
    random_number_position = random.randint(0,word_length-1)
    for l in range(word_length):
        if random.randint(0,1) == 1:
            word += random.choice(string.ascii_uppercase)
        else:
            word += random.choice(string.ascii_lowercase)

        if l == random_number_position:
            word += str(random.randint(0,10))
    return word

for app_name in apps:
    result += "назва додатку = " + app_name + "\n"
    result += "тип сервера = " + server_type + "\n"
    result += "файл = " + create_random_word() +".php" + "\n"
    for parameter in parameters:
        result += parameter + " = " + create_random_word() + "\n"
        if parameter == parameters[len(parameters)-1]:
            result += "\n"

print(result)

pyperclip.copy(result)
print("Copied to your clipboard")