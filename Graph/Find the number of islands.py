# Find the number of islands 
# https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1

def DFS(a,i,j,n,m):
    
    if(i<0 or i>=n or j<0 or j>=m or a[i][j]==0):
        return;
        
    a[i][j]=0;
    DFS(a,i+1,j,n,m);
    DFS(a,i-1,j,n,m);
    DFS(a,i,j+1,n,m);
    DFS(a,i,j-1,n,m);
    DFS(a,i+1,j+1,n,m);
    DFS(a,i-1,j-1,n,m);
    DFS(a,i-1,j+1,n,m);
    DFS(a,i+1,j-1,n,m);
    

def findIslands(a,n,m):
    #code 
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                ans += 1
                DFS(a,i,j,n,m)
    return ans



# -------------------JAVA--------------------

# class Islands
# {
    
#     // Function to find the number of island in the given list
#     // N, M: size of list row and column respectively
#     static void DFS(ArrayList<ArrayList<Integer>> list,int i,int j,int N, int M){
        
#         if(i<0 || j<0 || i>=N || j>=M || list.get(i).get(j)==0)
#             return;
        
#         list.get(i).set(j,0);
        
#         DFS(list,i-1,j,N,M);
#         DFS(list,i-1,j+1,N,M);
#         DFS(list,i,j+1,N,M);
#         DFS(list,i+1,j+1,N,M);
#         DFS(list,i+1,j,N,M);
#         DFS(list,i+1,j-1,N,M);
#         DFS(list,i,j-1,N,M);
#         DFS(list,i-1,j-1,N,M);
        
#     }
    
#     static int findIslands(ArrayList<ArrayList<Integer>> list, int N, int M)
#     {
        
#         // Your code here
#         int count=0;
        
#         for(int i=0;i<N;i++){
#             for(int j=0;j<M;j++){
#                 if(list.get(i).get(j)==1){
#                     DFS(list,i,j,N,M);
#                     count++;
#                 }
#             }
#         }
            
#         return count;
        
        
#     }
    
# }