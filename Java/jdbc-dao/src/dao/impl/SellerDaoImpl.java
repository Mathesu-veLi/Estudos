package dao.impl;

import dao.SellerDao;
import db.DB;
import db.DbException;
import entities.Department;
import entities.Seller;

import java.sql.*;
import java.util.*;

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
    PreparedStatement st = null;
    ResultSet rs = null;

    try {
      st = conn.prepareStatement("SELECT seller.*,department.Name as DepName FROM seller INNER JOIN department ON seller.DepartmentId = department.Id WHERE seller.Id = ?");
      st.setInt(1, id);
      rs = st.executeQuery();
      if (rs.next()) {
        Department dep = instantiateDepartment(rs);

        Seller obj = instantiateSeller(rs, dep);
        return obj;
      }
      return null;
    } catch (SQLException e) {
      throw new DbException(e.getMessage());
    } finally {
      DB.closeStatement(st);
      DB.closeResultSet(rs);
    }
  }

  private Seller instantiateSeller (ResultSet rs, Department dep) throws SQLException {
    Seller obj = new Seller();
    obj.setId(rs.getInt("Id"));
    obj.setName(rs.getString("Name"));
    obj.setEmail(rs.getString("Email"));
    obj.setBaseSalary(rs.getDouble("BaseSalary"));
    obj.setBirthDate(rs.getDate("BirthDate"));
    obj.setDepartment(dep);
    return obj;
  }

  private Department instantiateDepartment (ResultSet rs) throws SQLException {
    Department dep = new Department();
    dep.setId(rs.getInt("DepartmentId"));
    dep.setName(rs.getString("DepName"));
    return dep;
  }

  @Override
  public List<Seller> findAll () {
    PreparedStatement st = null;
    ResultSet rs = null;

    try {
      st = conn.prepareStatement("SELECT seller.*,department.Name as DepName FROM seller INNER JOIN department ON seller.DepartmentId = department.Id ORDER BY Name");
      rs = st.executeQuery();

      List<Seller> sellers = new ArrayList<>();
      Map<Integer, Department> departments = new HashMap<>();
      while (rs.next()) {
        Department dep = departments.get(rs.getInt("DepartmentId"));
        if (dep == null) {
          dep = instantiateDepartment(rs);
          departments.put(rs.getInt("DepartmentId"), dep);
        }
        Seller obj = instantiateSeller(rs, dep);
        sellers.add(obj);
      }

      return sellers;
    } catch (SQLException e) {
      throw new DbException(e.getMessage());
    } finally {
      DB.closeStatement(st);
      DB.closeResultSet(rs);
    }
  }


  @Override
  public List<Seller> findByDepartment (Department department) {
    PreparedStatement st = null;
    ResultSet rs = null;

    try {
      st = conn.prepareStatement("SELECT seller.*,department.Name as DepName FROM seller INNER JOIN department ON seller.DepartmentId = department.Id WHERE DepartmentId = ? ORDER BY Name");

      st.setInt(1, department.getId());
      rs = st.executeQuery();

      List<Seller> sellers = new ArrayList<>();
      Map<Integer, Department> departments = new HashMap<>();
      while (rs.next()) {
        Department dep = departments.get(rs.getInt("DepartmentId"));
        if (dep == null) {
          dep = instantiateDepartment(rs);
          departments.put(rs.getInt("DepartmentId"), dep);
        }
        Seller obj = instantiateSeller(rs, dep);
        sellers.add(obj);
      }

      return sellers;
    } catch (SQLException e) {
      throw new DbException(e.getMessage());
    } finally {
      DB.closeStatement(st);
      DB.closeResultSet(rs);
    }
  }
}
