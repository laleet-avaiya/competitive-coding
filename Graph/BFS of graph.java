// BFS of graph
// 09 June 2019
// https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

import java.util.*;

class Traversal {
    static void bfs(int s, ArrayList<ArrayList<Integer>> list, boolean vis[]) {
        Queue<Integer> q = new LinkedList<Integer>();

        q.add(0);
        vis[0] = true;

        while (!q.isEmpty()) {
            int p = q.remove();
            vis[p] = true;
            System.out.print(p + " ");

            for (int j = 0; j < list.get(p).size(); j++) {
                if (vis[list.get(p).get(j)] == false) {
                    q.add(list.get(p).get(j));
                    vis[list.get(p).get(j)] = true;
                }
            }
        }
    }
}

