
package HomeWork1;

public class Task1 {

    //Рекурсивно найти n-ое число Фибоначчи. Определить сложность. (fn[0] = 0 или 1) [fn(n) = (fn(n - 1) + fn(n - 2)]
    public static int fibonacciRecursion(int n) {
        if (n < 0)
            throw new IllegalArgumentException("n must be positive");

        if (n == 0)
            return 0;
        if (n == 1)
            return 1;

        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2);
    }

    //Найти n-ое число Фибоначчи за O(n).
    public static int fibonacciLinear(int n) {
        if (n < 0)
            throw new IllegalArgumentException("n must be positive");

        if (n == 0)
            return 0;
        if (n == 1)
            return 1;

        int current = 2;
        int fibonnacciMinus1 = 1;
        int fibonacci = 1;
        while (current < n) {
            int temp = fibonnacciMinus1;
            fibonnacciMinus1 = fibonacci;
            fibonacci += temp;
            current++;
        }
        return fibonacci;
    }

    //    Найти сумму элементов главной диагонали в двумерном массиве. Найти сумму элементов побочной диагонали в двумерном массиве
    public static int sumMainDiagonal(int[][] matrix) {
        int size = matrix.length;
        for (int[] line : matrix) {
            if (line.length != size)
                throw new IllegalArgumentException("Matrix must be square");
        }

        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += matrix[i][i];
        }
        return sum;
    }

    public static int sumSecondaryDiagonal(int[][] matrix) {
        int size = matrix.length;
        for (int[] line : matrix) {
            if (line.length != size)
                throw new IllegalArgumentException("Matrix must be square");
        }

        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += matrix[i][size - i - 1];
        }
        return sum;
    }

    //    Реализовать сдвиг элементов в массиве на n влево или вправо.
    public static void shiftArray(int[] array, int n) {
        if (n == 0) {
            return;
        }
        n = n % array.length;
        if (n < 0) {
            n = array.length + n;
        }
        int[] temp = new int[n];
        for (int i = 0; i < n; i++) {
            temp[i] = array[array.length - n + i];
        }
        for (int i = array.length - n - 1; i >= 0; i--) {
            array[i + n] = array[i];
        }
        for (int i = 0; i < n; i++) {
            array[i] = temp[i];
        }
    }
}
