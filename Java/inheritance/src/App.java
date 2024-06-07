import entities.Account;
import entities.BusinessAccount;

public class App {
    public static void main(String[] args) throws Exception {
        Account acc = new Account(1001, "Alex", 0.0);
        BusinessAccount bacc = new BusinessAccount(1002, "Maria", 0.0, 500.0);

        // Upcasting
        Account acc1 = bacc;
        Account acc2 = new BusinessAccount(1003, "Bob", 0.0, 200.0);
        Account acc3 = new BusinessAccount(1004, "Anna", 0.0, 0.01);
        
        
    }
}
