#this is header
from giveUJson.searchrobot import *
# from const import *
import json

def strFinder(strr,filename = 'data.json'):
	return dumper(strr,filename)

class book(object):
	def __init__(self):
		self.data = {'biology':[12345,2345],'testdata':[33],'Hello world':[1]}
	def get_data(self,strr):
		if self.data.__contains__(strr) == False:
			return "Sorry, can't find this world in textbook"
		else:
			return self.data[strr]

class jasoner(object):
	def __init__(self):
		self.outputer = []
		self.book = book()
		# Change the data.json location
	# def callable(self,strr,filename = '../data.json'):
	# 	worker = {}
	# 	worker['Int'] =  get_search_result(strr)
	# 	worker['Dic'] = self.book.get_data(strr)
	# 	print(worker['Dic'])
	# 	with open(filename, 'w') as outfile:
	# 		self.outputer.append(worker)
	# 		json.dump(self.outputer, outfile)
	def callable(self,strr,filename = '../data.json'):
		worker = {}
		tmp = get_search_result(strr)

		worker['Int'] = {}
		worker['Int']['name'] = strr
		worker['Int']['description'] = tmp[strr]["description"]
		worker['Int']['url'] = tmp[strr]['url']

		worker['Dic'] = self.book.get_data(strr)
		print(worker['Dic'])
		with open(filename, 'w') as outfile:
			self.outputer.append(worker)
			json.dump(self.outputer, outfile)
		return self.outputer
	def return_json(self):
		return self.outputer

if __name__ == "__main__":
	print("tester")
	ja = jasoner()
	ja.callable("testdat")
	# P = {}get_search_result("HI")
	# print(P)
