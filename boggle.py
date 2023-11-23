def make_board(board_string):
    """Make a board from a string.

    For example::

        >>> board = make_board('''
        ... N C A N E
        ... O U I O P
        ... Z Q Z O N
        ... F A D P L
        ... E D E A Z
        ... ''')

        >>> len(board)
        5

        >>> board[0]
        ['N', 'C', 'A', 'N', 'E']
    """

    letters = board_string.split()

    board = [
        letters[0:5],
        letters[5:10],
        letters[10:15],
        letters[15:20],
        letters[20:25],
    ]

    return board

def find(board, word):
    def dfs(row, col, index):
        # Base case: if the entire word has been found, return True
        if index == len(word):
            return True

        # Check if the current cell is out of bounds or does not match the current letter
        if (row < 0 or row >= len(board) or
            col < 0 or col >= len(board[0]) or
            board[row][col] != word[index]):
            return False

        # Temporarily mark the current cell as visited
        original_letter = board[row][col]
        board[row][col] = '*'

        # Explore all valid neighboring cells
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in neighbors:
            if dfs(row + dr, col + dc, index + 1):
                return True

        # Restore the original letter and backtrack
        board[row][col] = original_letter

        return False

    # Iterate through each cell in the board and attempt to start the search from there
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                return True  # If the word is found starting from this cell, return True

    return False  # Word not found in the entire board


# EXAMPLE TEST

board = make_board('''
N C A N E
O U I O P
Z Q Z O N
F A D P L
E D E A Z
''')

print(find(board, "NOON"))  # True
print(find(board, "NOPE"))  # True
print(find(board, "CANON"))  # False
print(find(board, "QUINE"))  # False
print(find(board, "FADED"))  # True

board2 = make_board('''
E D O S Z
N S O N R
O U O O P
Z Q Z O R
F A D P L
''')

print(find(board2, "NOOOOS"))  # True

