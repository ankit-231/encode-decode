def encryptor(dictionary):
    while True:
        ask = input("Encode or Decode? ")

        if ask.replace(' ', '').lower() == 'encode':
            a = ''
            word = input("Enter your word: ").lower()
            print('')
            print("How do you want to separate your final result?")
            print("Hint: hit ENTER for default separation")
            separator = input()
            if separator == '':
                separator = ' '

            def get_key(val):
                for key, value in dictionary.items():
                    if val == value:
                        return key

            for x in word:
                if x.lower() in dictionary.values():
                    a = a + '`' + get_key(x.lower())
                else:
                    a = a + '`' + x
            print(a.strip('`').replace('`', separator))
            again = input("Another round?")
            print()
            again_list = ['', 'yes', 'yeah', 'yup', 'okay', 'sure', 'y', 'ya', 'ok', 'k']
            if again not in again_list:
                print('         Thank You')
                break

        elif ask.replace(' ', '').lower() == 'decode':
            final = ''
            print()
            print("First off, type your code in following format:")
            print("g,8,t, ,39,8,92")
            print()
            code = input("Enter your code:")

            li = list(code.split(','))


            def get_key(val):
                for key, value in dictionary.items():
                    if val == value:
                        return key


            for new in li:
                if new in dictionary.keys():
                    final = final + dictionary[new]
                else:
                    final = final + new

            print(final)
            again = input("Another round?")
            print()
            again_list = ['', 'yes', 'yeah', 'yup', 'okay', 'sure', 'y', 'ya', 'ok', 'k']
            if again not in again_list:
                print('         Thank You')
                break
        else:
            continue
