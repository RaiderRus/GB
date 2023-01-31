// Класс Notebook содержит поля:
// Стоимость - price, double [100, 200, 300, 400, 500, 600, 700, 800]
// Оперативная память - ram, integer [4, 8, 16, 20, 24, 28, 32]
// Производитель - brand, enum Перечисление Brand может принимать следующие значения: Lenuvo, Asos, MacNote, Eser, Xamiou.
// Сортировать нужно в этом же порядке (т.е. Lenuvo имеет наивысший приоритет).
// Отсортировать по стоимости, по памяти, по перечислению (в таком порядке)

package HomeWork2;

import java.util.Arrays;

public class Program {
    public static void main(String[] args) {
        Integer[] array = {5,6,4,9,0,2,8,7,1,3};
        Sorter.heapSort(array);
        System.out.println(Arrays.toString(array));

        Notebook[] notebooks = Notebook.notebooksManufacturing(100);
        printArray(notebooks);
        Sorter.heapSort(notebooks);
        System.out.println("\n---------------- Sordet array ------------------------");
        printArray(notebooks);
    }

    static public void printArray(Notebook[] array) {
        for (Notebook nout : array) {
            System.out.println(nout);
        }
    }
}
