import pytest

# Given functions to be tested
def initialize_board():
    """Creates a 3x3 Tic-Tac-Toe board initialized with empty spaces."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def make_move(board, row, col, player):
    """
    Places the player's symbol ('X' or 'O') on the board at the specified position.
    
    Args:
        board (list): The current game board.
        row (int): The row index (0-based).
        col (int): The column index (0-based).
        player (str): The player's symbol ('X' or 'O').

    Returns:
        bool: True if the move was successful, False otherwise.
    """
    # check if row and col are within the valid range (0 to 2)
    if row not in range(3) or col not in range(3):
        return False  # Invalid move: out of bounds

    # check if the cell is empty
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def check_winner(board):
    """
    Checks the current board for a winner.

    Args:
        board (list): The current game board.

    Returns:
        str: 'X' or 'O' if there is a winner, 'Draw' if it's a draw, or None if the game is ongoing.
    """
    # Check rows, columns, and diagonals
    lines = board + list(zip(*board))  # Rows and columns
    lines.append([board[i][i] for i in range(3)])  # Main diagonal
    lines.append([board[i][2-i] for i in range(3)])  # Anti-diagonal

    for line in lines:
        if all(cell == 'X' for cell in line):
            return 'X'
        if all(cell == 'O' for cell in line):
            return 'O'
    
    # Check for draw
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    
    return None

def reset_game():
    """Resets the game by reinitializing the board."""
    return initialize_board()


# Testing functions are below
def test_initialize_board():
    """Verify the `initialize_board` function creates an empty 3x3 board."""
    board = initialize_board()
    assert len(board) == 3  # Check if number of rows = 3
    assert all(len(row) == 3 for row in board)  # Check the number of columns in each row
    assert all(cell == ' ' for row in board for cell in row)  # Check if all cells are empty

def test_make_move_valid():
    """Check whether make_move successfully places a player’s symbol on an empty cell."""
    board = initialize_board()
    assert make_move(board, 0, 0, 'X')  # Make a valid move with X
    assert board[0][0] == 'X'  # Check that 'X' is placed correctly
    assert make_move(board, 1, 1, 'O')  # Make another valid move with O
    assert board[1][1] == 'O'  # Check that 'O' is placed correctly

def test_make_move_invalid():
    """Ensure `make_move` does not overwrite an occupied cell and returns `False` when attempting to do so."""
    board = initialize_board()
    make_move(board, 0, 0, 'X')  # Place 'X' in an empty cell
    result = make_move(board, 0, 0, 'O')  # Attempt to overwrite the occupied cell
    assert not result  # Ensure that the move was unsuccessful
    assert board[0][0] == 'X'  # Confirm that 'X' remains in that cell

def test_game_integration():
    """Perform a series of operations in the game."""
    board = initialize_board()  # Initialize the board
    # Making multiple moves
    assert make_move(board, 0, 0, 'X')
    assert make_move(board, 0, 1, 'O')
    assert make_move(board, 1, 1, 'X')
    assert make_move(board, 1, 0, 'O')
    assert make_move(board, 2, 2, 'X')  # X wins with this move

    assert check_winner(board) == 'X'  # Check if 'X' is the winner
    board = reset_game()  # Reset the game
    assert board == initialize_board()  # Verify that the board is reset


# For question 2 a and b
# Create the decorator
import pytest

@pytest.mark.parametrize("initial_board, row, col, player, expected_result, expected_board", [
    (initialize_board(), 
     0, 0, 'X', True, 
     [['X', ' ', ' '], 
      [' ', ' ', ' '], 
      [' ', ' ', ' ']]),  # Valid move
      
    ([['X', ' ', ' '], 
      [' ', ' ', ' '], 
      [' ', ' ', ' ']], 
      0, 0, 'O', False, 
      [['X', ' ', ' '], 
       [' ', ' ', ' '], 
       [' ', ' ', ' ']]),  # Overwrite occupied cell

    (initialize_board(), 3, 3, 'X', False, initialize_board()),  # Out-of-bounds move
    (initialize_board(), -1, 0, 'O', False, initialize_board()),  # Out-of-bounds move
])
def test_make_move(initial_board, row, col, player, expected_result, expected_board):
    """test function `test_make_move` that tests multiple scenarios of making moves, including edge cases such as invalid row or column indices, and placing a marker in an already occupied spot."""
    try:
        result = make_move(initial_board, row, col, player)
        assert result == expected_result, f"Should get {expected_result} and get {result}."
        assert initial_board == expected_board, f"Should get {expected_board} and get {initial_board}."
    except IndexError:
        assert expected_result == False, "Should raise IndexError."

@pytest.fixture
def fresh_board():
    """Fixture that resets the board for each test."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def test_initialize_board(fresh_board): # This time, we input the fresh board and test the function
    """Write a test function `test_initialize_board` that verifies the `initialize_board` function creates an empty 3x3 board."""
    board = fresh_board # Get the fresh board from the fixture
    assert len(board) == 3  # Check if number of rows = 3
    assert all(len(row) == 3 for row in board)  # Check the number of columns in each row
    assert all(cell == ' ' for row in board for cell in row)  # Check if all cells are empty

def test_make_move_valid(fresh_board):
    """Create a test function `test_make_move_valid` that checks whether make_move successfully places a player’s symbol on an empty cell."""
    board = fresh_board # Get the fresh board from the fixture
    assert make_move(board, 0, 0, 'X')  # Make a valid move with X
    assert board[0][0] == 'X'  # Check that 'X' is placed correctly
    assert make_move(board, 1, 1, 'O')  # Make another valid move with O
    assert board[1][1] == 'O'  # Check that 'O' is placed correctly

def test_make_move_invalid(fresh_board):
    """Create a test function `test_make_move_invalid` that ensures `make_move` does not overwrite an occupied cell and returns `False` when attempting to do so"""
    board = fresh_board # Get the fresh board from the fixture
    make_move(board, 0, 0, 'X')  # Place 'X' in an empty cell
    result = make_move(board, 0, 0, 'O')  # Attempt to overwrite the occupied cell
    assert not result  # Ensure that the move was unsuccessful
    assert board[0][0] == 'X'  # Confirm that 'X' remains in that cell


if __name__ == "__main__":
    pytest.main()
