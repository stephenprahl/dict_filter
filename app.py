import re

with open("Chipewyan-Dictionary.txt", "r", encoding="utf-8") as f:
    for line in f:
        match = re.match(r"\s*(.*?)\s{2, }", line)
        if match:
            english = match.group(1).strip()
            phonetic = match.group(2).strip()

            print("English", english, " | Phonetic:", phonetic)
