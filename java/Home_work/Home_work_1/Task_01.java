// Задан массив, например, nums = [1,7,3,6,5,6].
// Написать программу, которая найдет индекс i для этого массива такой,
// что сумма элементов с индексами < i равна сумме элементов с индексами > i.

package com.gb;

public final class Task_01 {
    public static void main(String[] args) {

        int[] nums = new int[] {1, 7, 3, 6, 5, 6};

        int leftSum, rightSum;
        int index = 0;

        for (int i = 1; i < nums.length - 1; i++){
            leftSum = 0;
            rightSum = 0;

            for (int j = 0; j < i; j++){
                leftSum = leftSum + nums[j];
            }

            for (int k = i + 1; k < nums.length; k++){
                rightSum = rightSum + nums[k];
            }

            if (leftSum == rightSum) {
                index = i;
            }
        }

        if (index == 0) {
            System.out.println("Индекс не найден");
        }
        else {
            System.out.println("Значение индекса: " + index);
        }
    }
}