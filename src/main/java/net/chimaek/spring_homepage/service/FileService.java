package net.chimaek.spring_homepage.service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import org.springframework.stereotype.Service;

@Service
public class FileService {
  private static final String FILE_PATH = "src/main/resources/static/document/visit_count.txt";

  public String getVisitCount() throws IOException {
    // 파일에서 방문자 수 읽기 로직
    return Files.readString(Path.of(FILE_PATH));
  }

  public String incrementVisitCount() throws IOException {
    int count = Integer.parseInt(getVisitCount()) + 1;
    Files.writeString(Path.of(FILE_PATH), String.valueOf(count));
    return String.valueOf(count);
  }
}