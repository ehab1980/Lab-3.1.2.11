
wordWithoutVovels = ""

# Prompt the user to enter a word
# and assign it to the userWord variable
userWord = input('Please Enter The word: ')
print(userWord)
userWord = userWord.upper()
print(userWord)

for letter in userWord:
    # Complete the body of the loop.
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter,end='')

    
