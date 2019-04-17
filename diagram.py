import matplotlib.pyplot as plt
import csv



#create object for diagram
class Avg_Obj:
	def __init__(self, negative, positive, neutral, all_sum):
		self.negative = negative
		self.positive = positive
		self.neutral = neutral
		self.all_sum = all_sum

avg_obj = Avg_Obj(0,0,0,0)
print(avg_obj.all_sum)
filename = "reviews_sentiment.csv"

def average(avg_obj,sentiment):

	if sentiment<0:
		avg_obj.negative = avg_obj.negative + 1
	elif sentiment>0:
		avg_obj.positive = avg_obj.positive +1
	elif sentiment ==0:
		avg_obj.neutral = avg_obj.neutral +1

	avg_obj.all_sum = avg_obj.all_sum + 1
	return avg_obj

def create_diagram(avg_obj):

	labels = ['Negative', 'Positive', 'Neutral']
	sizes = [avg_obj.negative/avg_obj.all_sum *100, avg_obj.positive/avg_obj.all_sum *100,avg_obj.neutral/avg_obj.all_sum *100]
	colors = ['red', 'green', 'yellow']
	explode = (0.1, 0, 0)  # explode 1st slice
	 
	# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	autopct='%1.1f%%', shadow=True, startangle=140)
	 
	plt.axis('equal')
	plt.show()


with open(filename,'r') as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter='\t')
		    
	for row in csv_reader:

		sentiment = row['polarity']
		print(sentiment)
		avg_obj = average(avg_obj,float(sentiment))
		print(avg_obj.all_sum)
		print(avg_obj.negative)
		print(avg_obj.positive)
csv_file.close()
create_diagram(avg_obj)








