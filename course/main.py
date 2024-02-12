oceans = [
    "Southern",
    "Arctic"
]

with open("./data/oceans.txt", "a") as f:
    for ocean in oceans:
        f.write("\n")
        f.write(ocean)

        # Autre possibilité
        # print(ocean, file=f)

