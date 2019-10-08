
// Count the number of nodes at given level in a tree using BFS.
// 09 June 2019
// https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/

import java.util.*;

class Temp {
    int val;
    int level;

    Temp(int v, int level) {
        this.val = v;
        this.level = level;
    }
}

class TreeBFS {
    static int level;
    static int count;

    static List<Integer> ans;

    public static void BFS(int[][] g, int s) {
        Queue<Temp> q = new LinkedList<Temp>();
        boolean[] visited = new boolean[g.length];
        q.add(new Temp(s, 0));

        while (!q.isEmpty()) {
            Temp p = q.remove();

            if (p.level == level) {
                ans.add(p.val);
                count++;
            }
            for (int i = 0; i < g.length; i++) {
                if (g[p.val][i] == 1 && visited[i] == false) {
                    q.add(new Temp(i, p.level + 1));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int n = s.nextInt();
        int[][] G = new int[n][n];

        for (int i = 0; i < n - 1; i++) {
            int from = s.nextInt();
            int to = s.nextInt();

            G[from][to] = 1;
            // G[to][from] = 1;
        }
        ans = new ArrayList<>();
        level = s.nextInt();
        count = 0;
        BFS(G, 0);

        for (int i = 0; i < ans.size(); i++) {
            System.out.print(ans.get(i) + " ");
        }
        System.out.println(count);
    }
}