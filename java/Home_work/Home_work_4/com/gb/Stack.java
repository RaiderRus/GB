package com.gb;

public class Stack<T> {
    private T[] array;
    private int top;
    private final int MAX_SIZE;

    public Stack(int size) {
        this.array = (T[]) new Object[size];
        this.top = -1;
        this.MAX_SIZE = size;
    }

    public int size() {
        return this.top + 1;
    }

    public boolean isEmpty() {
        return this.top == -1;
    }

    public boolean isFull() {
        return this.top == this.MAX_SIZE - 1;
    }

    public void push(T item) {
        if (this.isFull()) {
            System.out.println("Переполнение стека. Завершение работы!\n");
            System.exit(-1);
        } else {
            this.array[++this.top] = item;
        }
    }

    public T peek() {
        if (this.isEmpty()) {
            System.out.println("Стек пуст. Завершение работы!\n");
            System.exit(-1);
        }
        return this.array[this.top];
    }

    public T pop() {
        if (this.isEmpty()) {
            System.out.println("Извлечение данных из пустого стека. Завершение работы!\n");
            System.exit(-1);
        }
        System.out.println("Удаление элемента: " + this.peek());
        return this.array[this.top--];
    }
}