// Реализовать метод contains в классе Tree

package HomeWork4;

import java.util.Objects;

public class Tree<T extends Comparable<T>> {

    public static void main(String[] args) {
        int[] values = {15, 8, 1, 5, 10, 20, 35, 30, 21, 3, 21, 40};
        Tree<Integer> tree = new Tree<Integer>();
        for (int value : values) {
            tree.add(value);
        }
        int[] checkValues = { 8, 17, 1, 5, 35, 14, 3, 21, 33, 40};
        for (int value : checkValues) {
            System.out.printf("%d %s contained in tree\n", value, tree.contains(value)?"":"not");
        }
        System.out.println();
    }

    private Node root;

    private class Node {
        private T value;
        private Node left;
        private Node right;

        public Node(T value) {
            this.value = value;
        }

        @Override
        public String toString() {
            return value.toString();
        }
    }

    public void add(T value) {
        Objects.requireNonNull(value);
        root = appendNode(root, value);
    }

    private Node appendNode(Node current, T value) {
        if (current == null) {
            return new Node(value);
        }

        int compare = value.compareTo(current.value);
        if (compare < 0) {
            current.left = appendNode(current.left, value);
        } else if (compare > 0) {
            current.right = appendNode(current.right, value);
        }

        return current;
    }

    public boolean contains(T value) {
        Objects.requireNonNull(value);
        return containsRecursive(root, value);
    }

    private boolean containsRecursive(Node current, T value) {
        if (current == null)
            return false;
        if (value.compareTo(current.value) == 0)
            return true;
        if(value.compareTo(current.value) < 0)
            return containsRecursive(current.left, value);
        return containsRecursive(current.right, value);
    }

}