import re

end_y = re.compile(r"y$")
end_other = re.compile(r"(o|(ch)|(sh)|x|s|z)$")

word = input()
# print(word, end_other.findall(word))
if end_y.findall(word):
    if word[-2] in ["a", "e", "i", "o", "u"]:
        word += "s"
    else:
        word = word[:-1] + "ies"
elif end_other.findall(word):
    word += "es"
else:
    word += "s"

print(word)
