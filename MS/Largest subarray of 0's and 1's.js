// Largest subarray of 0's and 1's
// 18 July 2019
// https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1

class GfG
{
    /*You are required to complete this method*/ 
    int maxLen(int[] arr) 
    {
         // Your code here
        int n = arr.length;
        int ans = 0;
        for(int i=0;i<n;i++)
        {
            for(int j =i;j<n;j++)
            {
                int count_zero = 0;
                int count_one = 0;
                for(int k = i;k<=j;k++)
                {
                    if(arr[k]==0)
                        count_zero++;
                    else
                        count_one++;
                }
                if(count_zero==count_one)
                   if(j-i+1>ans)
                    ans=j-i+1;
            }
        }
        return ans;
    }
}
