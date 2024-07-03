package com.veli.workshopmongo.services;

import com.veli.workshopmongo.domain.User;
import com.veli.workshopmongo.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

public class UserService {
  @Autowired
  private UserRepository repo;

  public List<User> findAll () {
    return repo.findAll();
  }
}
