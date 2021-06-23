story1 = {
    "start":"The journey starts here...",
    "Middle":"A big battle occurs...",
    "End":"It was all a dream."
}

print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())

print(story1.get("Start"))
print(story1.get("Middle"))
print(story1.get("End"))

for i in story1.values():
    print(i)

story1.update({"Hero":"Steel man"})
print(story1)