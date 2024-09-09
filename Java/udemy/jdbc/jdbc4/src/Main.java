import db.DB;

import java.sql.*;

public class Main {
  public static void main (String[] args) {
    Connection conn = null;
    PreparedStatement st = null;
    try {
      conn = DB.getConn();
      st = conn.prepareStatement("UPDATE seller SET BaseSalary = BaseSalary + ? WHERE (DepartmentId = ?)");
      st.setDouble(1, 200.0);
      st.setInt(2, 2);

      int rowsAffected = st.executeUpdate();
      System.out.println("Done! Rows affected: " + rowsAffected);
    } catch (SQLException e) {
      e.printStackTrace();
    }
  }
}