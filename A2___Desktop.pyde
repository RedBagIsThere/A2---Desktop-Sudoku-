number_table= [
      [1,0,3,4,5,6,7,8,9],
      [1,2,3,4,0,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
      [1,2,3,0,5,6,7,8,9],
      [0,2,3,4,5,6,7,8,0],
      [1,2,3,4,5,6,7,8,9],
      [0,2,3,4,5,6,7,8,9],
      [1,0,3,4,5,6,7,8,9],
      [1,2,3,4,5,6,7,8,9],
    ]

select_number = [1,2,3,4,5,6,7,8,9]

size = 800
distance_between_line = size/9

selected = 0

def setup():
    
    global x_start,y_start
    fullScreen()
    textAlign(CENTER,CENTER)
    x_start =(displayWidth/2)-(size/2) #table first pos in a center of display
    y_start = (displayHeight/2)-(size/2)
    
def draw():
    
    background(255)
    
    draw_sudoku_table(x_start, y_start, distance_between_line, size);
    draw_number(x_start, y_start, distance_between_line);
    draw_select(x_start, y_start, distance_between_line)
    pick_number(x_start, y_start, distance_between_line)
    

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
    
    sqr_size = 80
    col = 0
    while col<9:
        output = select_number[col]
        strokeWeight(3)
        rect(x+d*10, y+(col*d), d, d)
        text(output, x+d*10+(d/2), y+(col*d)+(d/2))
        col+=1
        
def pick_number(x, y, d):
    
    global selected
        
    row = 0
        
    while row <9:
            
        if mouseX >= x+d*10 and mouseX <= x+d*11 and mouseY >= y+d*row and mouseY <= y+ d*(row+1) : 
                
            if mouseButton == LEFT :
                    
                selected = select_number[row]
                            
            
        row+=1
    
                 

    
    
    
