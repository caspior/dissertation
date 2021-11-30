# Evaluation of E-Scooter Media Coverage

### Abstract
In this chapter, I examined the positions reporters take on shared e-scooters in mass media and illustrated temporal and geographical trends in news coverage across the USA. Ever since the introduction of e-scooters in September 2017, news articles voiced their criticism and support for e-scooters, alongside simply reporting about the new phenomena. I examined three years of news articles from 10 large metropolitans and national newspapers. I used sentiment analysis to determine each article's stand toward e-scooter
sharing – positive or negative – and mapped the common themes the articles discussed. My findings show that mass media was not overwhelmingly supportive of or against e-scooters. Negative coverage grew with time but lessened in the early months of 2020. News articles discussed e-scooter regulation, safety issues, and the conflict with other road users more than any other topics. In conclusion, my study shows that mass media developed to accept and normalize the operation of e-scooters with time.

### Data

I retrieved 840 e-scooter related articles published in news websites and known blogs in 10 US metropolitan areas and national publications between September 2017 and August 2020. To reach those articles I used Google news search with the key words "scooters" and "scooters CITY NAME". [This table](News_articles.pdf) lists all the articles I cited and [this table](News_articles.MD) summarizes it.
Due to the large variaty of data sources in this study I preffered manually coding the data into this [CSV spreadsheet](News_data.csv).

### Sentiment Analysis

The first analytical step of this chapter is a sentiment analysis. I used three ready-to-use unigram sentiment dictionaries to determine the overall sentiment of the articles. I used this [R markdown](News_sentiment.Rmd) and generated this [markdown output](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/News_sentiment.html).

### Word Count Analysis

The second nalytical step of this chapter is a word count analysis. After cleaning and steming the text I counted to appearance of the 20 words that can tell about the content of the paper. I included words like 'sidewalk' and 'regulation' but excluded words such as 'city' and 'scooter'. I used this [R markdown](News_count.Rmd) and generated this [markdown output](https://htmlpreview.github.io/?https://github.com/caspior/dissertation/blob/main/News_count.html).
