import db.DB;
import db.DbException;

import java.sql.*;

public class Main {
  public static void main (String[] args) {
    Connection conn = null;
    Statement st = null;
    ResultSet rs = null;

    try {
      conn = DB.getConn();
      st = conn.createStatement();
      rs = st.executeQuery("SELECT * FROM department");

      while (rs.next()) {
        System.out.printf("%d, %s%n", rs.getInt("Id"), rs.getString("Name"));
      }
    } catch (SQLException e) {
      throw new DbException(e.getMessage());
    } finally {
      DB.closeResultSet(rs);
      DB.closeStatement(st);
      DB.closeConnection();
    }
  }
}