import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Train[] trains = new Train[5];
        trains[0] = new Train("City1", 102, "10:00");
        trains[1] = new Train("City2", 201, "12:30");
        trains[2] = new Train("City1", 105, "14:45");
        trains[3] = new Train("City3", 304, "16:15");
        trains[4] = new Train("City2", 209, "18:00");

        Arrays.sort(trains, Comparator.comparingInt(Train::getTrainNumber));

        System.out.println("Поезда после сортировки по номерам:");
        for (Train train : trains) {
            System.out.println(train);
        }

        Arrays.sort(trains, Comparator
                .comparing(Train::getDestination)
                .thenComparing(Train::getDepartureTime));

        System.out.println("\nПоезда после сортировки по пункту назначения и времени отправления:");
        for (Train train : trains) {
            System.out.println(train);
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("\nВведите номер поезда для получения информации: ");
        int userTrainNumber = scanner.nextInt();

        boolean found = false;
        for (Train train : trains) {
            if (train.getTrainNumber() == userTrainNumber) {
                System.out.println("Информация о выбранном поезде: " + train);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Поезд с номером " + userTrainNumber + " не найден.");
        }
    }
}
