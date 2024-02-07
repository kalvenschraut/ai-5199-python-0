import re

def create_acronym(name):
    txt = ''
    for str in name.split(' '):
        if re.match(r'^[A-Z]', str):
            txt += str[0]
    return txt
assert create_acronym('Master of Science in Software Engineering') == 'MSSE'
assert create_acronym('As Soon As Possible') == 'ASAP'
assert create_acronym('American Association for Active Lifestyles and Fitness') == 'AAALF'
print('All tests passed');
