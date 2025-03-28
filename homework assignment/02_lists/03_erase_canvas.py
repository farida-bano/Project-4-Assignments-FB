import tkinter as tk
from tkinter import colorchooser

CELL_SIZE = 20
ROWS = 20
COLS = 20
ERASER_SIZE = 40

class CanvasApp:
    def __init__(self, root):
        self.root = root
        self.cell_color = "blue"
        self.bg_color = "white"
        
        # Setup main canvas
        self.canvas = tk.Canvas(root, 
                               width=COLS*CELL_SIZE, 
                               height=ROWS*CELL_SIZE, 
                               bg=self.bg_color)
        self.canvas.pack(pady=10)
        
        # Control buttons frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)
        
        # Color selection buttons
        self.cell_color_btn = tk.Button(self.button_frame, 
                                       text="Choose Cell Color", 
                                       command=self.choose_cell_color)
        self.cell_color_btn.pack(side=tk.LEFT, padx=5)
        
        self.bg_color_btn = tk.Button(self.button_frame,
                                     text="Choose Background Color",
                                     command=self.choose_bg_color)
        self.bg_color_btn.pack(side=tk.LEFT, padx=5)
        
        # Reset button
        self.reset_btn = tk.Button(self.button_frame,
                                  text="Reset Grid",
                                  command=self.reset_grid)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        # Drawing variables
        self.is_erasing = False
        self.eraser_rect = None
        self.cells = []

        self.draw_grid()
        self.setup_events()

    def draw_grid(self):
        """Draw the initial grid with current cell color"""
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(
                    x1, y1, x2, y2, 
                    fill=self.cell_color, 
                    outline="black"
                )
                row_cells.append(cell)
            self.cells.append(row_cells)

    def setup_events(self):
        """Bind mouse events to canvas"""
        self.canvas.bind("<ButtonPress-1>", self.start_erasing)
        self.canvas.bind("<B1-Motion>", self.erase)
        self.canvas.bind("<ButtonRelease-1>", self.stop_erasing)

    # Event handlers
    def start_erasing(self, event):
        self.is_erasing = True
        self.update_eraser(event)

    def erase(self, event):
        if self.is_erasing:
            self.update_eraser(event)

    def stop_erasing(self, event):
        self.is_erasing = False
        if self.eraser_rect:
            self.canvas.delete(self.eraser_rect)

    def update_eraser(self, event):
        """Update eraser position and erase cells"""
        x = event.x - ERASER_SIZE//2
        y = event.y - ERASER_SIZE//2

        # Update eraser visual
        if self.eraser_rect:
            self.canvas.delete(self.eraser_rect)
        self.eraser_rect = self.canvas.create_rectangle(
            x, y, x+ERASER_SIZE, y+ERASER_SIZE,
            outline="red", width=2
        )

        # Optimized erasing
        self.erase_cells(x, y)

    def erase_cells(self, eraser_x, eraser_y):
        """Erase cells under the eraser using optimized bounds checking"""
        # Calculate affected cell range
        min_col = max(0, eraser_x // CELL_SIZE)
        max_col = min(COLS-1, (eraser_x + ERASER_SIZE) // CELL_SIZE)
        min_row = max(0, eraser_y // CELL_SIZE)
        max_row = min(ROWS-1, (eraser_y + ERASER_SIZE) // CELL_SIZE)

        # Check only relevant cells
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                cell_x = col * CELL_SIZE
                cell_y = row * CELL_SIZE
                
                # Check collision with eraser
                if (cell_x < eraser_x + ERASER_SIZE and
                    cell_x + CELL_SIZE > eraser_x and
                    cell_y < eraser_y + ERASER_SIZE and
                    cell_y + CELL_SIZE > eraser_y):
                    
                    self.canvas.itemconfig(self.cells[row][col], fill=self.bg_color)

    # Color management
    def choose_cell_color(self):
        """Change color for cells"""
        color = colorchooser.askcolor()[1]
        if color:
            self.cell_color = color

    def choose_bg_color(self):
        """Change background color and eraser effect"""
        color = colorchooser.askcolor()[1]
        if color:
            self.bg_color = color
            self.canvas.config(bg=color)

    def reset_grid(self):
        """Reset all cells to current cell color"""
        for row in self.cells:
            for cell in row:
                self.canvas.itemconfig(cell, fill=self.cell_color)

def main():
    root = tk.Tk()
    root.title("Improved Canvas Eraser")
    CanvasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
