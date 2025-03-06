public class IdGeneratedAccount {
  private static final int INITIAL_VALUE = 10;

  private final String accountNumber;
  private final String accountOwner;
  private double balance;

  private static int currentId;

  static {
    System.out.println("Inicializando currentId");
    currentId = INITIAL_VALUE;
  }

  public IdGeneratedAccount (String accountOwner) {
    this.accountNumber = "000" + currentId++;
    this.accountOwner = accountOwner;
    this.balance = 0;
  }

  boolean deposit (double amount) {
    if (amount > 0) {
      balance += amount;
      return true;
    }
    return false;
  }

  boolean deposit(String amount) {
    return deposit(Double.parseDouble(amount));
  }

  boolean withdraw(double amount) {
    if (balance >= amount && amount > 0) {
      balance -= amount;
      return true;
    }
    return false;
  }

  void transfer (double amount, IdGeneratedAccount targetAccount) {
    this.withdraw(amount);
    targetAccount.deposit(amount);
  }

  void printBalance () {
    System.out.println("Balance: " + balance);
  }

  public String getAccountNumber () {
    return accountNumber;
  }

  public String getAccountOwner () {
    return accountOwner;
  }

  public void setBalance (double balance) {
    this.balance = balance;
  }

  public double getBalance () {
    return balance;
  }
}
