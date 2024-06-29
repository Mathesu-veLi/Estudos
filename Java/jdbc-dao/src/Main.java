import dao.DaoFactory;
import dao.SellerDao;
import entities.Department;
import entities.Seller;

import java.util.List;

public class Main {
  public static void main (String[] args) {
    SellerDao sellerDao = DaoFactory.createSellerDao();
    Department dep = new Department(2, "Electronics");
    List<Seller> list = sellerDao.findByDepartment(dep);

    list.forEach(System.out::println);
  }
}