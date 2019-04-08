package com.bbi.sentiment_analysis;

import com.bbi.sentiment_analysis.Controller.SentController;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SentimentAnalysisApplication {

    public static void main(String[] args) {
        SentController sc = new SentController();
        String path = sc.get_tweet_keyword_path("messi");
        sc.sentiment_file(path);
    }
}
