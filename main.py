"""
První projekt do Engeto Online Python Akademie

author: Václav Hanzl
email: hanzlvaclav00@gmail.com
discord: Wencour#6130 / Vašek H. (Engeto server)
"""
# import ...


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
         ]


##################### Users, input username and password, pass or quit #####################

# users = {
#     "bob": "123",
#     "ann": "pass123",
#     "mike": "password123",
#     "liz": "pass123"
# }


# user_name = input("What is your username: ").lower()
# password = input("What is your password: ")

# if users.get(user_name) == password:
#     print(f"\nHi {user_name.title()}, welcome to our text analyzator!\n")
# else:
#     print(f"username: {user_name}\npassword: {password}\nunregistered user, terminating the program...")
#     quit()

##################### Text split and index  #####################

number_of_articles = len(TEXTS)

print(f"There are {number_of_articles} articles to choose from.\n")


for index, text in enumerate(TEXTS, start=1):
    print(f"Article number {index}: \n{text}\n")

##################### User input choosing number of article  #####################


article_input = input("Choose the number of article you wanna check: ")

if article_input.isdigit():
    article_number = int(article_input)

    if 1 <= article_number <= len(TEXTS):
        chosen_article_number = TEXTS[article_number - 1]
    else:
        print(
            f"You have chosen number '{article_number}' which is not listed.\nPlease try again...")
        quit()
else:
    print(f"You have not entered a digit.\nPlease try again...")
