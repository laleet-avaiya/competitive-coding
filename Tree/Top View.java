//  Tree : Top View
//  https://www.hackerrank.com/challenges/tree-top-view/problem

public static class Temp {
    Node node;
    int dis;

    Temp(Node n, int d) {
        this.node = n;
        this.dis = d;
    }

}

class HK {
    public static void topView(Node root) {

        if (root == null)
            return;

        Queue<Temp> q = new LinkedList<>();
        Map<Integer, Integer> h = new TreeMap<>();

        q.add(new Temp(root, 0));

        while (!q.isEmpty()) {
            Temp obj = q.remove();

            Node a = obj.node;
            int distance = obj.dis;

            if (!h.containsKey(distance))
                h.put(distance, a.data);

            if (a.left != null)
                q.add(new Temp(a.left, distance - 1));

            if (a.right != null)
                q.add(new Temp(a.right, distance + 1));

        }

        for (Map.Entry<Integer, Integer> m : h.entrySet()) {
            System.out.print(m.getValue() + " ");
        }

    }
}

class Temp {
    TreeNode node;
    int dis;

    Temp(TreeNode n, int d) {
        this.node = n;
        this.dis = d;
    }

}

class GfG {
    public void printTopView(TreeNode root) {

        if (root == null)
            return;

        Queue<Temp> q = new LinkedList<>();
        Map<Integer, Integer> h = new HashMap<>();

        q.add(new Temp(root, 0));

        while (!q.isEmpty()) {
            Temp obj = q.remove();

            TreeNode a = obj.node;
            int distance = obj.dis;

            if (!h.containsKey(distance)) {
                h.put(distance, a.key);
                System.out.print(a.key + " ");
            }

            if (a.left != null)
                q.add(new Temp(a.left, distance - 1));

            if (a.right != null)
                q.add(new Temp(a.right, distance + 1));

        }

        // for (Map.Entry<Integer, Integer> m : h.entrySet()) {
        // System.out.print(m.getValue()+" ");
        // }

    }

}
