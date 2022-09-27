// Написать реализацию очереди на основе массива;
// Реализовать методы size(), empty(), offer(), poll(), peek()

package com.gb;

import com.gb.queue;

public class Task_02 {
    public static void main(String[] args) {

        Queue<String> queue = new Queue<>(5);

        queue.offer("1");
        queue.offer("second");
        queue.offer("third");

        System.out.println("Первый элемент очереди " + queue.peek());
        queue.poll();
        System.out.println("Первый элемент очереди " + queue.peek());

        System.out.println("Размер очереди " + queue.size());

        queue.poll();
        queue.poll();

        if (queue.isEmpty()) {
            System.out.println("Очередь пуста");
        } else {
            System.out.println("Очередь не пуста");
        }
    }
}