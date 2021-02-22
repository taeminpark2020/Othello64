import utils
import tkinter
import GoroNet_arch

map = utils.map

model = GoroNet_arch.GoroNet()


root=tkinter.Tk()
root.geometry("480x480")
root.mainloop()


for epoch in range(100):
    for iter in range(60):
        x = input("input x")
        y = input("input y")
        if utils.check(x, y, map):
            break

        utils.flip_flop(1, 2, map[iter])
        output = model(map)