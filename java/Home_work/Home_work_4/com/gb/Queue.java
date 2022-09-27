package com.gb;

public class Queue <T> {
    private T[] array;
    private int front;
    private int rear;
    private final int MAX_SIZE;
    private int count;

    public Queue (int size) {
        this.array = (T[]) new Object[size];
        this.MAX_SIZE = size;
        this.front = 0;
        this.rear = -1;
        this.count = 0;
    }

    public T poll()
    {
        if (isEmpty())
        {
            System.out.println("Извлечение данных из пустой очереди. Завершение работы!\n");
            System.exit(-1);
        }

        T x = this.array[this.front];

        System.out.println("Удаление элемента: " + x);

        this.front = (this.front + 1) % this.MAX_SIZE;
        this.count--;

        return x;
    }

    public void offer(T item)
    {
        if (this.isFull())
        {
            System.out.println("Переполнение очереди. Завершение работы!\n");
            System.exit(-1);
        }
        this.rear = (this.rear + 1) % this.MAX_SIZE;
        this.array[this.rear] = item;
        this.count++;
    }

    public T peek()
    {
        if (this.isEmpty())
        {
            System.out.println("Очередь пуста. Завершение работы!\n");
            System.exit(-1);
        }
        return this.array[this.front];
    }

    public int size() {
        return this.count;
    }

    public boolean isEmpty() {
        return (this.size() == 0);
    }

    public boolean isFull() {
        return (this.size() == this.MAX_SIZE);
    }
}