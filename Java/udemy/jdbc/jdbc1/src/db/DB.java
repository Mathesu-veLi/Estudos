package db;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;

public class DB {
  private static Connection conn = null;

  public static Connection getConn () {
    if (conn == null) {
      try {
        Properties props = loadProperties();
        String url = props.getProperty("dburl");
        conn = DriverManager.getConnection(url, props);
      } catch (SQLException e) {
        throw new DbException(e.getMessage());
      }
    }
    return conn;
  }

  private static Properties loadProperties () {
    try (FileInputStream fs = new FileInputStream("db.properties")) {
      Properties props = new Properties();
      props.load(fs);
      return props;
    } catch (IOException e) {
      throw new DbException(e.getMessage());
    }
  }

  public static void closeConnection () {
    try {
      if (conn != null) {
        conn.close();
      }
    } catch (SQLException e) {
      throw new DbException(e.getMessage());
    }
  }
}