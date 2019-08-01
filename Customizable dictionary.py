import json
from difflib import  get_close_matches

print('THIS IS A CUSTOMISABLE DICTIONARY, PLEASE FOLLOW ALL INSTRUCTIONS FOR ACCURATE RESULTS')
dico = json.load(open("data.json",'w+'))
add_word = None
rerun_prompt = None
print("What would you like to do with the dictionary today? \nEnter 'add words' to add words \nEnter 'check word definition' to check word definition" )
run_prompt = input()
run_prompt.lower()

if run_prompt == 'add words':

    print('What word do you want to add?')
    word_prompt = input()
    word_prompt.lower()
    print('What is the definition of the word? ')
    definition_prompt = input()
    dico[word_prompt]=[definition_prompt]
    print('Word added! Do you want to add another word? Enter yes or no: ')
    add_word = input()
    add_word.lower()

    while add_word != 'no':
        if add_word == 'yes':
            print('What word do you want to add?')
            word_prompt = input()
            word_prompt.lower()
            print('What is the definition of the word? ')
            definition_prompt = input()
            dico[word_prompt] = [definition_prompt]
        else:
            print('wrong entry, please enter yes or no: ')
            add_word = input()
            add_word.lower
        print('Word added! Do you want to add another word? Enter yes or no: ')
        add_word = input()
        add_word.lower()
    print ('Do you want to check word definitions? Enter yes or no')
    extra_prompt = input()
    if extra_prompt == 'yes':
        word = input("Enter word to get its definition(s): ")


        def definition(word):
            word = word.lower()

            if word in dico:

                X = (dico.get(word))
                for i, value in enumerate(X):
                    print(value)
            if word.upper() in dico:
                print(dico.get(word.upper()))
            elif word.title() in dico:
                Y = dico.get(word.title())
                for i, value in enumerate(Y):
                    print(value)
            elif word not in dico:
                word.lower()
                get_close_matches(word, dico.keys(), cutoff=0.8)
                if len(get_close_matches(word, dico.keys())) > 0:
                    print("did you mean", ':', get_close_matches(word, dico.keys())[0])
                    ask = input("enter Y for yes and N for no ")
                    if ask == 'Y':
                        R = (dico.get(get_close_matches(word, dico.keys())[0]))
                        for i, value in enumerate(R):
                            print(value)
                    elif ask == 'N':
                        print(
                            'Please double-check your entry, it is possible the definition is not included in this dictionary or word does not exist')
                    else:
                        print('I did not understand your entry')
                elif len(get_close_matches(word, dico.keys())) == 0:
                    print("Word does not exist")


        definition(word)
        rerun_prompt = input('Would you like to check for another word? Enter yes or no: ')
        rerun_prompt.lower

        while rerun_prompt != 'no':
            if rerun_prompt == 'yes':
                word = input("Enter word to get its definition(s): ")


                def definition(word):
                    word = word.lower()

                    if word in dico:

                        X = (dico.get(word))
                        for i, value in enumerate(X):
                            print(value)
                    if word.upper() in dico:
                        print(dico.get(word.upper()))
                    elif word.title() in dico:
                        Y = dico.get(word.title())
                        for i, value in enumerate(Y):
                            print(value)
                    elif word not in dico:
                        word.lower()
                        get_close_matches(word, dico.keys(), cutoff=0.8)
                        if len(get_close_matches(word, dico.keys())) > 0:
                            print("did you mean", ':', get_close_matches(word, dico.keys())[0])
                            ask = input("enter Y for yes and N for no ")
                            if ask == 'Y':
                                R = (dico.get(get_close_matches(word, dico.keys())[0]))
                                for i, value in enumerate(R):
                                    print(value)
                            elif ask == 'N':
                                print(
                                    'Please double-check your entry, it is possible the definition is not included in this dictionary or word does not exist')
                            else:
                                print('I did not understand your entry')
                        elif len(get_close_matches(word, dico.keys())) == 0:
                            print("Word does not exist")


                definition(word)
                rerun_prompt = input('Would you like to check for another word? Enter yes or no: ')
                rerun_prompt.lower

            else:
                print('Please enter yes or no')
                rerun_prompt = input()
                rerun_prompt.lower()



elif run_prompt == 'check word definition':



    word = input("Enter word to get its definition(s): ")

    def definition(word):
        word = word.lower()


        if word in dico:

            X = (dico.get(word))
            for i,value in enumerate(X):
                print(value)
        if word.upper() in dico:
            print(dico.get(word.upper()))
        elif word.title() in dico:
            Y = dico.get(word.title())
            for i, value in enumerate(Y):
                print(value)
        elif word not in dico:
            word.lower()
            get_close_matches(word, dico.keys(), cutoff=0.8)
            if len(get_close_matches(word, dico.keys()))>0:
                print("did you mean", ':', get_close_matches(word, dico.keys())[0])
                ask = input("enter Y for yes and N for no ")
                if ask == 'Y':
                    R =  (dico.get(get_close_matches(word, dico.keys())[0]))
                    for i, value in enumerate(R):
                        print(value)
                elif ask == 'N':
                    print('Please double-check your entry, it is possible the definition is not included in this dictionary or word does not exist')
                else:
                    print('I did not understand your entry')
            elif len(get_close_matches(word, dico.keys())) == 0:
                print("Word does not exist")

    definition(word)
    rerun_prompt = input('Would you like to check for another word? Enter yes or no: ')
    rerun_prompt.lower

    while rerun_prompt != 'no':
        if rerun_prompt == 'yes':
            word = input("Enter word to get its definition(s): ")


            def definition(word):
                word = word.lower()

                if word in dico:

                    X = (dico.get(word))
                    for i, value in enumerate(X):
                        print(value)
                if word.upper() in dico:
                    print(dico.get(word.upper()))
                elif word.title() in dico:
                    Y = dico.get(word.title())
                    for i, value in enumerate(Y):
                        print(value)
                elif word not in dico:
                    word.lower()
                    get_close_matches(word, dico.keys(), cutoff=0.8)
                    if len(get_close_matches(word, dico.keys())) > 0:
                        print("did you mean", ':', get_close_matches(word, dico.keys())[0])
                        ask = input("enter Y for yes and N for no ")
                        if ask == 'Y':
                            R = (dico.get(get_close_matches(word, dico.keys())[0]))
                            for i, value in enumerate(R):
                                print(value)
                        elif ask == 'N':
                            print(
                                'Please double-check your entry, it is possible the definition is not included in this dictionary or word does not exist')
                        else:
                            print('I did not understand your entry')
                    elif len(get_close_matches(word, dico.keys())) == 0:
                        print("Word does not exist")


            definition(word)
            rerun_prompt = input('Would you like to check for another word? Enter yes or no: ')
            rerun_prompt.lower

        else:
            print('Please enter yes or no')
            rerun_prompt =  input()
            rerun_prompt.lower()


    if rerun_prompt == 'no':
        print('Would you like to add words? Enter yes or no: ')
        extra1_prompt = input()
        if extra1_prompt == 'yes':
            print('What word do you want to add?')
            word_prompt = input()
            word_prompt.lower()
            print('What is the definition of the word? ')
            definition_prompt = input()
            dico[word_prompt] = [definition_prompt]
            print('Word added! Do you want to add another word? Enter yes or no: ')
            add_word = input()
            add_word.lower()

            while add_word != 'no':
                if add_word == 'yes':
                    print('What word do you want to add?')
                    word_prompt = input()
                    word_prompt.lower()
                    print('What is the definiton of the word? ')
                    definition_prompt = input()
                    dico[word_prompt] = [definition_prompt]
                else:
                    print('wrong entry, please enter yes or no: ')
                    add_word = input()
                    add_word.lower
                print('Word added! Do you want to add another word? Enter yes or no: ')
                add_word = input()
                add_word.lower()
        if extra1_prompt == 'no':
            print('Thank you for using this program! Do come again.')
dico.close()

