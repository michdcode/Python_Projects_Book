import json
from argparse import ArgumentParser
from dateutil.parser import *
# import dateutil.ArgumentParser
import numpy as numpy
import pandas as pandas
import matplotlib.pyplot as pyplot
from datetime import datetime

def get_parser():
	parser = ArgumentParser()
	parser.add_argument('--file',
						'-f',
						required=True,
						help='The .json file with all the posts')
	return parser


if __name__ == '__main__':
	parser = get_parser()
	args = parser.parse_args()
	with open(args.file) as f:
		posts = []
		for line in f:
			post = json.loads(line)
			created_time = dateutil.parser.parse(post['created_time'])
			posts.append(created_time.strftime('%H:%M:%S'))
		ones = np.ones(len(posts))
		idx = pd.DatetimeIndex(posts)
		my_series = pd.Series(ones, index=idx)

		per_hour = my_series.resample('1H', how='sum').fillna(0)

		fig, ax = plt.subplots()
		ax.grid(True)
		ax.set_title("Post Frequency")
		width = 0.8
		ind = np.arange(len(per_hour))
		plt.bar(ind, per_hour)
		tick_pos = ind + width /2
		labels = []
		for i in range(24):
			d = datetime.now().replace(hour=i, minute = 0)
			labels.append(d.strftime('%H:%M'))
		plt.xticks(tick_pos, labels, rotation=90)
		plt.savefig('posts_by_hour.png')
