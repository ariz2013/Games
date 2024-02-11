import tkinter
import time

canvas_width = 1000
canvas_height = 700
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvas_width, height=canvas_height, bg="darkblue")
canvas.pack()

bat = canvas.create_rectangle(0, 0, 30, 10, fill="red")
ball = canvas.create_oval(400, 250, 450, 300, fill="yellow")
window_open = True


def main_loop():
    while window_open:
        move_bat()
        move_ball()
        window.update()
        time.sleep(0.02)
        if window_open:
            check_game_over()


left_pressed = 0
right_pressed = 0


def on_key_press(event):
    global left_pressed, right_pressed
    if event.keysym == 'Left':
        left_pressed = 1
    elif event.keysym == 'Right':
        right_pressed = 1


def on_key_release(event):
    global left_pressed, right_pressed
    if event.keysym == 'Left':
        left_pressed = 0
    elif event.keysym == 'Right':
        left_pressed = 0


bat_speed = 8


def move_bat():
    bat_move = bat_speed * right_pressed - bat_speed * left_pressed
    (bat_left, bat_top, bat_right, bat_bottom) = canvas.coords(bat)
    if (bat_left > 0 or bat_move > 0) and (bat_right < canvas_width or bat_move < 0):
        canvas.move(bat, bat_move, 0)


ball_move_x = 4
ball_move_y = -4
set_bat_top = canvas_height - 40
set_bat_bottom = canvas_height - 30


def move_ball():
    global ball_move_x, ball_move_y
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
    if ball_move_x > 0 and ball_right > canvas_width:
        ball_move_x = -ball_move_x
    if ball_move_x < 0 and ball_left < 0:
        ball_move_x = -ball_move_x
    if ball_move_y < 0 and ball_top < 0:
        ball_move_y = -ball_move_y
    if ball_move_y > 0 and set_bat_top < ball_bottom < set_bat_bottom:
        (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
        if batRight > batLeft and ball_left < batRight:
            ball_move_y = -ball_move_y
    canvas.move(ball, ball_move_x, ball_move_y)


def check_game_over():
    (ball_left, ball_top, ball_right, ball_bottom) = canvas.coords(ball)
    if ball_top > canvas_height:
        play_again = tkinter.messagebox.askeysno(message='Do you want to play again?')
        if play_again:
            reset()
        else:
            close()


def close():
    global window_open
    window_open = False
    window.destroy()


def reset():
    global left_pressed, right_pressed
    global ball_move_x, ball_move_y
    left_pressed = 0
    right_pressed = 0
    ball_move_x = 4
    ball_move_y = -4
    canvas.coords(bat, 10, set_bat_top, 50, set_bat_bottom)
    canvas.coords(ball, 20, set_bat_top - 10, 10, set_bat_top)


window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)
reset()
main_loop()
