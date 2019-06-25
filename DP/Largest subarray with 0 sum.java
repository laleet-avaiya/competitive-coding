// Largest subarray with 0 sum
// 20 June 2019
// https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

class GfG
{


    class GfG
{
    int maxLen(int arr[], int n)
    {
        int ans=0,sum=0;
        LinkedHashMap<Integer,Integer>m=new LinkedHashMap<Integer,Integer>();
        for(int i=0;i<n;i++)
        {
          sum=sum+arr[i];
          if(sum==0)
            ans=i+1;
          
          if(m.containsKey(sum)==true)
          {
              int num=m.get(sum);
              ans=Math.max(ans,i-num);
          }
          else
          {
              m.put(sum,i);
          }
}
          if(ans!=0)
            return ans;
          else
            return ans;
    }
}


    int maxLen(int a[], int n)
    {
        // Your code here
        int[][] G = new int[n][n];
        
        for(int i=0;i<n;i++)
            G[i][i]=a[i];
        
        for(int i =0;i<n;i++){
            for(int j=i+1;j<n;j++){
                G[i][j] = G[i][j-1]+G[j][j];
            }
        }
        
        int ans=0;
        for(int i =0;i<n;i++){
            for(int j=i;j<n;j++)
            {    
                
                if(G[i][j]==0){
                    if(ans<j-i+1){
                       ans = j-i+1;
                    }
                }
            }
        }
            
        return ans;
                
        
    }
}