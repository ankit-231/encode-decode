# ask.replace(' ', '').lower() == 'decode':
dictionary = {'1': 'h', '2': 'he', '3': 'li', '4': 'be', '5': 'b', '6': 'c', '7': 'n', '8': 'o', '9': 'f', '10': 'ne', '11': 'na', '12': 'mg', '13': 'al', '14': 'si', '15': 'p', '16': 's', '17': 'cl', '18': 'ar', '19': 'k', '20': 'ca', '21': 'sc', '22': 'ti', '23': 'v', '24': 'cr', '25': 'mn', '26': 'fe', '27': 'co', '28': 'ni', '29': 'cu', '30': 'zn', '31': 'ga', '32': 'ge', '33': 'as', '34': 'se', '35': 'br', '36': 'kr', '37': 'rb', '38': 'sr', '39': 'y', '40': 'zr', '41': 'nb', '42': 'mo', '43': 'tc', '44': 'ru', '45': 'rh', '46': 'pd', '47': 'ag', '48': 'cd', '49': 'in', '50': 'sn', '51': 'sb', '52': 'te', '53': 'i', '54': 'xe', '55': 'cs', '56': 'ba', '57': 'la', '58': 'ce', '59': 'pr', '60': 'nd', '61': 'pm', '62': 'sm', '63': 'eu', '64': 'gd', '65': 'tb', '66': 'dy', '67': 'ho', '68': 'er', '69': 'tm', '70': 'yb', '71': 'lu', '72': 'hf', '73': 'ta', '74': 'w', '75': 're', '76': 'os', '77': 'ir', '78': 'pt', '79': 'au', '80': 'hg', '81': 'tl', '82': 'pb', '83': 'bi', '84': 'po', '85': 'at', '86': 'rn', '87': 'fr', '88': 'ra', '89': 'ac', '90': 'th', '91': 'pa', '92': 'u', '93': 'np', '94': 'pu', '95': 'am', '96': 'cm', '97': 'bk', '98': 'cf', '99': 'es', '100': 'fm', '101': 'md', '102': 'no', '103': 'lr', '104': 'rf', '105': 'db', '106': 'sg', '107': 'bh', '108': 'hs', '109': 'mt', '110': 'ds', '111': 'rg', '112': 'cn', '113': 'uut', '114': 'fl', '115': 'uup', '116': 'lv', '117': 'uus', '118': 'uuo'}
final = ''
not_final = ''
print()
print("First off, type your code in following format:")
print("g,8,t 39,8,92")
print()
code = input("Enter your code:")

li = list(code.split(' '))


def get_key(val):
    for key, value in dictionary.items():
        if val == value:
            return key


for new in li:
    new_list = list(new.split(','))
    print(new_list)
    for ne in new_list:
        print(ne)
        if ne in dictionary.keys():
            not_final = not_final + dictionary[ne]
        else:
            not_final = not_final + ne
    final = final + ' ' + not_final
    not_final = ''

print(final.strip())

print()