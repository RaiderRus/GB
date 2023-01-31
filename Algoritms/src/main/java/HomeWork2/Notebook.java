package HomeWork2;

import java.util.Random;

public class Notebook implements Comparable<Notebook> {

    enum Brand {
        LENUVO("Lenuvo"),
        ASOS("Asos"),
        MACNOTE("MacNote"),
        ESER("Eser"),
        XAMIOU("Xamiou");

        private String title;

        Brand(String title) {
            this.title = title;
        }

        public String getTitle() {
            return this.title;
        }

        @Override
        public String toString() {
            return this.title;
        }
    }

    private static double[] PRICE_VALUES = {100, 200, 300, 400, 500, 600, 700, 800};
    private static int[] RAM_VALUES = {4, 8, 16, 20, 24, 28, 32};
    private static Brand[] BRAND_VALUES = Brand.values();

    private double price;
    private int ram;
    private Brand brand;


    public Notebook() {
        Random rnd = new Random();
        price = PRICE_VALUES[rnd.nextInt(PRICE_VALUES.length)];
        ram = RAM_VALUES[rnd.nextInt(RAM_VALUES.length)];
        brand = BRAND_VALUES[rnd.nextInt(BRAND_VALUES.length)];
    }

    @Override
    public String toString() {
        return "Notebook{"
                + "price=" + price
                + " ram=" + ram
                + " brand=" + brand
                + '}';
    }

    @Override
    public int compareTo(Notebook o) {
        int compare = Double.compare(this.price, o.price);
        if (compare != 0)
            return compare;
        compare = Integer.compare(this.ram, o.ram);
        if (compare != 0)
            return compare;
        return Integer.compare(this.brand.ordinal(), o.brand.ordinal());
    }

    public static Notebook[] notebooksManufacturing(int count) {
        Notebook[] notebooks = new Notebook[count];
        for (int i = 0; i < notebooks.length; i++) {
            notebooks[i] = new Notebook();
        }
        return notebooks;
    }
}
