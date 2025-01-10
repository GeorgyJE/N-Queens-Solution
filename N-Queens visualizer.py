'''this interactive board is not for looking at solutions, but rather it was a part of solving the problem.
this board only helps you visualize the queens and the squares they attack in order for you to experiment with
different options and find the best technique to solve the problem.'''
import pygame
import attack_target
pygame.init()

#              ----all dimentions----
# Screen dimensions
WIDTH, HEIGHT = 600, 600
#ROWS = 4
ROWS = int(input("select how mny rows"))
SQUARE_SIZE = WIDTH // ROWS
# ANY COL --> MOUSE_POS[0]
# ANY ROW --> MOUSE_POS[1]
# ROWS GO TO THE SIDE AND ARE NUMBERED FROM UP TO DOWN
# COLUMNS GO DOWN AND ARE NUMBERED FROM LEFT TO RIGHT

# Colors and pieces
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pieces = {
    "white_queen": pygame.transform.scale(pygame.image.load("images/new_black_queen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "black_queen": pygame.transform.scale(pygame.image.load("images/new_white_queen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "marked_white_queen": pygame.transform.scale(pygame.image.load("images/new_marked_black_queen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "marked_black_queen": pygame.transform.scale(pygame.image.load("images/new_marked_white_queen.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    # "black_queen":
    "white_x": pygame.transform.scale(pygame.image.load("images/marked_white.png"), (SQUARE_SIZE, SQUARE_SIZE)),
    "black_x": pygame.transform.scale(pygame.image.load("images/marked_black.png"), (SQUARE_SIZE, SQUARE_SIZE))
    # "marked_W_queen":
    # "marked_B_queen":

}


board = []
for i in range(ROWS):
    board = board + [[]]
for row in range(len(board)):
    for col in range(ROWS):
        new_square = attack_target.X(row, col)
        new_square.color = "WHITE" if (row + col) % 2 == 0 else "BLACK"
        board[row] = board[row] + [new_square]

'''
for i in board:
    for x in i:
        print(x.row,end=",")
        print(x.col, end=" ")
    print("")
    '''

#              ----Initialize screen----
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens visualizer")



#           ----drawing functions----

def draw_chessboard():
    for row in range(ROWS):
        for col in range(ROWS):
            color = board[row][col].color
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

#               ----game interactions----

def what_square(mouse_pos):
    col = mouse_pos[0] // SQUARE_SIZE  # Integer division to find column
    row = mouse_pos[1] // SQUARE_SIZE  # Integer division to find row
    return row, col


def calculate_attacks(row, col):
    """Calculate all squares this queen attacks."""
    attacked_squares = []

    # Horizontal and Vertical Attacks
    for r in range(ROWS):
        attacked_squares.append((r, col))  # Vertical
    for c in range(ROWS):
        attacked_squares.append((row, c))  # Horizontal

    # Diagonal Attacks
    for i in range(1, max(ROWS, ROWS)):
        if row + i < ROWS and col + i < ROWS:
            attacked_squares.append((row + i, col + i))  # Down-right diagonal
        if row - i >= 0 and col - i >= 0:
            attacked_squares.append((row - i, col - i))  # Up-left diagonal
        if row + i < ROWS and col - i >= 0:
            attacked_squares.append((row + i, col - i))  # Down-left diagonal
        if row - i >= 0 and col + i < ROWS:
            attacked_squares.append((row - i, col + i))  # Up-right diagonal

    while(row,col) in attacked_squares:
        attacked_squares.remove((row,col))
    return attacked_squares

def place_image(current_square, row, col):
    if current_square.queens > 0:
        if current_square.IsQueen:
            if current_square.color == "WHITE":
                screen.blit(pieces["marked_white_queen"], (col * SQUARE_SIZE, row * SQUARE_SIZE))
            else:
                screen.blit(pieces["marked_black_queen"], (col * SQUARE_SIZE, row * SQUARE_SIZE))
        else:
            if current_square.color == "WHITE":
                screen.blit(pieces["white_x"], (col * SQUARE_SIZE, row * SQUARE_SIZE))
            else:
                screen.blit(pieces["black_x"], (col * SQUARE_SIZE, row * SQUARE_SIZE))
    else:
        if current_square.IsQueen:
            if current_square.color == "WHITE":
                screen.blit(pieces["white_queen"], (col * SQUARE_SIZE, row * SQUARE_SIZE))
            else:
                screen.blit(pieces["black_queen"], (col * SQUARE_SIZE, row * SQUARE_SIZE))
        else:
            color = board[row][col].color
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    running = True
    # Draw chessboard
    draw_chessboard()

    while running:
        # Event handling (close window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse click for adding or removing the queen
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button down
                mouse_pos = pygame.mouse.get_pos()
                square_pos = what_square(mouse_pos)  # Convert mouse position to grid coordinates
                current = board[square_pos[0]][square_pos[1]]
                attacked_squares = calculate_attacks(square_pos[0], square_pos[1])

                if current.IsQueen == False:  # No queen on this square, place a queen
                    current.IsQueen = True
                    place_image(board[square_pos[0]][square_pos[1]],square_pos[0],square_pos[1])
                    for square in attacked_squares:
                        board[square[0]][square[1]].queens += 1
                        place_image(board[square[0]][square[1]], square[0], square[1])

                else:  # A queen is already on this square, remove it
                    current.IsQueen = False
                    place_image(board[square_pos[0]][square_pos[1]], square_pos[0], square_pos[1])
                    for square in attacked_squares:
                        board[square[0]][square[1]].queens -= 1
                        place_image(board[square[0]][square[1]], square[0], square[1])


            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button released
                button_clicked = False  # Reset button clicked state after the button is released
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()

