package com.veli.spring.services;

import com.veli.spring.entities.User;
import com.veli.spring.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
  @Autowired
  private UserRepository repository;

  public List<User> findAll () {
    return repository.findAll();
  }
}
