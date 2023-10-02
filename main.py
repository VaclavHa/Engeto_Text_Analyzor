"""
První projekt do Engeto Online Python Akademie

author: Václav Hanzl
email: hanzlvaclav00@gmail.com
discord: Wencour#6130 / Vašek H. (Engeto server)

"""
# import


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
splitter = "=" * 50

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


user_name = input("What is your username: ").lower()
password = input("What is your password: ")

print(splitter)


if users.get(user_name) == password:
    print(f"\nHi {user_name.title()}, welcome to text analyzator!\n")
    print(splitter)

else:
    print(
f"""Username: {user_name}
Password: {password}
Unregistered user!
Terminating the program..."""
)
    quit()

##################### Text split into articles and index  #####################

number_of_articles = len(TEXTS)

print(f"There are {number_of_articles} articles to choose from.\n")


for index, text in enumerate(TEXTS, start=1):
    print(f"Article number {index}:\n{text}\n")
print(splitter)


##################### User input choosing number of article  #####################


article_input = input("Choose the number of article you wanna analyze: ")
print(splitter)

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
    quit()

##################### Text split and strip  #####################

striped_analyzed_text = []

for words in chosen_article_number.split():
    clear_word = words.strip(".,:!?;/-")
    striped_analyzed_text.append(clear_word)

##################### Word counter  #####################
total_word_count = 0

single_word_counter = {}


for words in striped_analyzed_text:
    if words.isalpha():
        total_word_count += 1
        if words not in single_word_counter:
            single_word_counter[words] = 1
        else:
            single_word_counter[words] += 1

# print(f"Word counter: {single_word_counter}")
print(f"There are {total_word_count} words in the seleceted text.")
print(splitter)


##################### Words starting with only capital letter  #####################
capital_letter_count = 0
capital_letter_words = {}

for words in striped_analyzed_text:
    if words.istitle() and words.isalpha():
        capital_letter_count += 1
        if words not in capital_letter_words:
            capital_letter_words[words] = 1
        else:
            capital_letter_words[words] += 1

# print(f"Capital letter words: {capital_letter_words}")
print(f"There are {capital_letter_count} titlecase words.")
print(splitter)

##################### Uppercase words  #####################
uppercase_count = 0
uppercase_words = {}

for words in striped_analyzed_text:
    if words.isupper() and words.isalpha():
        uppercase_count += 1
        if words not in uppercase_words:
            uppercase_words[words] = 1
        else:
            uppercase_words[words] += 1

# print(f"Uppercase words: {uppercase_words}")
print(f"There are {uppercase_count} uppercase words.")
print(splitter)

##################### Lowercase words  #####################
lowercase_count = 0
lowercase_words = {}

for words in striped_analyzed_text:
    if words.islower() and words.isalpha():
        lowercase_count += 1
        if words not in lowercase_words:
            lowercase_words[words] = 1
        else:
            lowercase_words[words] += 1

# print(f"Lowercase words: {lowercase_words}")
print(f"There are {lowercase_count} lowercase words.")
print(splitter)
##################### Number count  #####################
numbers_count = 0
numbers_occurance = {}

for numbers in striped_analyzed_text:
    if numbers.isdigit():
        numbers_count += 1
        if numbers not in numbers_occurance:
            numbers_occurance[numbers] = 1
        else:
            numbers_occurance[numbers] += 1


# print(f"Numbers: {numbers_occurance}")
print(f"There are {numbers_count} numeric strings.")

print(splitter)

##################### Numbers sum  #####################

numbers_summary = 0

for number in numbers_occurance:
    numbers_summary += int(number)

print(f"The sum of all the numbers is: {numbers_summary}")

print(splitter)

##################### Graf  #####################

word_lenght_freqeunce = {}

for word in striped_analyzed_text:
    if word.isalpha():
        word_lenght = len(word)
        if word_lenght not in word_lenght_freqeunce:
            word_lenght_freqeunce[word_lenght] = 1
        else:
            word_lenght_freqeunce[word_lenght] += 1

max_length = max(word_lenght_freqeunce.keys())


print(splitter)
print(f"{'LEN':<5}|{'OCCURRENCES':^20}|{'NR.':>5}")
print(splitter)


for length in range(1, max_length + 1):
    freq = word_lenght_freqeunce.get(length, 0)
    bar = '*' * freq
    print(f"{length:<5}|{bar:^20}|{freq:>5}")

print(splitter)
