replay = 'Y'
while replay == 'Y':
    word = input("Enter a word:    ").lower()
    score = 0
    for letter in word:
        if letter in 'aeioulnstr':
            score += 1
        elif letter in 'dg':
            score += 2
        elif letter in 'bcmp':
            score += 3
        elif letter in 'fhvwy':
            score += 4
        elif letter == 'k':
            score += 5
        elif letter in 'jx':
            score += 8
        elif letter in 'qz':
            score += 10
    print(f"The score for this word is: {score}")
    replay = input("Play Again? (Y/N)     ").strip().upper()
