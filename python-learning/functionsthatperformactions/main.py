def textspacefunc(text):
    screen_width = 80
    if len(text)>screen_width-4:
        print("Text too long")
    elif text == "*":
        print(text*screen_width)
    else:
        output_string="**{0}**".format(text.center(screen_width-4))
        print(output_string)


textspacefunc("*")
textspacefunc("I live a happy life")
textspacefunc("I am happy")
textspacefunc("*")

