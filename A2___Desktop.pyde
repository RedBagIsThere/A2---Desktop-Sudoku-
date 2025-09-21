def setup():
   size(500,500)


def draw():
    draw_sudoku_table()


def draw_sudoku_table():
  
    table_line_x_axis = width/9
    table_line_y_axis = height/9
    
    i = 1
    
    while(i<=8):
        line(table_line_x_axis*i, 0 , table_line_x_axis*i, height)
        line(0, table_line_y_axis*i , width, table_line_y_axis*i)
        i+=1
    
