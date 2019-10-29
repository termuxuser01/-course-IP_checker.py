def center(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)
 
 
# call the function
center("spam and eggs")
center("spam, spam and eggs")
center(12)
center("spam, spam, spam and spam")
 
center("first", "second", 3, 4, "spam")
