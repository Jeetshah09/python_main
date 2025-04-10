import tkinter as tk

def create_game_board():
    # Create the main window
    root = tk.Tk()
    root.title("3x3 Game Board")

    # Create a 3x3 grid of buttons
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text=f"({row},{col})", width=10, height=3)
            button.grid(row=row, column=col, padx=5, pady=5)

    # Run the GUI event loop
    root.mainloop()

# Run the game board
create_game_board()
