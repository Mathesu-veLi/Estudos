package services;

import entities.Contract;
import entities.Instalment;

import java.time.LocalDate;

public class ContractService {
  private final OnlinePaymentService onlinePaymentService;

  public ContractService (OnlinePaymentService onlinePaymentService) {
    this.onlinePaymentService = onlinePaymentService;
  }

  public void processContract(Contract contract, int months) {
    double basicQuota = contract.getTotalValue() / months;

    for (int i = 0; i < months; i++) {
      LocalDate dueDate = contract.getDate().plusMonths(i);

      double interest = onlinePaymentService.interest(basicQuota, i);
      double fee = onlinePaymentService.paymentFee(basicQuota + interest);
      double quota = basicQuota + interest + fee;

      contract.getInstallments().add(new Instalment(dueDate, quota));
    }
  }
}
