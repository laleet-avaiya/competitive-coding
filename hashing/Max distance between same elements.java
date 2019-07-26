Max distance between same elements 
17 July 2019
https://practice.geeksforgeeks.org/problems/max-distance-between-same-elements/1

class GfG
{
    int maxDistance(int arr[], int n)
    {
	
	HashMap<Integer, Integer> map = new HashMap<>(); 

        int max_dist = 0; 
  
        for (int i = 0; i < n; i++) 
        { 
           
            if (!map.containsKey(arr[i])) 
                map.put(arr[i], i); 
  
            
            else
                max_dist = Math.max(max_dist, i - map.get(arr[i])); 
        } 
        
        return max_dist;
    }
}