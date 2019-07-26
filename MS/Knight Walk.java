// Knight Walk
// 22 July 2019
// https://practice.geeksforgeeks.org/problems/knight-walk/0

/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;


class Cell{
    int x;
    int y;
 
    Cell(int x,int y){
        this.x=x;
        this.y=y;
    }
}
    
    
class GFG {
    
    static int[] move_row = {-2, -1, 1, 2, -2, -1, 1, 2};  
    static int[] move_col = {-1, -2, -2, -1, 1, 2, 2, 1};
    
    public static int FindMin(int s1,int s2,int d1,int d2,int n,int m)
    {
       
       
        int[][] Maze = new int[n][m];
        Queue<Cell> q = new LinkedList<>();
        
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                Maze[i][j] = 99999999;
	    
        
        q.add(new Cell(s1-1,s2-1));
        Maze[s1-1][s2-1]=0;
    
        while(!q.isEmpty()){
             
            Cell c=q.poll();
             
            for(int i=0;i<8;i++){
                 
                 int x=move_row[i]+c.x;
                 int y=move_col[i]+c.y;
                 
                 if(x>=0&& y>=0 && x<n && y<m)
                 {
                    int dis=Maze[c.x][c.y]+1;
                     
                    if(Maze[x][y]>dis)
                    {
                        Maze[x][y]=dis;
                        q.add(new Cell(x,y));
                    }   
                }
            }
        }
         
        return Maze[d1-1][d2-1]==99999999?-1:Maze[d1-1][d2-1];
         
        
    }
	public static void main (String[] args) {
		//code
		
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		while(t-->0)
		{
		    int n = s.nextInt();
		    int m = s.nextInt();
		    
		    // Src.
		    int s1 = s.nextInt();
		    int s2 = s.nextInt();
		    
		    // Dest.
		    int d1 = s.nextInt();
		    int d2 = s.nextInt();
		    
		    // Print minDistance
		    System.out.println(FindMin(s1,s2,d1,d2,n,m));
		}
	}
}