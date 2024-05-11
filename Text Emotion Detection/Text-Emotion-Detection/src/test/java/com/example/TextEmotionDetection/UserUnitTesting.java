package com.example.TextEmotionDetection;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.util.List;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.example.TextEmotionDetection.Model.User;
import com.example.TextEmotionDetection.Repository.UserRepo;






@SpringBootTest
public class UserUnitTesting {
	@Autowired
	UserRepo usersRepository;

	@Test
	public void testSaveUsers() {
		User users = new User();
		users.setId(2L);
		users.setName("Test");
		users.setEmail("Test@gmail.com");
		users.setMobile("07015245");
		users.setPassword("12345");
		users.setRole("ROLE_USER");
		usersRepository.save(users);
		assertNotNull(usersRepository.findById(2L).get());
	}

	@Test
	public void testReadAll() {
		List<User> list = usersRepository.findAll();
		assertThat(list).size().isGreaterThan(0);
	}


	@Test
	public void testUpdateUser() {
		User users = usersRepository.findById(1L).get();
		users.setName("Test");
		usersRepository.save(users);
		assertNotEquals("Test", usersRepository.findById(1L).get().getName());
	}

	@Test
	public void testDelete() {
		usersRepository.deleteById(2L);
		assertThat(usersRepository.existsById(2L)).isFalse();
	}
}
