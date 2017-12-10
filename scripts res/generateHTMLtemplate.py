filename = "../website res/"+input("Name of file? \t")
template = open("template.html", "r")
f = open(filename, "w+")
f.write(template.read())
