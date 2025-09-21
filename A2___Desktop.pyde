number_table= [
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
    ]

def setup():
    
    fullScreen()
    textAlign(CENTER,CENTER)
    
def draw():
    
    background(255)
    draw_sudoku_table(800)


def draw_sudoku_table(s):
  
    x =(width/2)-(s/2) #table first pos in a center of display
    y = (height/2)-(s/2)
    distance_between_line = s/9
    
    strokeWeight(5)
    
    rect(x,y,s,s)

    i = 1
    
    while i<=8 :
        
        if i%3 == 0:
            strokeWeight(3)

        else:
            strokeWeight(1)       
        
        line(x + distance_between_line*i, y , x+ distance_between_line*i, y + distance_between_line*9) # x-axis line
        line(x, y + distance_between_line*i , x + distance_between_line*9, y + distance_between_line*i) # y-axis line
        
        i+=1
        
        draw_number(x, y, distance_between_line)
        
def draw_number(x, y, d):
  
    row = 0
    
    textSize(d*0.6)
    
    while row<9:
      
        col = 0
        
        while col<9:
            output = number_table[row][col]
            fill(0)
            text(output, x+d*col + d/2, y+d*row + d/2)
            noFill()
            col += 1
        
        row+=1
        
    
    
    
    
