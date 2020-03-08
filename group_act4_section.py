

def menu():
    print("[1] ADD")
    print("[2] Search")  # choices
    print("[0] Exit")

    choice = input("")  # user input
    if choice == "1":  # if user input is equal to  "1" go to add() function
        add()
    elif choice == "2":  # if user input is equal to  "2" go to search() function
        search()
    elif choice == "0":  # if user input is equal to  "0" return to terminate program
    else:
        menu()  # if user input non in the choices then the program will go back in menu() function


def add():  # add() function dito nag aadd ng content
    print("##### Contact Person #####")
    print("----- Add New Contact -----")

    # input ng contact name remember contact name is always index zero in our text file
    contact_person = input("Contact Name: ")
    contact = ""  # contact dito natin icoconcatinate yung mga labels and contacts

    while True:  # this is infinite loooooop...!!!!
        # contact_type input ng kung email ba yan or phone umber or kahit ano
        contact_type = input("Contact Type: ")
        if contact_type == "0":  # if contact_type is equal to zero meaning matatapos na yung loop at mahihinto na ang pag iinput ng mga label and contact
            break
        else:  # else meaning hindi zero ang tinype kaya makakapag input pa rin ng label and contact..!!!
            # input lang with printing lang yung contact_type eg: (Email: yourinputhere blahblah blah...)
            content = input("{}: ".format(contact_type))
            # pagkatapos mag input concatenate lang nyung contact_type which is our label and content which is our contact
            contact += "#"+contact_type+"^" + content  # dont forget the delimiter

    # whole details is equal to contact_person na contact name natin and contact whice is our label and contact
    whole_detail = contact_person + contact + "\n"

    file = open("group_data_section.txt", "a")  # open with pemission append
    # append lang remember pag appending nasa dulo lagi ang pointer or cursor so hindi maooverwrite madadagdaglang yung string ah
    file.write(whole_detail)
    file.close()
    menu()  # go back lang sa menu kasi yun ang rule


def search():  # search() function
    print("##### Contact Person #####")
    print("----- Search Contact -----")

    # get the user input eto yung sinesearch ni user it can be part lang nung string na hinahanap na title
    user_input = input("Contact Name:")

    file = open("group_data_section.txt", "r")  # open as reading
    # we have here a list na magiging storage natin sa lahat ng makikita na na nag cocontain ng user_input
    searched_items = []

    # getting the search
    # so here in loop basicaly pag nag cocontain si user_input ng kahit saang part ni contact_infos iaapend lang natin sa searched_items na list
    for contact_infos in file:
        # always remember na kinocompare natin sa index zero kasi sa title lang dapat icompare
        if user_input.lower() in contact_infos.split("#")[0].lower():
            # eto yung appending na sinasabi ko
            searched_items.append(contact_infos)

    file.close()

    # displaying search contact names
    if len(searched_items) == 0:  # if the lenght of the list searched_items is empty or zero meaning no record found sa sinesearch ni user
        print("No records.")
        menu()  # go back lang sa menu()
        return

    # dito na natin ililist down lahat titles na nakita sa search
    # enumerate remember alaways have 2 parameter the first one is the iterable value or variable and the second one is start which is the default value is zero
    for numbering, contact_name in enumerate(searched_items, start=1):
        # index zero kasi title lang dinidisplay natin
        print("[{}] {}".format(numbering, contact_name.split("#")[0]))

    print("[0] Main Menu")  # main menu option

    choice = input("")  # the choice
    # wag kakalimutan tong searched_picked variable na to gamit na gamit natin to sa updating and deleting functions...!!!
    # su searched_picked kasi ang maiistore sakanya is yung pinli ni user sa search..!!!
    searched_picked = ""

    if choice == "0":  # if user choice is equal to zero go back in menu() function and return
        menu()
        return
    else:
        # storing na kay searched_picked..!!!
        # we store kay searched_picked yung value ni searched_items with the index nung pinili or (choice) minus one because we are dealing with index and indexes always start with zero
        searched_picked = searched_items[int(choice)-1]
        # go to this function to this play the content of that
        displaySearchedPicked(searched_picked)


# dito sa function na ito nag didisplay ng ng buong title, label and content... and mga choices kung dedelete ba or upupdate or babalik blah blah blah....!!
# gamit na gamit si seached_picked ah wag kakalimutan kung sino siya
def displaySearchedPicked(searched_picked):

    print("##### Contacts #####")
    print("----- Contact Details -----")
    print("Contact Name => {}".format(
        searched_picked.split("#")[0]))  # display ng title or the contact name

    # displaying ng label and contents
    # kaya searched_picked.split("#")[1:] kasi ayaw natin mag start sa index zero kasi prinint na natin si title sa taas
    for search_infos in searched_picked.split("#")[1:]:

        # split lang sa delimetet "^" paramahati si label at contact
        label, contact = search_infos.split("^")
        print("{} => {}".format(label, contact))  # printing label and contact

    print("[1] Go back")  # printing options
    print("[2] Update Contacts")
    print("[3] Delete Contact")
    print("[0] Main Menu")

    choice = input("")  # dito iistore si kung anong process pinili ni user

    if choice == "1":  # if chooice equal to 1 then go back to seach() function
        search()
    # if choice equal to 2 then go to updateContact(searched_picked) function remember eto parin pinapasa natin value ah wag kakalimutan si variable na to
    elif choice == "2":
        updateContact(searched_picked)
    # if choice equal to 2 then go to deleteContact(searched_picked) function remember eto parin pinapasa natin value ah wag kakalimutan si variable na to
    elif choice == "3":
        deleteContact(searched_picked)
    elif choice == "0":  # go back lang sa menu if zero
        menu()


# dito na si update yun parin ang pinapasa na value or varibale
def updateContact(searched_picked):
    print("##### Contacts #####")
    print("----- Update Contact Details -----")

    # print lang ng title parang umulit lang naman to iih
    print("Contact Name => {}".format(searched_picked.split("#")[0]))

    # ganun uli loop lang start uli sa [1:] or index 1 kasi di na natin need sali si title na print na bago pa to
    for search_infos in searched_picked.split("#")[1:]:

        # spluit lang uli sa delimete na "^" para mahati si label and contact
        label, contact = search_infos.split("^")
        # printing ng label and contact
        print("[{}] => {}".format(label, contact))

    # choice kung anong label ang babaguhin
    choice = input("Choice: ")
    # input ng bagong contact kay label na napili
    new_content = input("New {}: ".format(choice))

    # updataed value nilagay na natin yung title kasi hindi naman naiiba yun
    updated_value = searched_picked.split("#")[0]

    # loop uli ganun lang din
    for search_infos in searched_picked.split("#")[1:]:
        label, content = search_infos.split("^")

    # so pang yung choice ay equal na sa label meaning andun na tayo sa part na babaguhing content or contact so icoconcatenate natin yung bagong value
        if choice.lower() == label.lower():
            updated_value += "#"+label + "^" + new_content
        else:
            # pag hindi equal meaning icoconcatenate lang natin yung lumang value kasi hindi iyon yung hinahanap
            updated_value += "#"+label + "^" + content

    if "\n" not in updated_value: #pag wala pang "\n" sa dulo bali lalagyan pag meron na hindi na
        updated_value += "\n"  
    # print(updated_value)

    # updating text file

    file = open("group_data_section.txt", "r")  # open with reading permission
    updated_infos = ""

    # so dito buong file naman babaguhin natin ilalagay natin yung updated value at mawawala na yung dati
    for contact_infos in file:
        # if yung line na yun yung hinahanap ang icoconcatenate natin is yung bagong whole info na or yung updated_value
        # same logic lang din kanina
        if searched_picked in contact_infos:
            updated_infos += updated_value
        else:
            # else yung lumang line parin coconcatenate natin
            updated_infos += contact_infos

    print("Update success...")
    file.close()
    # para maupdate at maoverwrite natin yung lumang text file is gagamit tayo ng "W" permission and yung updated_infos na yung bagong laman
    file = open("group_data_section.txt", "w")
    file.write(updated_infos)
    file.close()
    # display lang yung bagong laman kaay bumalik tayo sa function na to
    displaySearchedPicked(updated_value)


# almost the same lang naman din si delete ni update
# yunn parin syempre ipinapasa nating parameter
def deleteContact(searched_picked):
    print("##### Contacts #####")
    print("----- Update Contact Details -----")

    file = open("group_data_section.txt", "r")  # opend reading

    updated_value = ""  # dito natin muna iistore sa string na to

    for search_infos in file:
        # so habang hindi yung line na hinahanap  natin ang lumalabas coconcatenate lang natin lagi
        # so pag asa line na tayo nung hinahanap bali lalagpasan lang natin para hindi na masama sa text file
        if searched_picked != search_infos:
            updated_value += search_infos
    file.close()

    # asking lang ng confirmation
    if input("Are you sure you want to proceed? [y/s]: ").lower() == "y":
        file = open("group_data_section.txt", "w")
        file.write(updated_value)  # overwite natin ng updated_value
        file.close()
        menu()  # balik sa menu()
    else:
        # pag nag no balik sa display ng sinearch
        displaySearchedPicked(searched_picked)


menu()


# note mas okay kung itatry nyo gawin sa bahay kahit di same logic para masanay din kayo at syempre pag nagawa nyo kaya nyo na tong iexplain
# goodluck wag masyadong ipressure pero mag kabisa hehe
