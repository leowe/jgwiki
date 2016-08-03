import re
from collections import Counter

stoppwoerter = ["der", "die", "das", "den", "und", "in", "to", "bei", "um", "zu", "aus", "/*", "*/", "wir"]


def parse_site(filename):
    with open(filename) as file:
        text = file.read()
    tmp = re.sub("<[^<]+>", '', text).split()
    return tmp


def is_not_stoppwort(string):
    if string not in stoppwoerter:
        return string


def occurrences(text_list, top=100):
    c = Counter()
    for word in text_list:
        c.update(word.split())
    return c.most_common(top)

#result = [item for item in parse_site("jgw.txt") if is_not_stoppwort(item.lower())]


#print(occurrences([item for item in parse_site("jgw.txt")]))
#print(result)
