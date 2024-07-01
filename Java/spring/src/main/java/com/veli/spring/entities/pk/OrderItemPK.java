package com.veli.spring.entities.pk;

import com.veli.spring.entities.Order;
import com.veli.spring.entities.Product;
import jakarta.persistence.*;

import java.io.Serializable;

@Embeddable
public class OrderItemPK implements Serializable {

  @ManyToOne
  @JoinColumn(name = "order_id")
  private Order order;
  
  @ManyToOne
  @JoinColumn(name = "product_id")
  private Product product;

  public Order getOrder () {
    return order;
  }

  public void setOrder (Order order) {
    this.order = order;
  }

  public Product getProduct () {
    return product;
  }

  public void setProduct (Product product) {
    this.product = product;
  }

  @Override
  public boolean equals (Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;

    OrderItemPK that = (OrderItemPK) o;
    return getOrder().equals(that.getOrder()) && getProduct().equals(that.getProduct());
  }

  @Override
  public int hashCode () {
    int result = getOrder().hashCode();
    result = 31 * result + getProduct().hashCode();
    return result;
  }
}
