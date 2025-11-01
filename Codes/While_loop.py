import random
import time

naruto_power = 0
sasuke_power = 0
goal = 100  # The target power to win

print("🔥 Naruto vs Sasuke: Power Training Begins! 🔥\n")

while naruto_power < goal and sasuke_power < goal:
    # Both train and gain random power between 5 and 20
    naruto_gain = random.randint(5, 20)
    sasuke_gain = random.randint(5, 20)
    
    naruto_power += naruto_gain
    sasuke_power += sasuke_gain

    print(f"Naruto trains and gains {naruto_gain} power! ⚡ (Total: {naruto_power})")
    print(f"Sasuke trains and gains {sasuke_gain} power! 🔥 (Total: {sasuke_power})")
    print("-" * 50)
    
    time.sleep(1)  # Just for fun: slows down the loop like a real battle
    
# After loop ends, check who reached the goal first
if naruto_power >= goal and sasuke_power >= goal:
    print("\nIt’s a tie! Both reached ultimate power! 💥")
elif naruto_power >= goal:
    print("\nNaruto wins! Dattebayo! 🦊💪")
else:
    print("\nSasuke wins! The power of the Sharingan prevails! 👁️🔥")
