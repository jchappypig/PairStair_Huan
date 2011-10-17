import Tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

CW = 30
RH = 15
NC = 10
NR = 20

sx, sy, ex, ey = CW, 0, CW, NR*RH
for col in range(NC):
    canvas.create_line(sx, sy, ex, ey)
    sx += CW
    ex += CW

sx, sy, ex, ey = 0, RH, CW*NC, RH
for row in range(NR):
    canvas.create_line(sx, sy, ex, ey)
    sy += RH
    ey += RH


root.mainloop()