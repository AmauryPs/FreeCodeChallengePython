def get_words(paragraph):
    specchara = [",","!","."]
    paragraph = paragraph.lower()
    paragraph = paragraph.split(" ")
    print(paragraph)
    for char in specchara:
        if char in paragraph:
            print(char)
            paragraph.remove(char)
    for i in paragraph:
        paragraphd = dict((i, paragraph.count(i)))
    
    return print(paragraph)


get_words("Hello, je suis, amaury, le, le, le bg les pates de amaury !")