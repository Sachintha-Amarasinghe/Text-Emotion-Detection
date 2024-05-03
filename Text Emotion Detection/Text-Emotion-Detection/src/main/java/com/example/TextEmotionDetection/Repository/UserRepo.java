package com.example.TextEmotionDetection.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.TextEmotionDetection.Model.User;





public interface UserRepo extends JpaRepository<User, Long>{
	
	public User findByEmail(String email);

}
