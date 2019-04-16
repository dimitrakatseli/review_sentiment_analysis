from textblob import TextBlob
import csv


filename = "mobile_phones_review.csv"
file_sentiment = "reviews_sentiment.csv"
f = open(file_sentiment,"w")

headers = "title\tstar\treview\ttranslate\tpolarity\tsubjectivity"
f.write(headers +"\n")

with open(filename,'r') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter='\t')
		    
	for row in csv_reader:

		review_gr = row['review']
		title = row['title']
		star = row['star']
		analysis = TextBlob(review_gr)
		review_en = analysis.translate(from_lang="el", to='en')
		print(review_en)
		print(review_en.sentiment)
		f.write("\t".join([title, star, review_gr, str(review_en), str(review_en.sentiment.polarity), str(review_en.sentiment.subjectivity) + "\n"]))


f.close()
csv_file.close()