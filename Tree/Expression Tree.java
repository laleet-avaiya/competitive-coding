// Expression Tree
// 17 June 2019
// https://practice.geeksforgeeks.org/problems/expression-tree/1

class GfG{
    public int evalTree(Node node)
    {
    //Your code here.
    
    if(node==null) return 0;
    int lt=0,rt=0;
    
    if(node.left==null && node.right==null) 
        return Integer.parseInt(node.data);
        
    lt=evalTree(node.left);
    rt=evalTree(node.right);
    
    if(node.data.equals("+"))
        return lt+rt;
    if(node.data.equals("-"))
        return lt-rt;
    else if(node.data.equals("*"))
        return lt*rt;
    else //(node.data.equals("/"))
        return lt/rt;
    
    
}
}