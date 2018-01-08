from tkinter import *
import sudoku

puzzle = []
master = Tk()


def solve_puzzle():
    z = []
    x = [i.get() for i in puzzle]
    for i in range(len(x)):
        if x[i]=='':
            z.append(0)
        else:
            z.append(int(x[i]))

    y = [z[9*i:9*(i+1)] for i in range(9)]
    sudoku.solveSudoku(y)
    print(y)





for i in range(1, 10):
    for j in range(1, 10):
        entry = Entry(master)
        entry.grid(row=i, column=j)
        puzzle.append(entry)
        # Label(master, text =str(i) ).grid(row=i)



Button(master, text='Solve', command=solve_puzzle).grid(row=12, column=0, sticky=W, pady=4)
#Button(master, text='Check', command=show_entry_fields).grid(row=12, column=1, sticky=W, pady=4)



mainloop()
