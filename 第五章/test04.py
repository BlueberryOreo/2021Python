character = input()

if character.isupper() and not len(character) - 1:
    out = character.lower()
elif character.islower() and not len(character) - 1:
    out = character.upper()
else:
    out = character
print(out)
