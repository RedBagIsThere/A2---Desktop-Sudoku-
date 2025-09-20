int number_table[][]= {
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
      {1,2,3,4,5,6,7,8,9},
    };

int select_number[] = {1,2,3,4,5,6,7,8,9};

void setup(){
  
    fullScreen();
    textAlign(CENTER,CENTER);
}

void draw(){
    
    background(255);
    draw_sudoku_table(800);
    draw_select();
}

void draw_sudoku_table(float s){
  
    float x = (width/2)-(s/2); // table first pos in a center of display
    float y = (height/2)-(s/2);
    float distance_between_line = s/9;
    
    
    strokeWeight(5);
    rect(x,y,s,s);
    
    int i = 1;
    
    while(i<=8){
        
        if(i%3 == 0){
            strokeWeight(3);
        }
        else{
            strokeWeight(1);        
        }
        
        line(x + distance_between_line*i, y , x+ distance_between_line*i, y + distance_between_line*9); // x-axis line
        line(x, y + distance_between_line*i , x + distance_between_line*9, y + distance_between_line*i); // y-axis line
        
        i+=1;
    }
    
        draw_number(x, y, distance_between_line);
}

void draw_number(float x, float y, float d){
  
    int row = 0;
    
    textSize(d*0.6);
    
    while(row<9){
      
        int col = 0;
        
        while(col<9){
            int output = number_table[row][col];
            fill(0);
            text(output, x+d*col + d/2, y+d*row + d/2);
            noFill();
            col += 1;
            
        }
        
        row+=1;
        
    }
    
}

void draw_select(){
    int sqr_size = 80;
    int col = 0;
    while(col<9){
        int output = select_number[col];
        strokeWeight(3);
        rect(width-200, 100+(col*sqr_size), sqr_size, sqr_size);
        text(output, width-200+(sqr_size/2), 100+(col*sqr_size)+(sqr_size/2));
        col+=1;
    }
}
