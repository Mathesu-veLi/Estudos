import dao.DaoFactory;
import dao.SellerDao;
import entities.Seller;

import java.util.List;

public class Main {
  public static void main (String[] args) {
    SellerDao sellerDao = DaoFactory.createSellerDao();
    List<Seller> list = sellerDao.findAll();

    list.forEach(System.out::println);
  }
}