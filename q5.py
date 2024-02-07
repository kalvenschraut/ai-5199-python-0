# this generates a new list instead of appending and changing original
def add_attraction(attractions=[], attraction=''):
    if len(attraction) == 0:
        attraction = 'State fair'
    return attractions + [attraction]
originalAttractions=['Attraction A', 'Attraction B', 'Attraction C']
newAttraction = 'Some Attraction'
newAttractions = add_attraction(attraction=newAttraction, attractions=originalAttractions)
print(len(newAttractions), len(originalAttractions));
assert len(newAttractions) == (len(originalAttractions) + 1)
assert newAttractions[-1] == newAttraction
