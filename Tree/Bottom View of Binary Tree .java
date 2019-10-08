class GfG {
    // Should print bottom view of tree with given root
    public void bottomView(Node root) {
        // Your code here

        if (root == null)
            return;

        Queue<Node> q = new LinkedList<Node>();
        Map<Integer, Integer> h = new TreeMap<>();

        int distance = 0;
        root.hd = distance;
        q.add(root);

        while (!q.isEmpty()) {
            Node a = q.remove();
            distance = a.hd;

            h.put(distance, a.data);

            if (a.left != null) {
                a.left.hd = distance - 1;
                q.add(a.left);
            }

            if (a.right != null) {
                a.right.hd = distance + 1;
                q.add(a.right);
            }

        }

        for (Map.Entry<Integer, Integer> m : h.entrySet()) {
            System.out.print(m.getValue() + " ");
        }

    }
}