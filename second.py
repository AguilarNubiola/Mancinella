grouped_comics = [
    ["Ultimates", [1]],
    ["Ultimate Black Panther", [4]],
    ["Ultimate Wolverine", [5]],
    ["Ultimate X-Men", [2]],
    ["Ultimate Spider-Man", [3]],
]

sorted_comics = sorted(grouped_comics, key=lambda x: x[1])
print(sorted_comics)

grouped_comics_dict = {
    "Ultimate Spider-Man": 3,
    "Ultimate Black Panther": 4,
    "Ultimates": 1,
    "Ultimates X-Men": 2,
    "Ultimate Wolverine": 5,
}


current_comics = {
    "Ultimates": {
        "writer": "Deniz Camp",
        "release_year": 2024,
        "company": "Marvel",
        "description": "An alternative universe version of the Avengers fix societal issues and injustices (on a micro and macro level) while tearing down the Maker's council"
    },
    "Ultimate X-Men": {
        "writer": "Peach Momoko",
        "release year": 2024,
        "company": "Marvel",
        "description": "A group of Japanese teenagers deal with amongst others, a cult, a xenophobic society, parental abuse, depression and a crazed geneticis"
    },
    "Ultimate Spider-Man": {
        "writer": "Jonathan Hickman",
        "release year": 2024,
        "company": "Marvel",
        "description": "Spider-Man takes on Wilson Fisk and his Sinister Six, while raising his two children alongside his wife Mary Jane"
    },
    "Ultimate Wolverine": {
        "writer": "Chris Condon",
        "release year": 2025,
        "company": "Marvel",
        "description": "A brainwashed Logan is used as a weapon by the Eurasian government, is debrainwashed and turns against the government",
    }
}