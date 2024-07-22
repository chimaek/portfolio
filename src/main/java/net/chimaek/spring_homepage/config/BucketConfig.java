package net.chimaek.spring_homepage.config;

import io.github.bucket4j.Bandwidth;
import io.github.bucket4j.Bucket;
import io.github.bucket4j.Refill;
import java.time.Duration;
import org.springframework.context.annotation.Configuration;

@Configuration
public class BucketConfig {

  public Bucket createBucket() {
    long overdraft = 30;
    Refill refill = Refill.intervally(10, Duration.ofMinutes(1));
    Bandwidth limit = Bandwidth.classic(overdraft, refill);
    return Bucket.builder().addLimit(limit).build();
  }
}