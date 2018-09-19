def is_palindrome():
    user_word = input("Palindrome Checker: Enter a word here:  ")
    if user_word != user_word[::-1]:
        print("The word is NOT a Palindrome :(  ")
    else:
        print("The word IS a Palidrome! :)  ")
is_palindrome()
    

