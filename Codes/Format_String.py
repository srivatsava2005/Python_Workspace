name = "Naruto Uzumaki"
village = "Hidden Leaf"
dream = "become Hokage"

intro = "My name is {} from the {} Village, and I will {} one day!".format(name, village, dream)
print(intro)

quote = "{1} says, 'I won't run away anymore. That's my {0}!'".format("ninja way", "Naruto")
print(quote)

message = "Sasuke’s brother is {brother}, and he is from the {clan} clan.".format(brother="Itachi", clan="Uchiha")
print(message)

name = "Kakashi"
title = "Copy Ninja"
students = ["Naruto", "Sasuke", "Sakura"]

print(f"{name}, the {title}, trains {students[0]}, {students[1]}, and {students[2]}.")

chakra_level = 9876.54321
print(f"Naruto’s chakra level is {chakra_level:.2f}")

print(f"{'Character':<10} | {'Village':^15} | {'Rank':>10}")
print(f"{'-'*40}")
print(f"{'Naruto':<10} | {'Leaf':^15} | {'Genin':>10}")
print(f"{'Gaara':<10} | {'Sand':^15} | {'Kazekage':>10}")
