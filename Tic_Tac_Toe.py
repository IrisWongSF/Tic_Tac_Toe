import pygame

pygame.init()


def main():
    # Set up game

    WHITE = (255, 255, 255)
    x = 10
    WIN_WIDTH = 300
    WIN_HEIGHT = 300

    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    pygame.display.set_caption("TIC TAC TOE")
    # Load The images
    Cross = pygame.image.load("Cross.png")
    Cross = pygame.transform.scale(Cross, (50, 50))
    O = pygame.image.load("Nought.png")
    O = pygame.transform.scale(O, (50, 50))
    line_width = 6

    board = []
    pos = []
    turn = 'X'

    def draw_grid():
        # Draw grid function, setup grid on the screen
        grid_colour = (50, 50, 50)

        WIN.fill(WHITE)
        for i in range(1, 3):
            """ This for loop is for drawing lines """
            pygame.draw.line(WIN, grid_colour, (0, i * 100), (WIN_WIDTH, i * 100), line_width)
            pygame.draw.line(WIN, grid_colour, (i * 100, 0), (i * 100, WIN_HEIGHT), line_width)

    for i in range(3):
        row = [0] * 3
        board.append(row)

    run = True
    clicked = False
    draw_grid()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
                print("clicked")
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                print("clicked2")
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]

                if board[cell_y // 100][cell_x // 100] == 0:

                    board[cell_y // 100][cell_x // 100] = turn
                    print(board)

                    if turn == "X":

                        pic = Cross
                    elif turn == "O":
                        pic = O

                    cell_x, cell_y = check_pos(cell_x, cell_y)

                    print("cell_x", cell_x)
                    print("cell_y", cell_y)

                    WIN.blit(pic, (cell_x, cell_y))

                    pygame.display.flip()
                    # check_winning_condition(board)
                    if check_winning_condition(board) or check_draw(board):
                        msg = ''
                        if check_winning_condition(board):
                            msg = "The winner is " + turn
                        else:
                            msg = "Draw !"
                        font = pygame.font.Font(None, 36)
                        message = font.render(msg, True, (255, 255, 255), (0, 0, 0))
                        message_rect = message.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

                        # create a new window for the message
                        message_window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
                        pygame.display.set_caption("Winner!")
                        # display the message and wait for the user to close the window
                        message_window.fill((0, 0, 0))
                        message_window.blit(message, message_rect)
                        pygame.display.flip()
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                        break

                    else:
                        if turn == "X":
                            turn = "O"
                        else:
                            turn = "X"

        pygame.display.update()

    pygame.quit()


def check_pos(cell_x, cell_y):
    if cell_x // 100 == 0 and cell_y // 100 == 0:
        print("opt 1 ")
        cell_x = 20
        cell_y = 30
    elif cell_x // 100 == 0 and cell_y // 100 == 1:
        print("opt 2 ")
        cell_x = 30
        cell_y = 130
    elif cell_x // 100 == 0 and cell_y // 100 == 2:
        print("opt 3 ")
        cell_x = 30
        cell_y = 230
    elif cell_x // 100 == 1 and cell_y // 100 == 0:
        print("opt 4 ")
        cell_x = 130
        cell_y = 30
    elif cell_x // 100 == 1 and cell_y // 100 == 1:
        print("opt 5 ")
        cell_x = 130
        cell_y = 130
    elif cell_x // 100 == 1 and cell_y // 100 == 2:
        print("opt 6 ")
        cell_x = 130
        cell_y = 230
    elif cell_x // 100 == 2 and cell_y // 100 == 0:
        print("opt 7 ")
        cell_x = 230
        cell_y = 30
    elif cell_x // 100 == 2 and cell_y // 100 == 1:
        print("opt 8 ")
        cell_x = 230
        cell_y = 130
    elif cell_x // 100 == 2 and cell_y // 100 == 2:
        print("opt 9 ")
        cell_x = 230
        cell_y = 230
    return cell_x, cell_y


def check_winning_condition(list):
    print(list)
    print(((list[0][0] == list[0][1] == list[0][2])))
    if ((((list[0][0] == list[0][1] == list[0][2])) and list[0][0] != 0)
            | (((list[1][0] == list[1][1] == list[1][2])) and list[1][0] != 0)
            | (((list[2][0] == list[2][1] == list[2][2])) and list[2][0] != 0)
            | (((list[0][0] == list[1][0] == list[2][0])) and list[0][0] != 0)
            | (((list[0][1] == list[1][1] == list[2][1])) and list[0][1] != 0)
            | (((list[0][2] == list[1][2] == list[2][2])) and list[0][2] != 0)
            | (((list[0][0] == list[1][1] == list[2][2])) and list[0][0] != 0)
            | (((list[0][2] == list[1][1] == list[2][0])) and list[0][2] != 0)):
        return True
    return False


def check_draw(list):
    return (0 not in list[0]) and (0 not in list[1]) and (0 not in list[2])


if __name__ == "__main__":
    main()
