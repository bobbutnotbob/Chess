import os
import tkinter as tk
from PIL import Image, ImageTk


def render_images():
    image_directory = "H:/Digital Programming/Python Programs/GUIZero/Pieces"
    images = []
    for file in os.listdir(image_directory):
        if file.endswith('.png'):
            load = Image.open('./Pieces/' + file)

            render = ImageTk.PhotoImage(load)
            images.append(render)
    load = Image.open('./chessboard.jpg')
    background_img = ImageTk.PhotoImage(load)
    return images, background_img


def main():
    root = tk.Tk()

    pieces, bg_img = render_images()
    black_pieces = []
    white_pieces = []

    # Create Chessboard
    background_label = tk.Label(root, image=bg_img)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Setup pawns
    for pawn in range(8):
        # Initialise white pawns
        white_pieces.append(tk.Button(root, image=pieces[9], height=60, width=60, bd=0))
        white_pieces[pawn].grid(row=1, column=pawn)

        # Initialise black pawns
        black_pieces.append(tk.Button(root, image=pieces[3], height=60, width=60, bd=0))
        black_pieces[pawn].grid(row=6, column=pawn)

    # Setup special pieces

    # Rooks
    white_pieces.append(tk.Button(root, image=pieces[11], height=60, width=60, bd=0))
    white_pieces[8].grid(row=0, column=0)
    white_pieces.append(tk.Button(root, image=pieces[11], height=60, width=60, bd=0))
    white_pieces[9].grid(row=0, column=7)

    black_pieces.append(tk.Button(root, image=pieces[5], height=60, width=60, bd=0))
    black_pieces[8].grid(row=7, column=0)
    black_pieces.append(tk.Button(root, image=pieces[5], height=60, width=60, bd=0))
    black_pieces[9].grid(row=7, column=7)

    # Knights
    white_pieces.append(tk.Button(root, image=pieces[8], height=60, width=60, bd=0))
    white_pieces[10].grid(row=0, column=1)
    white_pieces.append(tk.Button(root, image=pieces[8], height=60, width=60, bd=0))
    white_pieces[11].grid(row=0, column=6)

    black_pieces.append(tk.Button(root, image=pieces[2], height=60, width=60, bd=0))
    black_pieces[10].grid(row=7, column=1)
    black_pieces.append(tk.Button(root, image=pieces[2], height=60, width=60, bd=0))
    black_pieces[11].grid(row=7, column=6)

    # Bishops
    white_pieces.append(tk.Button(root, image=pieces[6], height=60, width=60, bd=0))
    white_pieces[12].grid(row=0, column=2)
    white_pieces.append(tk.Button(root, image=pieces[6], height=60, width=60, bd=0))
    white_pieces[13].grid(row=0, column=5)

    black_pieces.append(tk.Button(root, image=pieces[0], height=60, width=60, bd=0))
    black_pieces[12].grid(row=7, column=2)
    black_pieces.append(tk.Button(root, image=pieces[0], height=60, width=60, bd=0))
    black_pieces[13].grid(row=7, column=5)

    # Queens
    white_pieces.append(tk.Button(root, image=pieces[4], height=60, width=60, bd=0))
    white_pieces[14].grid(row=0, column=3)

    black_pieces.append(tk.Button(root, image=pieces[4], height=60, width=60, bd=0))
    black_pieces[14].grid(row=7, column=3)

    # Kings
    white_pieces.append(tk.Button(root, image=pieces[1], height=60, width=60, bd=0))
    white_pieces[15].grid(row=0, column=4)

    black_pieces.append(tk.Button(root, image=pieces[1], height=60, width=60, bd=0))
    black_pieces[15].grid(row=7, column=4)

    tk.mainloop()


if __name__ == '__main__':
    main()
