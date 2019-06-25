// # Twice counter
// # 17 June 2019
// # https://practice.geeksforgeeks.org/problems/twice-counter/0


class GFG {
	public static void main (String[] args) {
		//code
		Scanner s = new Scanner(System.in);
		
		int t = s.nextInt();
		while(t-->0){
		    Hashtable<String,Integer> ans = new Hashtable<>();
	
		    int n = s.nextInt();
		    s.nextLine();
		    String[] p = s.nextLine().split(" ");
		    
		    for(String a:p)
		    {
		        if(ans.containsKey(a)){
		            ans.put(a,ans.get(a)+1);
		        }else{
		            ans.put(a,1); 
		        }
		    }
		    
		    int count = 0;
		    Collection<Integer> ap = ans.values();
		    for(int i:ap)
		        if(i==2) count++;
		    System.out.println(count);
		}
	    
	}
}