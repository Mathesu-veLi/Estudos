package dao.impl;

import dao.DepartmentDao;
import db.DB;
import db.DbException;
import entities.Department;

import java.sql.*;
import java.util.List;

public class DepartmentDaoImpl implements DepartmentDao {
  private Connection conn;

  public DepartmentDaoImpl (Connection conn) {
    this.conn = conn;
  }

  @Override
  public void insert (Department obj) {
    PreparedStatement st = null;
    try {
      st = conn.prepareStatement("INSERT INTO department (Name) VALUES (?)");
      st.setString(1, obj.getName());

      int rowsAffected = st.executeUpdate();
      if (rowsAffected > 0) {
        ResultSet rs = st.getGeneratedKeys();
        if (rs.next()) {
          int id = rs.getInt(1);
          obj.setId(id);
        }
        DB.closeResultSet(rs);
      } else {
        throw new DbException("Unexpected error! No rows affected!");
      }
    } catch (SQLException e) {
      throw new DbException(e.getMessage());
    } finally {
      DB.closeStatement(st);
    }
  }

  @Override
  public void update (Department obj) {

  }

  @Override
  public void deleteById (Integer id) {

  }

  @Override
  public Department findById (Integer id) {
    return null;
  }

  @Override
  public List<Department> findAll () {
    return List.of();
  }
}