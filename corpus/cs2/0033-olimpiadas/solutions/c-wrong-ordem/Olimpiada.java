import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    static class Country {
        int index;
        int medals;

        public Country(int index, int medals) {
            this.index = index;
            this.medals = medals;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        Country[] countries = new Country[n];
        for (int i = 0; i < n; i++) {
            countries[i] = new Country(i, 0);
        }

        for (int i = 0; i < m; i++) {
            int o = scanner.nextInt() - 1;
            int p = scanner.nextInt() - 1;
            int b = scanner.nextInt() - 1;
            countries[o].medals++;
            countries[p].medals++;
            countries[b].medals++;
        }

        Arrays.sort(countries, new Comparator<Country>() {
            @Override
            public int compare(Country c1, Country c2) {
                if (c1.medals > c2.medals) {
                    return -1;
                } else if (c1.medals < c2.medals) {
                    return 1;
                } else {
                    return Integer.compare(c1.index, c2.index);
                }
            }
        });

        for (int i = 0; i < n; i++) {
            System.out.print((countries[i].index + 1) + " ");
        }
        System.out.println();
    }
}