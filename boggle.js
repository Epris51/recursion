function find(board, word) {
  const numRows = board.length;
  const numCols = board[0].length;

  function dfs(row, col, index) {
    // Base case: if the entire word has been found, return true
    if (index === word.length) {
      return true;
    }

    // Check if the current cell is out of bounds or does not match the current letter
    if (
      row < 0 || row >= numRows ||
      col < 0 || col >= numCols ||
      board[row][col] !== word[index]
    ) {
      return false;
    }

    // Temporarily mark the current cell as visited
    const originalLetter = board[row][col];
    board[row][col] = '*';

    // Explore all valid neighboring cells
    const neighbors = [
      [-1, 0], [1, 0], [0, -1], [0, 1] // Up, Down, Left, Right
    ];

    for (const [dr, dc] of neighbors) {
      if (dfs(row + dr, col + dc, index + 1)) {
        return true;
      }
    }

    // Restore the original letter and backtrack
    board[row][col] = originalLetter;

    return false;
  }

  // Iterate through each cell in the board and attempt to start the search from there
  for (let row = 0; row < numRows; row++) {
    for (let col = 0; col < numCols; col++) {
      if (dfs(row, col, 0)) {
        return true; // If the word is found starting from this cell, return true
      }
    }
  }

  return false; // Word not found in the entire board
}

// EXAMPLE TEST

const board = makeBoard(`N C A N E
                       O U I O P
                       Z Q Z O N
                       F A D P L
                       E D E A Z`);

console.log(find(board, "NOON")); // true
console.log(find(board, "NOPE")); // true
console.log(find(board, "CANON")); // false
console.log(find(board, "QUINE")); // false
console.log(find(board, "FADED")); // true

const board2 = makeBoard(`E D O S Z
                        N S O N R
                        O U O O P
                        Z Q Z O R
                        F A D P L`);

console.log(find(board2, "NOOOOS")); // true
