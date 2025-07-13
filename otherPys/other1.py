contents = ["It's raining cats and dogs!",
            "It's been raining for hours!",
            "Flash floods are coming!"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)