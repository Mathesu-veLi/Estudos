package dao;

import dao.impl.DepartmentDaoImpl;
import dao.impl.SellerDaoImpl;
import db.DB;

public class DaoFactory {
  public static SellerDao createSellerDao () {
    return new SellerDaoImpl(DB.getConn());
  }

  public static DepartmentDao createDepartmentDao () {
    return new DepartmentDaoImpl(DB.getConn());
  }
}
