package app;

import account.AccountService;
import exceptions.ServiceException;

public class App10 {
  public static void main(String[] args) {
    AccountService as = new AccountService();
    try {
      as.createAndWithdraw("1234", 400);
    } catch(ServiceException e) {
      e.printStackTrace();
    }
  }
}
