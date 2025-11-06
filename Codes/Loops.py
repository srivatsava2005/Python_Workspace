# bleach_loops_demo.py
# Python loops all-in-one using Bleach anime references.

# Sample data
shinigami = ["Ichigo Kurosaki", "Rukia Kuchiki", "Renji Abarai", "Byakuya Kuchiki"]
arrancar = ["Ulquiorra", "Grimmjow", "Nnoitra", "Coyote Starrk"]
captains = {
    "Gotei 13": ["Unohana", "Soi Fon", "Byakuya", "Kyoraku"],
    "Espada": ["Starrk", "Baraggan", "Tier", "Nnoitra"]
}

print("=== 1) for-loop over list ===")
for s in shinigami:
    print(f"- {s}")
# Output: list of shinigami

print("\n=== 2) for-loop with enumerate (index + value) ===")
for i, s in enumerate(shinigami, start=1):
    print(f"{i}. {s}")
# Shows indices starting from 1

print("\n=== 3) for-loop with zip (pairing teams) ===")
# Pair first 3 shinigami with first 3 arrancar (battle pairs)
for s, a in zip(shinigami, arrancar):
    print(f"{s} vs {a}")
# If sequences differ in length, zip stops at shortest

print("\n=== 4) iterating over dict (keys, values, items) ===")
print("Gotei 13 captains by squad:")
for squad, members in captains.items():
    print(f"{squad}: {len(members)} captains -> {', '.join(members)}")

print("\n=== 5) while-loop (training until power threshold) ===")
# Ichigo trains until power reaches threshold
power = 20
threshold = 80
session = 0
while power < threshold:
    session += 1
    power += 12  # training boost per session
    print(f"Session {session}: Ichigo power = {power}")
# Use while for repeated actions until a condition is met

print("\n=== 6) break and continue inside loop ===")
enemies = ["Hollows", "Arrancar", "Espada", "Aizen"]
for e in enemies:
    if e == "Arrancar":
        print("Arrancar found — skip (gather info).")
        continue
    if e == "Aizen":
        print("Aizen found — stop mission!")
        break
    print(f"Engaging {e}")
# continue skips remaining body and moves to next; break exits loop

print("\n=== 7) for-else (search with else when not found) ===")
target = "Aizen"
for s in shinigami:
    if target in s:
        print(f"Found target among shinigami: {s}")
        break
else:
    # executed only if loop completes without break
    print(f"{target} not found among shinigami")

print("\n=== 8) nested loops (team matchups) ===")
print("All possible matchups between first 2 Shinigami and first 2 Arrancar:")
for s in shinigami[:2]:
    for a in arrancar[:2]:
        print(f"{s} vs {a}")
# nested loops enumerate Cartesian product

print("\n=== 9) list comprehension (compact mapping/filtering) ===")
bankai_users = [name for name in shinigami if "Byakuya" in name or "Ichigo" in name]
print("Bankai-capable (example):", bankai_users)

# more interesting: create tuple pairs with a condition
matchups = [(s.split()[0], a) for s in shinigami for a in arrancar if s != "Rukia Kuchiki"]
print("Generated matchups (first-name, arrancar):", matchups[:5])  # print first 5

print("\n=== 10) iter() and next() manual iteration ===")
it = iter(arrancar)
try:
    while True:
        enemy = next(it)
        print("Scanned arrancar:", enemy)
except StopIteration:
    print("All arrancar scanned.")

print("\n=== 11) reversed() and range iteration ===")
print("Shinigami in reverse order:")
for name in reversed(shinigami):
    print(name)

print("\n=== 12) looping over characters in a string ===")
name = "Ichigo"
letters = [ch for ch in name]
print("Letters in 'Ichigo':", letters)

print("\n=== 13) generator-style loop (simulate streaming encounters) ===")
def encounter_stream():
    for e in ("Hollow", "Menos", "Arrancar", "Espada"):
        yield e

for encounter in encounter_stream():
    print("Encountered:", encounter)
    if encounter == "Arrancar":
        print("-- prepare reiatsu!")

print("\n=== 14) small practical example: simulate a 'duel' with loops ===")
# Simple duel: Ichigo vs first Arrancar, turn-based until one HP <= 0
ichigo_hp, arrancar_hp = 120, 90
turn = 0
while ichigo_hp > 0 and arrancar_hp > 0:
    turn += 1
    # Ichigo attacks on odd turns, arrancar on even
    if turn % 2 == 1:
        arrancar_hp -= 30
        print(f"Turn {turn}: Ichigo hits! Arrancar HP = {max(0, arrancar_hp)}")
        if arrancar_hp <= 0:
            print("Arrancar defeated! Ichigo wins.")
            break
    else:
        ichigo_hp -= 20
        print(f"Turn {turn}: Arrancar hits! Ichigo HP = {max(0, ichigo_hp)}")
        if ichigo_hp <= 0:
            print("Ichigo falls...")

print("\n=== Demo complete ===")
