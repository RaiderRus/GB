// 1. Реализовать методы addFirst, removeFirst.
// 2. Реализовать методы разворота связного списка.

package HomeWork3;

import java.util.Iterator;

public class List {

    public static void main(String[] args) {
        ListNode listHead = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        System.out.println(listHead);
        listHead = ListNodeUtils.addFirst(listHead, 10);
        System.out.println(listHead);
        listHead = ListNodeUtils.addFirst(listHead, 11);
        System.out.println(listHead);
        listHead = ListNodeUtils.addFirst(listHead, 12);
        System.out.println(listHead);
        listHead = ListNodeUtils.revertList(listHead);
        System.out.println(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        System.out.println(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        System.out.println(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        listHead = ListNodeUtils.removeFirst(listHead);
        System.out.println(listHead);
        listHead = ListNodeUtils.addFirst(listHead, 10);
        listHead = ListNodeUtils.addFirst(listHead, 11);
        listHead = ListNodeUtils.addFirst(listHead, 12);
        System.out.println(listHead);
        System.out.println(new ListNode(111));
    }

    public static class ListNode implements Iterable<Integer> {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }

        @Override
        public Iterator<Integer> iterator() {
            return new ListIterator(this);
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder("[ ");
            sb.append(this.val);
            if(this.next!=null) {
                for (Integer value : this.next) {
                    sb.append(" -> ").append(value);
                }
            }
            sb.append(" ]");
            return sb.toString();
        }
    }

    public static class ListIterator implements Iterator<Integer> {
        private ListNode nextNode;

        public ListIterator(ListNode head) {
            this.nextNode = head;
        }

        @Override
        public boolean hasNext() {
            return nextNode != null;
        }

        @Override
        public Integer next() {
            Integer value = nextNode.val;
            this.nextNode = this.nextNode.next;
            return value;
        }
    }

    public static class ListNodeUtils {

        public static ListNode addFirst(ListNode node, int value) {
            return new ListNode(value, node);
        }

        public static ListNode removeFirst(ListNode node) {
            if (node == null)
                return null;
            return node.next;
        }

        public static ListNode revertList(ListNode node) {
            if(node == null)
                return null;
            return revertList(node, null);
        }

        private static ListNode revertList(ListNode node, ListNode prev) {
            if (node.next != null) {
                ListNode next = node.next;
                node.next = prev;
                return revertList(next, node);
            }
            node.next = prev;
            return node;
        }
    }
}
