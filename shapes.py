import tkinter as tk

def create_canvas_with_shapes():
    # Create the main window
    root = tk.Tk()
    root.title("Canvas with Shapes")

    # Create a canvas widget
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Draw simple shapes on the canvas
    # Rectangle (x1, y1, x2, y2)
    canvas.create_rectangle(50, 50, 150, 150, fill="blue")

    # Circle (x, y, radius)
    canvas.create_oval(200, 50, 300, 150, fill="green")

    # Line (x1, y1, x2, y2)
    canvas.create_line(50, 200, 350, 200, fill="red", width=2)

    # Run the GUI event loop
    root.mainloop()

# Run the canvas with shapes
create_canvas_with_shapes()
