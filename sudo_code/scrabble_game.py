# Set the replay value to Y automatically
replay = 'Y'
# While the replay value is Y, we should be prompted to input a word
while replay == 'Y':
    word = input("Enter a word:    ").lower()
    # Score starts at 0
    score = 0
    # For each letter in the word it adds the points to score according to the scrabble score incrementors
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
    # Prints the score for the word
    print(f"The score for this word is: {score}")
    # Prompts the user if they want to replay. Take options Y or N
    replay = input("Play Again? (Y/N)  ").strip().upper()
