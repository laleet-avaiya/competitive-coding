/*
* Frequency Game
* 12 Oct. 2019
* https://practice.geeksforgeeks.org/problems/frequency-game/1
*/

class Geeks
{
    // Function to find largest number with minimum frequency
    public static int LargButMinFreq(int arr[], int n)
    {
        
        // Todo : Step 1. Count Freq.
        
        Map<Integer,Integer> m = new HashMap<>();
        
        for(int i=0;i<n;i++)
        {
            if(m.containsKey(arr[i]))
                m.put(arr[i],m.get(arr[i])+1);
            else
                m.put(arr[i],1);
        }
        
        // Todo : Step 2. store freq : Max Element 
        
        Map<Integer,Integer> t = new TreeMap<>();
        
        for(Map.Entry<Integer,Integer> entry : m.entrySet())
        {    
            int element = entry.getKey();
            int newkey_freq = entry.getValue();
            
            if(t.containsKey(newkey_freq))
            {
                if(element>t.get(newkey_freq)){
                    t.put(newkey_freq,element);
                }
            }
            else
            {
                t.put(newkey_freq,element);
            }
        }
        
        // Todo : Step 3. return 1st element
        int ans=0;
        for(Map.Entry<Integer,Integer> entry : t.entrySet())
        {
            ans =  entry.getValue();
            break;
        }
        return ans;
    }
}