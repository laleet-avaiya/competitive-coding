// 17. Delete without head pointer 
// https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1


class GfG
{
    void deleteNode(Node del)
    {
         // Your code here
         Node temp = del;
         Node forward = temp.next;
         Node prev =temp;
         while(forward!=null){
             prev=temp;
             temp.data=forward.data;
             temp=forward;
             forward = forward.next;
         }
         prev.next=null;
         
    }
}