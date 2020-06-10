# 2020-06-10
# Иерархическая структура данных


class Category:

    def __init__(self, title, subcats=[]):
        self.title = title
        self.subcats = subcats

    def print(self, level=0):
        print("   " * level, self.title)
        for subcat in self.subcats:
            subcat.print(level + 1)


root = Category("root", [
    Category("photo", [
        Category("travels"),
        Category("memes")
    ]),
    Category("audio", [
        Category("music", [
            Category("rock"),
            Category("popsa"),
            Category("classic")
        ]),
        Category("audiobooks", [
            Category("sci-fi"),
            Category("education")
        ])
    ]),
    Category("video", [
        Category("films", [
            Category("sci-fi"),
            Category("adventures"),
            Category("thriller")
        ]),
        Category("cartoons"),
        Category("education")
    ])
])

root.print()
