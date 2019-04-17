# review_sentiment_analysis
Read greek reviews, translate to english and find sentiment analysis (using PatternAnalyzer) using textblob and save them to reviews_sentiment.csv


## Development Guide

    1. Create a virtualenv. virtualenv venv 
    2. Activate venv. source venv/bin/activate
    3. Install the requirements. pip install -r requirements.txt
    4. Run python3 reviews_sentiment.py
    
 
 ## Example results   
![test](https://user-images.githubusercontent.com/22845560/56279754-621e4500-6111-11e9-9e21-bd37fac58c5a.png)

Polarity measures how positive or how negative some text is (-1 negative, 0 neutral, 1 positive)

Subjectivity = how much of an opinion a text is 

After getting reviews you can create a Pie chart diagram 
python3 diagram.py

result
![pie](https://user-images.githubusercontent.com/22845560/56292902-bdabfb00-6130-11e9-90ac-d3204e5f4a5e.png)
