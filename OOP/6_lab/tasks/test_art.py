from art import text2art, tprint

print("--- Приклад 1: tprint ---")
tprint("OOP", font="block")

print("\n--- Приклад 2: text2art ---")
ascii_art = text2art("Python 3.14", font="small")
print(ascii_art)