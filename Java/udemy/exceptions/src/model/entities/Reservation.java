package model.entities;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

import model.exceptions.DomainException;

public class Reservation {
  private Integer roomNumber;
  private Date checkIn;
  private Date checkOut;

  private static SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
  
  public Reservation() {
  }

  public Reservation(Integer roomNumber, Date checkIn, Date checkOut) throws DomainException {
    if (!checkOut.after(checkIn)) {
      throw new DomainException("Check-out date must be after check-in date");
    }

    this.roomNumber = roomNumber;
    this.checkIn = checkIn;
    this.checkOut = checkOut;
  }

  public Integer getRoomNumber() {
    return roomNumber;
  }

  public void setRoomNumber(Integer roomNumber) {
    this.roomNumber = roomNumber;
  }

  public Date getCheckIn() {
    return checkIn;
  }

  public Date getCheckOut() {
    return checkOut;
  } 

  public long duration() {
    long diff = checkOut.getTime() - checkIn.getTime();
    return TimeUnit.DAYS.convert(diff, TimeUnit.MILLISECONDS);
  }

  public String updateDates(Date checkIn, Date checkOut) throws DomainException {
    Date now = new Date();
    if (checkIn.before(now) || checkOut.before(now)) {
      throw new DomainException("Reservation dates for updates must be future dates");
    } 
    if (!checkOut.after(checkIn)) {
      throw new DomainException("Check-out date must be after check-in date");
    }
    
    this.checkIn = checkIn;
    this.checkOut = checkOut;
    return null;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append(String.format("Room: %d, ", roomNumber));
    sb.append(String.format("check-in: %s, ", sdf.format(checkIn)));
    sb.append(String.format("checkOut: %s, ", sdf.format(checkOut)));
    sb.append(String.format("%s nights.", duration()));
    return sb.toString();
  }
}