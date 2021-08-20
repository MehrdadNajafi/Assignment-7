import sys
import colorama
from pyfiglet import Figlet
from colorama import Fore
colorama.init(autoreset=True)

translate_list = []

def load():
    try:
        print('Loading...')

        f = open('translate.txt','r')
        data = f.read()
        data_list = data.split('\n')
        
        for i in range(1,len(data_list),2):

            
            my_dict = { 'english' : data_list[i-1] ,
                        'persian' : data_list[i]   }
            
            translate_list.append(my_dict)
    
        print('Welcome')
    except:
        print(Fore.RED + 'Something went wrong. Can\'t load the file !!!')
        sys.exit()

def show_menu():
    print(Fore.BLUE + "<'''Menu'''>")
    print('1- Add new word')
    print('2- Translation english to persian')
    print('3- Translation persian to english')
    print('4- Save and Exit')

def add_word():
    print('1- Persian \n2- English ')
    user_choice = int(input())

    if user_choice == 1:
        new_persian_word = input('Please enter new world: ')
        
        c = 0
        for i in range(len(translate_list)):
            if new_persian_word.lower() == translate_list[i]['persian']:
                print('This word already added !!!')
                c += 1
                break
            
        if c == 0:
            new_english_word = input('Enter the English equivalent of the word: ')
            
            my_dict = { 'english' : new_english_word,
                        'persian' : new_persian_word}
            
            translate_list.append(my_dict)
            print('Word added !!!')
    
    elif user_choice == 2:
        new_english_word = input('Please enter new world: ')
        
        c = 0
        for i in range(len(translate_list)):
            if new_english_word.lower() == translate_list[i]['english']:
                print('This word already added !!!')
                c += 1
                break
            
        if c == 0:
            new_persian_word = input('Enter the Persian equivalent of the word: ')
            
            my_dict = { 'english' : new_english_word,
                        'persian' : new_persian_word}
            
            translate_list.append(my_dict)
            print('Word added !!!')

def english_to_persian():
    english_word = input('Please enter the text: ').lower()
    
    c = 0
    for i in english_word:
        if i != '.' :
            english_word_list = english_word.split(' ')
            c += 1
    
    if c == len(english_word):
        final_translate = ''
        for item in english_word_list:
            for i in range(len(translate_list)):
                if item == translate_list[i]['english']:
                    translate = translate_list[i]['persian'] + ' '
                    final_translate += translate
                    break
        print(final_translate)

    c_2 = 0
    for i in english_word:
        if i == '.':
            english_words_list = english_word.split('.')
            c_2 += 1
            break
    
    if c_2 == 1:
        
        final_en_list = []
        for i in range(len(english_words_list)):
            en_word_list = english_words_list[i].split(' ')
            final_en_list.append(en_word_list)
        
        final_translate = ''
        for i in range(len(final_en_list)):
            for j in range(len(final_en_list[i])):
                for k in range(len(translate_list)):
                    if final_en_list[i][j] == translate_list[k]['english']:
                        translate = translate_list[k]['persian'] + ' '
                        final_translate += translate
                        break
        
        print(final_translate)

def persian_to_english():
    persian_word = input('Please enter your text: ')

    c = 0
    for i in persian_word:
        if i != '.':
            c += 1
    
    if c == len(persian_word):
        persian_word_list = persian_word.split(' ')

        final_translate = ''
        for i in range(len(persian_word_list)):
            for j in range(len(translate_list)):
                if persian_word_list[i] == translate_list[j]['persian']:
                    translate = translate_list[j]['english'] + ' '
                    final_translate += translate
                    break
        print(final_translate)

    c_2 = 0
    for i in persian_word:
        if i == '.':
            c_2 += 1
            break
    
    if c_2 == 1 :
        persian_word_list = persian_word.split('.')
        
        final_persian_list = []
        for i in range(len(persian_word_list)):
            final_persian_list.append(persian_word_list[i].split(' '))
        
        final_translate = ''
        for i in range(len(final_persian_list)):
            for item in final_persian_list[i]:
                for j in range(len(translate_list)):
                    if item == translate_list[j]['persian']:
                        translate = translate_list[j]['english'] + ' '
                        final_translate += translate
                        break
        print(final_translate)

def exit_program():
    f = open('translate.txt', 'w')
    
    final_str = ''
    for i in range(len(translate_list)):
        if i == (len(translate_list)-1):
            str = translate_list[i]['english'] + '\n'
            final_str += str

            str = translate_list[i]['persian']
            final_str += str
        
        else:
            str = translate_list[i]['english'] + '\n'
            final_str += str

            str = translate_list[i]['persian'] + '\n'
            final_str += str
    
    f.write(final_str)
    f.close()
    exit()

load()

f = Figlet(font='standard')
print(f.renderText('Translator'))

while True:
    show_menu()

    user_choice = int(input('Please choose a option: '))

    if user_choice == 1:
        add_word()

    elif user_choice == 2:
        english_to_persian()

    elif user_choice == 3:
        persian_to_english()

    elif user_choice == 4:
        exit_program()