# Made by GottusJ
import random
from simple_chalk import chalk

print(chalk.blue("\n=== Password Generator ==="))

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890<>/?.,"

number = input(chalk.green("Amount of passwords generated: "))
number = int(number)

length = input(chalk.green("Password length: "))
length = int(length)

print(chalk.blue("\nPasswords Generated:"))

for n in range(number):
    psw = ""
    for l in range(length):
        psw += random.choice(chars)
    print(chalk.yellow(psw))

print("\n")
