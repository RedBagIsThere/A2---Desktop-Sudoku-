void setup(){
  
    fullScreen();
    
}

void draw(){
    
    background(255);
    draw_sudoku_table(800);
}

void draw_sudoku_table(float s){
    float x = (width/2)-(s/2); // table first pos
    float y = (height/2)-(s/2);
    float table_line_x_axis = s/9;
    float table_line_y_axis = s/9;
    
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
        line(x + table_line_x_axis*i, y , x+ table_line_x_axis*i, y + table_line_y_axis*9); // x-axis line
        line(x, y + table_line_y_axis*i , x + table_line_x_axis*9, y + table_line_y_axis*i); // y-axis line
        i+=1;
    }
    
}
