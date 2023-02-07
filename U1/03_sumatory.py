tickets=0
addition=int(input("How many money do you have?\n"))
while addition>tickets:
    tickets += 1
    addition -= tickets
print("Enough for you ",tickets," tickets")