// Right View of Binary Tree
// https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1

public class Temp {
    TreeNode node;
    int dis;

    Temp(TreeNode n, int d) {
        this.node = n;
        this.dis = d;
    }

}

class GfG {
    void rightView(TreeNode node) {
        // add code here.
        if (node == null)
            return;

        Queue<Temp> q = new LinkedList<>();
        Map<Integer, Integer> h = new TreeMap<>();

        q.add(new Temp(node, 0));

        while (!q.isEmpty()) {
            Temp obj = q.remove();

            TreeNode a = obj.node;
            int distance = obj.dis;

            // if(!h.containsKey(distance))
            h.put(distance, a.data);

            if (a.left != null)
                q.add(new Temp(a.left, distance + 1));

            if (a.right != null)
                q.add(new Temp(a.right, distance + 1));

        }

        for (Map.Entry<Integer, Integer> m : h.entrySet()) {
            System.out.print(m.getValue() + " ");
        }

    }
}