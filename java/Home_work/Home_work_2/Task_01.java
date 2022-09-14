// Напишите метод, который определит тип (расширение) файлов из текущей папки и выведет в консоль результат вида.


import java.io.*;

public class Task_01 {
    public static void main(String[] args) {
        String targetStr = ".";
        String tempStr="";
        String currPathname = System.getProperty("user.dir");
        File currDir = new File (currPathname);
        File[] files = currDir.listFiles();
        String [] extensions = new String[files.length];
        System.out.println("В текущей папке существуют файлы со следующими расширениями: ");
        for(int i=0; i<files.length; i++){
            tempStr=files[i].toString();
            extensions[i]=tempStr.substring(tempStr.indexOf(targetStr));
            System.out.println(i+1 +". "+ "Расширение файла:"+ "'"+extensions[i]+"'");
        }
    }
}