def setup():
    
    fullScreen()

def draw():
    
    background(255)
    draw_sudoku_table(800)


def draw_sudoku_table(s):
  
    x =(width/2)-(s/2) #table first pos
    y = (height/2)-(s/2)
    table_line_x_axis = s/9
    table_line_y_axis = s/9
    
    rect(x,y,s,s)

    i = 1
    
    while i<=8 :
        line(x + table_line_x_axis*i, y , x+ table_line_x_axis*i, y + table_line_y_axis*9) # x-axis line
        line(x, y + table_line_y_axis*i , x + table_line_x_axis*9, y + table_line_y_axis*i) # y-axis line
        i+=1
    
    
    
    
