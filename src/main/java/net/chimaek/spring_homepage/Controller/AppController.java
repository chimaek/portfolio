package net.chimaek.spring_homepage.Controller;

import net.chimaek.spring_homepage.service.AppService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AppController {
  private final AppService appService;
  private final JavaMailSender mailSender;

  @Autowired
  public AppController(AppService appService, JavaMailSender mailSender) {
    this.appService = appService;
    this.mailSender = mailSender;
  }
  @GetMapping("/")
  public String getHello(Model model) {
    String visitorCount = appService.incrementVisitCount();
    model.addAttribute("visitorCount", visitorCount);
    return "index";
  }

  @GetMapping("/portfolio-{id}")
  public String getPortfolio(@PathVariable int id) {
    return "portfolio-" + id;
  }

  @PostMapping("/send-message")
  public String sendMessage(@ModelAttribute MessageDto messageDto) {
    // 이메일 전송 로직
    return "redirect:/#home";
  }


}