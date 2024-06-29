package dao.impl;

import dao.SellerDao;
import db.DB;
import db.DbException;
import entities.Department;
import entities.Seller;

import java.sql.*;
import java.util.List;

public class SellerDaoImpl implements SellerDao {
  private Connection conn;

  public SellerDaoImpl (Connection conn) {
    this.conn = conn;
  }

  @Override
  public void insert (Seller obj) {

  }

  @Override
  public void update (Seller obj) {

  }

  @Override
  public void deleteById (Integer id) {

  }

  @Override
  public Seller findById (Integer id) {
    return null;
  }

  @Override
  public List<Seller> findAll () {
    return List.of();
  }
}
