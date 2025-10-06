import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

public class LocalTimeApp {
    public static void main(String[] args) {
        LocalTime time1 = LocalTime.of(23,10,15);
        System.out.println(time1);

        LocalTime time2 = LocalTime.now();
        System.out.println(time2);

        LocalTime time3 = LocalTime.now().withSecond(0).withNano(0);
        System.out.println(time3);

        LocalTime time4 = LocalTime.parse("00:00:00");
        System.out.println(time4);

        LocalTime time5 = LocalTime.parse("13-30-20", DateTimeFormatter.ofPattern("HH-mm-ss"));
        System.out.println(time5);
    }
}
