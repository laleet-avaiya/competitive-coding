// Vertical sum 
// 18 June 2019
// https://practice.geeksforgeeks.org/problems/vertical-sum/1/?ref=self


class GfG
{
    public static void printVertical(Node root)
    {
        // add your code here
        int[] vd = new int[5000];
        if(root==null){
            System.out.print(0);
        }else{
            Queue<Node> q = new LinkedList<>();
            Map<Integer,Integer> ans = new TreeMap<>();
            q.add(root);
            int v;
            while(!q.isEmpty()){
                Node a = q.poll();
                v = vd[a.data];
                
                if(ans.containsKey(v)){
                    ans.put(v,ans.get(v)+a.data);
                }else{
                    ans.put(v,a.data);
                }
                
                if(a.left!=null){
                    q.add(a.left);
                    vd[a.left.data] = v-1;
                }
                if(a.right!=null){
                    q.add(a.right);
                    vd[a.right.data] = v+1;
                }
            }
            for(int a:ans.values())
            System.out.print(a + " ");
        }
        // System.out.println("");
        
        
    }
    
}
