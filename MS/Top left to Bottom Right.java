/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;



class Codechef
{
   
public static void main (String[] args) throws java.lang.Exception
{
// your code goes here

// Scanner s = new Scanner(System.in);
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


// int t = s.nextInt();
int t = Integer.parseInt(br.readLine());

while(t-->0){
 //  int n = s.nextInt();
   int n = Integer.parseInt(br.readLine());

 
   int arr[][] = new int[n][n];
   
   
   for(int i =0;i<n;i++)
   {
        String[] s = br.readLine().split(" ");

       for(int j=0;j<n;j++){
           arr[i][j]= Integer.parseInt(s[j]);
     
       }
       
   }
           
   
    int ans[][] = new int[n][n];
    int ans2[][] = new int[n][n];
   
    for(int i =0;i<n;i++){
       for(int j=0;j<n;j++){
           if(i==0 && j==0){
               ans[i][j]=arr[0][0];
               ans2[i][j]=arr[0][0];
           }
         else{
             
           if(j<=i)
               ans[i][j] = 9999999;
           else if(i==0 && j!=0)
               ans[i][j] = ans[i][j-1]+arr[i][j];
           else if(i!=j)
               ans[i][j]= Math.min(ans[i-1][j],ans[i][j-1])+arr[i][j];
               
              if(j>=i)
               ans2[i][j] = 9999999;
           else if(j==0 && i!=0)
               ans2[i][j] = ans2[i-1][j]+arr[i][j];
           else if(i!=j)
               ans2[i][j]= Math.min(ans2[i][j-1],ans2[i-1][j])+arr[i][j];
         }
       }
    }
   
    int total = ans[n-2][n-1] + ans2[n-1][n-2] + arr[n-1][n-1];

 System.out.println(total);
}