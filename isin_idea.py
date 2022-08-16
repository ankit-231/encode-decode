while True:
    ask = input("Encode or Decode? ")

    if ask.replace(' ', '').lower() == 'encode' or ask == '1':
        dictionary = {'1': 'h', '2': 'he', '3': 'li', '4': 'be', '5': 'b', '6': 'c', '7': 'n', '8': 'o', '9': 'f',
                      '10': 'ne',
                      '11': 'na', '12': 'mg', '13': 'al', '14': 'si', '15': 'p', '16': 's', '17': 'cl', '18': 'ar',
                      '19': 'k',
                      '20': 'ca', '21': 'sc', '22': 'ti', '23': 'v', '24': 'cr', '25': 'mn', '26': 'fe', '27': 'co',
                      '28': 'ni',
                      '29': 'cu', '30': 'zn', '31': 'ga', '32': 'ge', '33': 'as', '34': 'se', '35': 'br', '36': 'kr',
                      '37': 'rb',
                      '38': 'sr', '39': 'y', '40': 'zr', '41': 'nb', '42': 'mo', '43': 'tc', '44': 'ru', '45': 'rh',
                      '46': 'pd',
                      '47': 'ag', '48': 'cd', '49': 'in', '50': 'sn', '51': 'sb', '52': 'te', '53': 'i', '54': 'xe',
                      '55': 'cs',
                      '56': 'ba', '57': 'la', '58': 'ce', '59': 'pr', '60': 'nd', '61': 'pm', '62': 'sm', '63': 'eu',
                      '64': 'gd',
                      '65': 'tb', '66': 'dy', '67': 'ho', '68': 'er', '69': 'tm', '70': 'yb', '71': 'lu', '72': 'hf',
                      '73': 'ta',
                      '74': 'w', '75': 're', '76': 'os', '77': 'ir', '78': 'pt', '79': 'au', '80': 'hg', '81': 'tl',
                      '82': 'pb',
                      '83': 'bi', '84': 'po', '85': 'at', '86': 'rn', '87': 'fr', '88': 'ra', '89': 'ac', '90': 'th',
                      '91': 'pa',
                      '92': 'u', '93': 'np', '94': 'pu', '95': 'am', '96': 'cm', '97': 'bk', '98': 'cf', '99': 'es',
                      '100': 'fm',
                      '101': 'md', '102': 'no', '103': 'lr', '104': 'rf', '105': 'db', '106': 'sg', '107': 'bh',
                      '108': 'hs',
                      '109': 'mt', '110': 'ds', '111': 'rg', '112': 'cn', '113': 'nh', '114': 'fl', '115': 'mc',
                      '116': 'lv',
                      '117': 'ts', '118': 'og'}

        #
        a = ''
        word = input("Enter your word: ").lower()
        print('')
        print("How do you want to separate your final result?")
        print("Hint: hit ENTER for default separation")
        while True:
            separator = input()
            if separator == '`':
                print("Sorry, you can't use (`) as a separator")
                print('Try using anything else:')
                continue
            else:
                break
        if separator == '':
            separator = ','


        def get_key(val):
            for key, value in dictionary.items():
                if val == value:
                    return key


        for key1, value1 in dictionary.items():
            if value1 in word:
                a = a + '`' + get_key(value1)
                

            # for x in word:
            #     if x.lower() in dictionary.values():
                    a = a + '`' + get_key(x.lower())
                else:
                    a = a + '`' + x
        a_stripped = a.strip('`').replace('`', separator)
        e_f = ''
        a_stripped_list = list(a_stripped.split(' '))
        for e in a_stripped_list:
            e_f = e_f + ' ' + e.strip(',')
        print(e_f.strip())
        again = input("Another round? ")
        print()
        again_list = ['', 'yes', 'yeah', 'yup', 'okay', 'sure', 'y', 'ya', 'ok', 'k']
        if again not in again_list:
            print('         Thank You')
            break

    elif ask.replace(' ', '').lower() == 'decode' or ask == '2':
        dictionary = {'1': 'h', '2': 'he', '3': 'li', '4': 'be', '5': 'b', '6': 'c', '7': 'n', '8': 'o', '9': 'f',
                      '10': 'ne', '11': 'na', '12': 'mg', '13': 'al', '14': 'si', '15': 'p', '16': 's', '17': 'cl',
                      '18': 'ar', '19': 'k', '20': 'ca', '21': 'sc', '22': 'ti', '23': 'v', '24': 'cr', '25': 'mn',
                      '26': 'fe', '27': 'co', '28': 'ni', '29': 'cu', '30': 'zn', '31': 'ga', '32': 'ge', '33': 'as',
                      '34': 'se', '35': 'br', '36': 'kr', '37': 'rb', '38': 'sr', '39': 'y', '40': 'zr', '41': 'nb',
                      '42': 'mo', '43': 'tc', '44': 'ru', '45': 'rh', '46': 'pd', '47': 'ag', '48': 'cd', '49': 'in',
                      '50': 'sn', '51': 'sb', '52': 'te', '53': 'i', '54': 'xe', '55': 'cs', '56': 'ba', '57': 'la',
                      '58': 'ce', '59': 'pr', '60': 'nd', '61': 'pm', '62': 'sm', '63': 'eu', '64': 'gd', '65': 'tb',
                      '66': 'dy', '67': 'ho', '68': 'er', '69': 'tm', '70': 'yb', '71': 'lu', '72': 'hf', '73': 'ta',
                      '74': 'w', '75': 're', '76': 'os', '77': 'ir', '78': 'pt', '79': 'au', '80': 'hg', '81': 'tl',
                      '82': 'pb', '83': 'bi', '84': 'po', '85': 'at', '86': 'rn', '87': 'fr', '88': 'ra', '89': 'ac',
                      '90': 'th', '91': 'pa', '92': 'u', '93': 'np', '94': 'pu', '95': 'am', '96': 'cm', '97': 'bk',
                      '98': 'cf', '99': 'es', '100': 'fm', '101': 'md', '102': 'no', '103': 'lr', '104': 'rf',
                      '105': 'db', '106': 'sg', '107': 'bh', '108': 'hs', '109': 'mt', '110': 'ds', '111': 'rg',
                      '112': 'cn', '113': 'uut', '114': 'fl', '115': 'uup', '116': 'lv', '117': 'uus', '118': 'uuo'}
        final = ''
        not_final = ''
        print()
        separator = input("How is your code separated? ")
        print("First off, type your code in following format:")
        print("g,8,t 39,8,92")
        print()
        code = input("Enter your code:")

        li = list(code.split(separator))


        def get_key(val):
            for key, value in dictionary.items():
                if val == value:
                    return key


        for new in li:
            new_list = list(new.split(','))
            for ne in new_list:
                if ne in dictionary.keys():
                    not_final = not_final + dictionary[ne]
                else:
                    not_final = not_final + ne
            final = final + ' ' + not_final
            not_final = ''

        print(final.strip())
        again = input("Another round? ")
        print()
        again_list = ['', 'yes', 'yeah', 'yup', 'okay', 'sure', 'y', 'ya', 'ok', 'k']
        if again not in again_list:
            print('         Thank You')
            print('         5 39   a 7 19 53 t')
            break
    else:
        continue
