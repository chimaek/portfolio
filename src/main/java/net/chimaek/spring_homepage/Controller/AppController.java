package net.chimaek.spring_homepage.Controller;

import java.io.IOException;
import net.chimaek.spring_homepage.service.AppService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@Controller
public class AppController {
  private final AppService appService;
//  private final JavaMailSender mailSender;

  @Autowired
  public AppController(AppService appService) {
    this.appService = appService;
  }
  @GetMapping("/")
  public String getHello(Model model) throws IOException {
    String visitorCount = appService.incrementVisitCount();
    model.addAttribute("visitorCount", visitorCount);
    return "index";
  }

  @GetMapping("/portfolio-{id}")
  public String getPortfolio(@PathVariable int id) {
    return "portfolio-" + id;
  }

//  @PostMapping("/send-message")
//  public String sendMessage(@ModelAttribute MessageDto messageDto) {
//    // 이메일 전송 로직
//    return "redirect:/#home";
//  }


}