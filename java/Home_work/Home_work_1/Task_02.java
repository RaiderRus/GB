// Напишите функцию, для поиска наиболее длинного общего префикса, среди массива строк.
// Если общего префикса нет, то возвращать пустую строку. Пример ["aabb", "aabbb", "aaabb"] - ответ "aa"

package main.java.com.gb;

public class Task_02 {
    public static void main(String[] args) {

        String[] strings = new String[] {"aabb", "aabbb", "aaabb"};

        StringBuilder prefix = new StringBuilder();
        int min_length = strings[0].length();
        boolean check = true;

        for (int i = 0; i < strings.length; i++){
            if (strings[i].length() < min_length) {
                min_length = strings[i].length();
            }
        }

        for (int i = 0; i < min_length; i++) {
            for (int j = 0; j < strings.length; j++) {
                if (strings[0].charAt(i) != strings[j].charAt(i)) {
                    check = false;
                }
            }
            if (check == true) {
                prefix.append(strings[0].charAt(i));
            }
        }

        System.out.println("Общий префикс: " + prefix);
    }
}