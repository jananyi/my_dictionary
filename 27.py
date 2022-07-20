import pickle

"""
     --- controller code ---
"""


def handle_add():
    add = process_choice(chr, menu)
    add = input("enter a word to add:")
    add = sanitize_input(add)
    add_meaning = input("enter the meaning:")
    add1 = add_entry(add, add_meaning)


def handle_look_up():
    print("you choose to look_up")
    look_up = input("enter a word to look_up:")
    look_up = sanitize_input(look_up)
    look_up_value = look_up_entry(look_up)
    if (look_up_value is not None):
        print("the word is found")
        display_entry(look_up, look_up_value)
    else:
        print("the word is not found")


def handle_remove():
    print("you choose to delete")
    delete = input("enter a word to delete:")
    delete = sanitize_input(delete)
    delete = remove_entry(delete)
    if delete is None:
        print("word is deleted")
    else:
        print("word is not found")


def handle_edit():
    print("you choose to edit")
    word_meaning_change = input("enter the word whose meaning is to be changed:")
    new_meaning = input("enter correct meaning:")
    word_meaning_change = sanitize_input(word_meaning_change)
    add_entry(word_meaning_change, new_meaning)


def handle_rename():
    old_word = input("enter the old name:")
    if look_up_entry(old_word) is not None:
        new_word = input("enter correct name:")
        new_word = sanitize_input(new_word)
        rename_entry(old_word, new_word)
    else:
        print("word not found")


def handle_print():
    print("you choose to print")
    print_dictionary()


def handle_save():
    print("saving....")
    save_dictionary()
    print("saved")


def handle_exit():
    print("you choose to exit")
    exit()


def display_menu(disp_menu):
    menu_index = 1
    print("\n ***MENU*** \n")
    for item in disp_menu:
        display_text = "%d. %s (%c)" % (menu_index, item[0], item[1])
        print(display_text)
        menu_index += 1


def process_choice(item, disp_menu):
    for menu_item in disp_menu:
        if item == menu_item[1]:
            print("you chose ", menu_item[0])
            menu_item[2]()


def sanitize_input(m):
    menu_out = m.lower().strip()
    return menu_out


def menu_loop():
    while True:
        display_menu(menu)
        menu_inp = input("enter your choice:")
        menu_inp = sanitize_input(menu_inp)
        process_handle(menu_inp, menu)


def process_handle(choice, disp_menu):
    called = False
    index = 1
    if choice.isdigit():
        int_choice = int(choice)
    else:
        int_choice = -1
    for menu_item in disp_menu:
        if choice == menu_item[1] or int_choice == index:
            print("you chose to", menu_item[0])
            menu_item[2]()
            called = True
        index += 1
    if not called:
        print("invalid choice")


"""
     --- model code ---
"""


def add_entry(s, m):
    D[s] = m
    return


def look_up_entry(key):
    if key in D:
        return (D[key])
    else:
        return None


def remove_entry(k):
    if k in D:
        del ([D[k]])
    else:
        return None


def rename_entry(old_word, new_word):
    meaning = look_up_entry(old_word)
    remove_entry(old_word)
    add_entry(new_word, meaning)


def load_dictionary():
    global D, load_from_file
    if not load_from_file:
        add_entry("cake", "an edible sweet bread")
        add_entry("brother", "an annoying person")
        add_entry("chicken", "an edible bird")
        add_entry("mom", "bad chef")
    else:
        my_file = open("janany.dict", "rb")
        D = pickle.load(my_file)
        print(D)


def save_dictionary():
    my_file = open("janany.dict", "wb")
    pickle.dump(D, my_file)


"""
     --- view code ---
"""


def print_dictionary():
    print_index = 1

    print("\n***DICTIONARY*** \n")

    for word, meaning in D.items():
        display_entry(print_index, word, meaning)
        print_index += 1
    print("\n")
    print("total number of entries:", print_index - 1)
    print("\n")


def display_entry(index, key, value):
    output = "%d . %s: %s" % (index, key, value)
    print(output)


menu = [
    ["add", "a", handle_add],
    ["look_up", "l", handle_look_up],
    ["delete", "d", handle_remove],
    ["edit", "e", handle_edit],
    ["rename", "r", handle_rename],
    ["print", "p", handle_print],
    ["save", "s", handle_save],
    ["exit", "x", handle_exit]
]

load_from_file = True
D = {}
load_dictionary()
menu_loop()
