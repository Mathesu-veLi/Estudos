package com.veli.spring.services;

import com.veli.spring.entities.User;
import com.veli.spring.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class UserService {
  @Autowired
  private UserRepository repository;

  public List<User> findAll () {
    return repository.findAll();
  }
}
