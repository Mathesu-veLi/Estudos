package api;

public class ExPhoneBook {
    public static void main(String[] args) {
        var p = new PhoneBook();
        /*String phone = p.findByName("pedro").orElseThrow(IllegalArgumentException::new);
        System.out.println(phone);*/

        p.findByName("pedro").ifPresentOrElse(System.out::println, () -> { throw new IllegalArgumentException(); });
    }
}
