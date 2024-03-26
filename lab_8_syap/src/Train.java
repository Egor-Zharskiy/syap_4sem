

public class Train {
    public String destination;
    public int trainNumber;
    public String departureTime;

    public Train(String destination, int trainNumber, String departureTime) {
        this.destination = destination;
        this.trainNumber = trainNumber;
        this.departureTime = departureTime;
    }

    public int getTrainNumber() {
        return trainNumber;
    }

    @Override
    public String toString() {
        return "Train{" + "destination='" + destination + '\'' + ", trainNumber=" + trainNumber + ", departureTime='" + departureTime + '\'' + '}';
    }

    public String getDestination() {
        return destination;
    }

    public String getDepartureTime() {
        return departureTime;
    }
}
