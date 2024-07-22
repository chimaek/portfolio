package net.chimaek.spring_homepage.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AppService {
    private final FileService fileService;

    @Autowired
    public AppService(FileService fileService) {
        this.fileService = fileService;
    }

    public String getHello() {
        return "Hello World!";
    }

    public String incrementVisitCount() {
        return fileService.incrementVisitCount();
    }
}