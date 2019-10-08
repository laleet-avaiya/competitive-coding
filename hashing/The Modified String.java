// The Modified String
// 17 July 2019
// https://practice.geeksforgeeks.org/problems/the-modified-string/1/?ref=self

class solve{
    public static long modified(String a){
        // Your code here
        
    char prevChar = '1';
    int count = 0;
    int ans = 0;
    
    for(int i=0;i<a.length();i++)
    {
        if(a.charAt(i)==prevChar)
            count++;
        else
        {
            if(count>=3)
            {
                if(count%2!=0)
                    ans += count/2;    
                else
                    ans += (count-1)/2;
            }
            prevChar = a.charAt(i);
            count = 1;
        }       
    }
    
    if(count>=3)
    {
        if(count%2!=0)
            ans += count/2;    
        else
            ans += (count-1)/2;
    }
    
    return ans;
    }
}