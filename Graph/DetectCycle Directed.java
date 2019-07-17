class DetectCycle
{
    
    
    static boolean[] visited;
    static boolean[] recStack;
    static boolean ans;
    static int n;

    
    
    static void DFS(ArrayList<ArrayList<Integer>> list,int s){
        
                                        // if already visited Return
        if (visited[s])
            return;
                                        // mark visited and in recStack
        visited[s] = true;
        recStack[s] = true; 
        
        for(int i=0; i<list.get(s).size(); i++)
        {
                                        // if in recStack => Cycle Detect.
            if(recStack[list.get(s).get(i)]==true)
                ans=true;
            DFS(list,list.get(s).get(i));
        }
        recStack[s] = false; 
    }
    
    static boolean isCyclic(ArrayList<ArrayList<Integer>> list, int V)
    {
        n = V;
        ans = false;
        visited = new boolean[V]; 
        recStack = new boolean[V]; 
        
        for(int i=0;i<V;i++)
                   DFS(list,i);
                   
        return ans;
    }
}