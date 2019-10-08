// Odd even level difference 
// 18 June 2019
// https://practice.geeksforgeeks.org/problems/odd-even-level-difference/1


class GfG
{   /*You are required to complete this function*/

    static int odd;
    static int even;

    int getLevelDiff(Node root)
    {
        // Your code here	
        odd=0;
        even=0;
        
        Queue<Node> q = new LinkedList<>();
        int[] level = new int[50000];
        q.add(root);
        int l=0;
        while(!q.isEmpty()){
            Node a = q.poll();
            l = level[a.data];
            
            if(l%2==0){
                even += a.data;
            }else{
                odd += a.data;
            }
            
            if(a.left!=null){
                q.add(a.left);
                level[a.left.data] = l+1;
            }
            
            if(a.right!=null){
                q.add(a.right);
                level[a.right.data] = l+1;
            }
        }
        return even-odd;
    }
}