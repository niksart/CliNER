import os
import os.path
import sys
import glob
import argparse
import helper

from model import Model
from note import *

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", 
		dest = "input", 
		help = "The input files to predict", 
		default = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/test_data/*')
	)

	parser.add_argument("-o", 
		dest = "output", 
		help = "The directory to write the output", 
		default = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/test_predictions')
	)

	parser.add_argument("-m",
		dest = "model",
		help = "The model to use for prediction",
		default = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../model/awesome.model')
	)

	
	args = parser.parse_args()

	# Locate the test files
	files = glob.glob(args.input)

	# Load a model and make a prediction for each file
	path = args.output
	helper.mkpath(args.output)

	model = Model(filename = args.model)
	for txt in files:
		data = read_txt(txt)
		labels = model.predict(data)
		con = txt.split(os.sep)[-1]
		con = os.path.join(path, con[:-3] + 'con')
		write_con(con, data, labels)

if __name__ == '__main__':
	main()