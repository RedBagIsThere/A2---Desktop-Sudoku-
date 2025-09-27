size = 800

def setup():
    
    global x_start,y_start,number_table,select_number,distance_between_line,selected
    fullScreen()
    textAlign(CENTER,CENTER)
    x_start =(displayWidth/2)-(size/2) #table first pos in a center of display
    y_start = (displayHeight/2)-(size/2)
    number_table= load_sudoku('table.txt')
    select_number = [1,2,3,4,5,6,7,8,9]
    distance_between_line = size/9
    selected = 0
    game_status = True
    
def draw():
    
    background(255)
    
    draw_sudoku_table(x_start, y_start, distance_between_line, size)
    draw_number(x_start, y_start, distance_between_line)
    draw_select(x_start, y_start, distance_between_line)
    pick_number(x_start, y_start, distance_between_line)
    input_number(x_start, y_start, distance_between_line)
    check_sudoku_row(x_start, y_start, distance_between_line)
    check_sudoku_col(x_start, y_start, distance_between_line)
    check_sudoku_box_3x3(x_start, y_start, distance_between_line)

    

def draw_sudoku_table(x, y, d, s):
  
    strokeWeight(5)
    
    rect(x,y,s,s)

    i = 1
    
    while i<=8 :
        
        if i%3 == 0:
            strokeWeight(3)

        else:
            strokeWeight(1)       
        
        line(x + d*i, y , x+ d*i, y + d*9) # x-axis line
        line(x, y + d*i , x + d*9, y + d*i) # y-axis line
        
        i+=1

        
def draw_number(x, y, d):
  
    row = 0
    
    textSize(d*0.6)
    
    while row<9:
      
        col = 0
        
        while col<9:
            output = number_table[row][col]
            
            if output != 0:
                fill(0)
                text(output, x+d*col + d/2, y+d*row + d/2)
                noFill()
                
            col += 1
        
        row+=1
        
def draw_select(x, y, d):
    
    col = 0
    while col<9:
        output = select_number[col]
        strokeWeight(3)
        rect(x+d*10, y+(col*d), d, d)
        fill(0)
        text(output, x+d*10+(d/2), y+(col*d)+(d/2))
        noFill()
        col+=1
        
def pick_number(x, y, d):
    
    global selected
        
    row = 0
    while row <9:
        if mouseX >= x+d*10 and mouseX <= x+d*11 and mouseY >= y+d*row and mouseY <= y+ d*(row+1) : 
            if mouseButton == LEFT :
                selected = select_number[row]
                            
            
        row+=1
    
                 
def input_number(x, y, d):
    
    row = 0
    while row <9:
        col = 0
        while col<9:
            if mouseX >= x+d*col and mouseX <= x+d*(col+1) and mouseY >= y+d*row and mouseY <= y+d*(row+1):
                if mouseButton == LEFT :
                    number_table[row][col] = selected
            col+=1
        
        row+=1
        
def check_sudoku_row(x, y, d):
    
    #check row
    row = 0
    while row<9:
        col = 0
        while col < 9:
            i = 1
            while col+i <9:

                if number_table[row][col] == number_table[row][col+i] and number_table[row][col] != 0:
                    fill(255, 0, 0, 50)
                    rect(x+d*col, y+d*row, d, d)
                    rect(x+d*(col+i), y+d*row, d, d)
                    noFill()
                    
                i+=1
            col+=1
        row+=1
    
        
def check_sudoku_col(x, y, d):
    
    #check col
    col = 0
    while col<9:
        row = 0
        while row < 9:
            i = 1
            while row+i <9:

                if number_table[row][col] == number_table[row+i][col] and number_table[row][col] != 0:
                    fill(255, 0, 0, 50)
                    rect(x+d*col, y+d*row, d, d)
                    rect(x+d*col, y+d*(row+i), d, d)
                    noFill()
                    
                i+=1
                
            row+=1
            
        col+=1
        
def check_sudoku_box_3x3(x, y, d):

    box_row = 0
    while box_row < 9: #box
        box_col = 0
        while box_col <9:
            
            row = 0
            while row<3: #in box
                col = 0
                while col<3:
                    current_row = box_row+row
                    current_col = box_col+col
                    
                    i = 0
                    while i<3: # check in box
                        j = 0
                        while j <3:
                            check_row = box_row+i
                            check_col = box_col+j
                            if(current_row != check_row or current_col != check_col):
                                if(number_table[current_row][current_col] == number_table[check_row][check_col] and number_table[current_row][current_col] != 0):
                                    fill(255, 0, 0, 50)
                                    rect(x+d*current_col, y+d*current_row, d, d)
                                    rect(x+d*check_col, y+d*check_row, d, d)
                                    noFill()
                                
                            j+=1
                        i+=1
                    
                    col+=1
                row+=1
                
            box_col+=3
        box_row+=3
        
def load_sudoku(file_name):
    
    table = []
    
    f = open(file_name)
    for line in f:
        row = [int(char) for char in line.strip()]
        table.append(row)
    f.close()
    
    return table
        
    
