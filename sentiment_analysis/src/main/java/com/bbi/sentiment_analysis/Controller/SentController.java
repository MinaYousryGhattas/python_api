package com.bbi.sentiment_analysis.Controller;
import com.bbi.sentiment_analysis.models.Tweet;
import org.springframework.boot.autoconfigure.web.client.RestTemplateAutoConfiguration;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.boot.web.client.*;

import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import sun.java2d.cmm.Profile;

import java.net.URI;
import java.util.Arrays;
import java.util.List;

@Controller
public class SentController {
    public String get_tweet_keyword_path(String keyword){
        System.out.println("Test");
        RestTemplate restTemplate = new RestTemplate();
        String path = restTemplate.getForObject("http://127.0.0.1:5000/get_tweets/"+keyword, String.class);
        System.out.println(path);
        return path.replace("\\\\","\\");
    }

    public void sentiment_file(String path){
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

        MultiValueMap<String, String> map= new LinkedMultiValueMap<String, String>();
        map.add("path", path);

        HttpEntity<MultiValueMap<String, String>> request = new HttpEntity<MultiValueMap<String, String>>(map, headers);

        RestTemplate restTemplate = new RestTemplate();
        Tweet[] tweets= restTemplate.postForEntity("http://127.0.0.1:5000/analyze", (Object) request, Tweet[].class).getBody();
        for (int i = 0;i < 5; i++){
            System.out.println(tweets[i].getText());
            System.out.println(tweets[i].getSentiment());
        }
    }
}
