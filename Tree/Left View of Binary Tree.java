
public class Temp {
    Node node;
    int dis;

    Temp(Node n, int d) {
        this.node = n;
        this.dis = d;
    }

}

class GfG
{
    void leftView(Node root)
    {
      // Your code here
      if (root == null)
            return;

        Queue<Temp> q = new LinkedList<>();
        Map<Integer, Integer> h = new TreeMap<>();

        q.add(new Temp(root, 0));

        while (!q.isEmpty()) {
            Temp obj = q.remove();

            Node a = obj.node;
            int distance = obj.dis;

            if(!h.containsKey(distance))
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

