#check if string start with a substring
text = "hello world"
print(text.startswith("hello")) #true
print(text.startswith("world")) #false

#check if string end with a substring
print(text.endswith("world")) #falstrue

#find the position of a substring
print(text.find("world"))

#count occurence of the substring
print(text.count("l"))

#check if all characters are alphaumaric
print(text.isalnum())

#check if all characters are alphanumeric
print(text.isalpha())

