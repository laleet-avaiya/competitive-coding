// Minimum indexed character
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/minimum-indexed-character/1

class solve{
    public static void solution(String str, String patt){
        // Your code here
        
        HashMap<Character, Integer> map = new HashMap<>(); 
    
        for(int i=0;i<str.length();i++)
            if(!map.containsKey(str.charAt(i)))
                map.put(str.charAt(i),i);
        
        int ans = 9999;
        char c='a';
        for(int i=0;i<patt.length();i++)
        {
            if(map.containsKey(patt.charAt(i)))
            {
                if(map.get(patt.charAt(i))<ans)
                {
                   ans = map.get(patt.charAt(i));
                   c = patt.charAt(i);
                }
                
            }
        }
            
            
        if(ans == 9999)
            System.out.print("No character present");
        else
            System.out.print(c);
    }
}