
// Bellman Ford's Algorithm:

import java.util.*;

class BFA {
	public static void main(String[] args) {

		int a = 1, b = 2, c = 3, d = 4, s = 0;
		int[][] edges = { { a, b, 5 }, { a, c, 8 }, { a, d, -4 }, { b, a, -2 }, { c, b, -3 }, { c, d, 9 }, { d, s, 2 },
				{ d, b, 7 }, { s, a, 6 }, { s, c, 7 } };
		int v = 5;

		int[] distance = new int[5];
		for (int i = 0; i < distance.length; i++)
			distance[i] = 9999999;
		distance[0] = 0;

		for (int j = 0; j < v; j++)
			for (int i = 0; i < edges.length; i++)
				if ((distance[edges[i][0]] + edges[i][2]) < distance[edges[i][1]])
					distance[edges[i][1]] = distance[edges[i][0]] + edges[i][2];

		for (int i = 0; i < v; i++)
			System.out.print(distance[i] + " ");

	}
}