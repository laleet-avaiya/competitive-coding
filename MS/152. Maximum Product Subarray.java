// 152. Maximum Product Subarray
// 18 July 2019
// https://leetcode.com/problems/maximum-product-subarray/submissions/

class Solution {
    public int maxProduct(int[] nums) {
        
        
		    int n = nums.length;
		    
		    int maxTillIndex;
		    int minTillIndex;
		    int globalMax;
		    
		   
		    
		    maxTillIndex = nums[0];
		    minTillIndex = nums[0];
		    globalMax = nums[0];
		    
		    for(int i=1;i<n;i++)
		    {
		        int a = nums[i];
		        int temp = maxTillIndex;
		        
		        maxTillIndex = Math.max(a,Math.max(maxTillIndex*a,minTillIndex*a));
		        
		        globalMax = Math.max(globalMax,maxTillIndex);
		        
		        minTillIndex = Math.min(a,Math.min(temp*a,minTillIndex*a));
		        
		    }
		   return (globalMax);
		        
		    
            
            
        
    }
}