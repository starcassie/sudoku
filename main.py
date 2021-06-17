from itertools import chain
import time
import tkinter as tk
from time import time

squaresFilled = 0

start = time()

test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def display(valArray, row, col):
  # displays the sudoku and highlight the new number solved for
  global squaresFilled
  window = tk.Tk()
  for i in range(9):
      for j in range(9):
          frame = tk.Frame(
              master=window,
              relief=tk.RAISED,
              borderwidth=1
          )
          frame.grid(row=i, column=j)
          if (row == i and col == j):
            label = tk.Label(master=frame, text=f"{valArray[i][j]}", width=2, height=1, bg="red")
            squaresFilled += 1
          elif (valArray[i][j] != 0):
            label = tk.Label(master=frame, text=f"{valArray[i][j]}", width=2, height=1)
          else:
            label = tk.Label(master=frame, text=" ", width=2, height=1)
          label.pack()
  window.geometry('+%d+%d'%(1000,400))
  window.after(1000, window.destroy)
  window.mainloop()

# easy
# vals = [[8, 5, 0, 0, 0, 1, 0, 0, 6], #5
#        [0, 0, 7, 0, 6, 4, 1, 0, 0], #5
#        [0, 0, 4, 0, 7, 0, 5, 9, 0], #5
#        [2, 0, 0, 0, 5, 6, 0, 0, 4], #5
#        [6, 0, 0, 1, 0, 9, 0, 7, 0], #5
#        [7, 0, 1, 0, 4, 0, 0, 0, 9], #5
#        [0, 1, 0, 9, 0, 0, 4, 6, 0], #5
#        [0, 9, 6, 0, 0, 8, 0, 0, 7], #5
#        [0, 7, 0, 6, 0, 0, 0, 0, 1]] #5

# hard
vals = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

# displays the initial values
display(vals, -1, -1)

# prints the initial values
print("unsolved")
for row in vals:
  print(row)

options = [[[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []],
        [[], [], [], [], [], [], [], [], []]]

# gives everything square all the options it could be filled in with initially
for row in range(9):
  for col in range(9):
    options[row][col] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def hasZeros():
  # checks if the sudoku is solved
  for row in vals:
    for num in row:
      if(num == 0):
        return True
  return False

# def countZeros():
#   number = 0;
#   for row in vals:
#     for num in row:
#       if(num == 0):
#         number += 1
#   return(number)

# holds the values of each ninth
quad = {1: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2,1], [2, 2]], 2: [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2,4], [2, 5]], 3: [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2,7], [2, 8]], 4: [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5,1], [5, 2]], 5: [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5,4], [5, 5]], 6: [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5,7], [5, 8]], 7: [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8,1], [8, 2]], 8: [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8,4], [8, 5]], 9: [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8,7], [8, 8]]}

# holds the ranges for each ninth
ranges = {1: [[*range(0,3)], [*range(0,3)]], 2: [[*range(0,3)], [*range(3,6)]], 3: [[*range(0,3)], [*range(6,9)]], 4: [[*range(3,6)], [*range(0,3)]], 5: [[*range(3,6)], [*range(3,6)]], 6: [[*range(3,6)], [*range(6,9)]], 7: [[*range(6,9)], [*range(0,3)]], 8: [[*range(6,9)], [*range(3,6)]], 9: [[*range(6,9)], [*range(6,9)]]}

#holds the ranges of the rows/cols outside of a ninth
rangesOut = {1: [[*range(6,9)], [*range(6,9)]], 2: [[*range(6,9)], [*chain(range(0,3),range(6,9))]], 3: [[*range(6,9)], [*range(0,6)]], 4: [[*chain(range(0,3),range(6,9))], [*range(6,9)]], 5: [[*chain(range(0,3),range(6,9))], [*chain(range(0,3),range(6,9))]], 6: [[*chain(range(0,3),range(6,9))], [*range(0,6)]], 7: [[*range(0,6)], [*range(6,9)]], 8: [[*range(0,6)], [*chain(range(0,3),range(6,9))]], 9: [[*range(0,6)], [*range(0,6)]]}

def update(row, col):
  # updates the display
  display(vals, row, col)

def getRanges(row, col):
  # gets the ranges for the square a specific number is in
  for key in quad.keys():
    if([row, col] in quad[key]):
      spot = key
  return(ranges[spot])
  
def checkValsV2(row, col):
  # checks to ensure that filled in numbers are removed from options
  # also checks in the row/col to remove filled in numbers from options
  # if there is only one option it set the number officially
  if(vals[row][col] != 0):
    options[row][col] = [vals[row][col]]
    return
  this = options[row][col]
  for num in range(9):
    if(vals[row][num] != 0 and vals[row][num] in this):
      this.remove(vals[row][num])
    if(vals[num][col] != 0 and vals[num][col] in this):
      this.remove(vals[num][col])
  rangesS = getRanges(row, col)
  rangeR = rangesS[0]
  rangeC = rangesS[1]
  for rows in rangeR:
    for cols in rangeC:
      if(vals[rows][cols] != 0 and vals[rows][cols] in this):
        this.remove(vals[rows][cols])
  options[row][col] = this
  if(len(this) == 1):
    vals[row][col] = this[0]
    update(row, col)
    for num in range(9):
      checkValsV2(row, num)
      checkValsV2(num, col)

def findOptions():
  # finds the options for each position in the grid
  for row in range(9):
    for col in range(9):
      checkValsV2(row, col)

def checkRows():
  # chekcs in each row if there is only one place where a number can be in a row
  rowin= 0
  for row in options:
    counts = [[],[],[],[],[],[],[],[],[],[]]
    colin = 0
    for col in row:
      for val in col:
        counts[val].append(colin)
      colin += 1
    for count in range(len(counts)):
      if(len(counts[count]) == 1 and vals[rowin][counts[count][0]] == 0):
        a = counts[count][0]
        vals[rowin][a] = count
        update(rowin, a)
    rowin += 1

def checkCols():
  # checks in each col if there is only one place where a number can be in a col
  for col in range(9):
    counts = [[],[],[],[],[],[],[],[],[],[]]
    for row in range(9):
      for val in options[row][col]:
        counts[val].append(row)
    for count in range(len(counts)):
      if(len(counts[count]) == 1 and vals[counts[count][0]] == 0):
        a = counts[count][0]
        vals[a][col] = count
        update(a, col)

def checkSquaresV2():
  # checks in each square if there is only one place wehre a number can be in a square
  for key in quad.keys():
    counts = [[],[],[],[],[],[],[],[],[],[]]
    rangeS = ranges[key]
    rangeR = rangeS[0]
    rangeC = rangeS[1]
    rangeO = rangesOut[key]
    rangeOR = rangeO[0]
    rangeOC = rangeO[1]
    for row in rangeR:
      for col in rangeC:
        for val in options[row][col]:
          counts[val].append([row, col])
    for count in range(len(counts)):
      if(len(counts[count]) == 1 and vals[counts[count][0][0]][counts[count][0][1]] == 0):
        a=counts[count][0]
        vals[a[0]][a[1]] = count
        update(a[0], a[1])
      elif(len(counts[count]) > 1):
        rowM = counts[count][0][0]
        colM = counts[count][0][1]
        rowE = True
        colE = True
        for pair in counts[count]:
          if(pair[0] != rowM):
            rowE = False
          if(pair[1] != colM):
            colE = False
          if(not(rowE) and not(colE)):
            break
        if(rowE):
          for colR in rangeOC:
            if(count in options[rowM][colR]):
              options[rowM][colR].remove(count)
        elif(colE):
          for rowR in rangeOR:
            if(count in options[rowR][colM]):
              options[rowR][colM].remove(count)

while(hasZeros()):
  # cycles through the functions to solve the sudoku
  findOptions()
  if(not hasZeros()):
    break
  checkRows()
  if(not hasZeros()):
    break
  findOptions()
  if(not hasZeros()):
    break
  checkCols()
  if(not hasZeros()):
    break
  findOptions()
  if(not hasZeros()):
    break
  checkSquaresV2()

# creates the intial window
window = tk.Tk()
for i in range(9):
  for j in range(9):
    frame = tk.Frame(
      master=window,
      relief=tk.RAISED,
      borderwidth=1
    )
    frame.grid(row=i, column=j)
    label = tk.Label(master=frame, text=f"{vals[i][j]}", width=2, height=1)
    label.pack()
window.geometry('+%d+%d'%(1000,400))
window.mainloop()

# prints the solved once the tk window is closed
print()
print("solved")
for row in vals:
  print(row)
