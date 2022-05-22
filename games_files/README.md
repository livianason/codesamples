# codesamples/games_files

`codesamples/games_files/` contains a collection of Python mini games you can download and play and make your own. The games are constantly being added and updated so please look out for the next updates. 

### Current list of games
- Wordle
- Hangman
- Mancala

Please leave a comment below with some ideas for mini games I can write in Python!

### How to play
1. Clone/download a copy of the repository
2. Open the terminal, and choose a game
3. Navigate to `$ cd codesamples/games_files/wordle/` or any game folder
4. Run `$ python3 wordle.py`

#### Wordle
1. A 5 letter word is selected at random
2. You must guess the word within 6 tries
3. After each guess, you are told how close your word is
    - O : a correct letter is in the correct position
    - X : a correct letter is in the wrong position
    - _ : the letter is not in the final word
4. Use the results to decide what the next word guess should be

#### Hangman
1. Run the game and choose a category
2. A word is randomly selected from that category
3. You must guess the word one letter guess at a time
4. You have 10 wrong guesses before the man is hung
5. You may guess the whole word, but you'll lose 2 tries if it is wrong

#### Mancala
1. Run the game and select the number of players
   - 1 Player : you play against the computer
   - 2 Players : you play against a friend
2. The game board is shown. Select a cup.
3. One point from the cup is placed into each following cup, counter-clockwise
4. If the last point in the cup falls on the score, you may go again
5. If the last point in the cup falls on an empty space on your side of the board, you may steal the points opposite.
6. Play until one side of the board is empty
7. Add all points left over on the board to that player's score. Highest score wins!
