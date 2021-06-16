stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,"Glasgow Queen")
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
# ans - insert number was 4 not 3 because Queen street had been added
stops.insert(3, "Polmont")
#4. Print out the index position of "Linlithgow"
# ans -
print(stops.index("Linlithgow"))
#5. Remove "Livingston" from the list using its name
# ans -
stops.remove("Livingston")
#6. Delete "Cumbernauld" from the list by index
# ans -
stops.pop(1)
#7. Print the number of stops there are in the list
# ans -
print(len(stops))
#8. Sort the list alphabetically
# ans -
stops.sort()
#9. Reverse the positions of the stops in the list
# ans -
stops.sort(reverse = True)
print(stops)
#10 Print out all the stops using a for loop
# ans -
for stop in stops:
    print(stop)
