import tkinter
import random

game_over = False
score = 0
squares_to_clear = 0


def create_bombfield(b):
    global squares_to_clear
    for row in range(0, 10):
        row_List = []
        for column in range(0, 10):
            if random.randint(1, 100) < 20:
                row_List.append(1)
            else:
                row_List.append(0)
                squares_to_clear += 1
        b.append(row_List)


bombfield = []


def play_bobmdodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


def printfiled(bobmfield):
    for rowList in bobmfield:
        print(rowList)


def layout_window(window):
    for row_number, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(bombfield):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text='    ', bg='darkgreen')
            elif random.randint(1, 100) < 75:
                square = tkinter.Label(window, text='    ', bg='seagreen')
            else:
                square = tkinter.Label(window, text='    ', bg='green')
            square.grid(row=row_number, column=columnNumber)
            square.bind('<Button-1>', on_click)


def on_click(event):
    global score
    global game_over
    global squares_to_clear
    square = event.widget
    row = int(square.grid_info()['row'])
    column = int(square.grid_info()['column'])
    current_text = square.cget('text')
    if not game_over:
        if bombfield[row][column] == 1:
            game_over = True
            square.config(bg="red")
            print('Game over :(. You hit a bomb!')
            print('Your score:', score)
        elif current_text == '    ':
            square.config(bg="brown")
            total_bombs = 0
            if row < 9:
                if bombfield[row + 1][column] == 1:
                    total_bombs += 1

            if row > 0:
                if bombfield[row - 1][column] == 1:
                    total_bombs += 1

            if column > 0:
                if bombfield[row][column + 1] == 1:
                    total_bombs += 1

            if column < 9:
                if bombfield[row][column + 1] == 1:
                    total_bombs += 1

            if row > 0 and column > 0:
                if bombfield[row - 1][column - 1] == 1:
                    total_bombs += 1

            if row < 9 and column > 0:
                if bombfield[row + 1][column - 1] == 1:
                    total_bombs += 1

            if row > 0 and column < 9:
                if bombfield[row - 1][column + 1] == 1:
                    total_bombs += 1

            if row < 9 and column < 9:
                if bombfield[row + 1][column + 1] == 1:
                    total_bombs += 1
            square.config(text=' ' + str(total_bombs) + ' ')
            squares_to_clear -= 1
            score += 1
            if squares_to_clear == 0:
                game_over = True
                print('Well done! You found all the safe squares!')
                print('Your score was:', score)


play_bobmdodger()
