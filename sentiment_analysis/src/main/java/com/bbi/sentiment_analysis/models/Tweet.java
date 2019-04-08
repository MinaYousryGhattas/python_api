package com.bbi.sentiment_analysis.models;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Tweet {
    String text;
    String sentiment;

    public Tweet() {
    }

    public Tweet(String text, String sentiment) {
        this.text = text;
        this.sentiment = sentiment;
    }

    public String getText() {

        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getSentiment() {
        return sentiment;
    }

    public void setSentiment(String sentiment) {
        this.sentiment = sentiment;
    }
}
