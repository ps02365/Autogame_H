import tkinter as tk

class RectangleCaptureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rectangle Capture App")

        self.canvas = tk.Canvas(self.master, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.rect_start = None
        self.rect_id = None

        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_drag(self, event):
        if self.rect_start:
            self.canvas.delete(self.rect_id)
            x, y = self.rect_start
            x_end, y_end = event.x, event.y
            self.rect_id = self.canvas.create_rectangle(x, y, x_end, y_end, outline="blue")

    def on_release(self, event):
        if self.rect_start:
            x, y = self.rect_start
            x_end, y_end = event.x, event.y
            rect_x = min(x, x_end)
            rect_y = min(y, y_end)
            rect_width = abs(x_end - x)
            rect_height = abs(y_end - y)
            print(f"Rectangle coordinates: x={rect_x}, y={rect_y}, width={rect_width}, height={rect_height}")
            self.rect_start = None
            self.canvas.delete(self.rect_id)

    def run(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleCaptureApp(root)
    app.run()