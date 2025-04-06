def count_words(message):
    words = message.split()
    return len(words)

def count_characters(message):
    message.lower()
    characterCounts = {}
    for c in message:
        if c in characterCounts:
            characterCounts[c] += 1
        else: 
            characterCounts[c] = 1
    return characterCounts

def sort_on(dict):
    return dict["count"]

def sort_characters_dict(dict):
    listds = []
    for entry in dict:
        obj = {"character": entry, "count": dict[entry]}
        listds.append(obj)
    listds.sort(reverse=True, key=sort_on)
    return listds

