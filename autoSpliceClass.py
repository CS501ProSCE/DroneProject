##	Ashley Dicks ##
##	Automatic Splice UAV flight timeseries data
import math

class AnomalyDetection:
	average = 0.0
	count = 0.0
	previousDataIndex = 0
	inAnomaly = False
	anomalyArray = []
	coolDownIndex = 0
	inCoolDown = False
	
	def __init__(self, data):
		self.data = data
		self.previousDataCount = math.ceil(len(data) * 0.005)
		self.previousData = [0] * self.previousDataCount
		self.anomlyThreashHold, self.average = self.calcStandardDevation(data)
		#print(self.average)
		#print(self.anomlyThreashHold)
		# self.anomlyThreashHold = self.anomlyThreashHold

	def parseDataPoint(self, dataPoint):
		returnVal = None
		if(abs(dataPoint) >= (abs(self.average) + abs(self.anomlyThreashHold)) and not self.inAnomaly and not self.inCoolDown and self.count > self.previousDataCount):
			# start of anonly detected
			# add past data points
			self.anomalyArray = []
			x = 0
			i = self.previousDataIndex
			while x < self.previousDataCount:
				self.anomalyArray.append(self.previousData[i])
				i = (i + 1) % self.previousDataCount
				x += 1
			# add current data point
			self.anomalyArray.append(dataPoint)
			self.inAnomaly = True
		elif(abs(dataPoint) >= (abs(self.average) + abs(self.anomlyThreashHold)) and self.inAnomaly and not self.inCoolDown):
			# inside current anomly, add data point
			self.anomalyArray.append(dataPoint)
		elif(abs(dataPoint) >= (abs(self.average) + abs(self.anomlyThreashHold)) and not self.inAnomaly and self.inCoolDown):
			# If we are in the coolDown phase of self.previousDataCount length and we detect a anomaly, exit cooldown phase and restart anomaly phase 
			self.anomalyArray.append(dataPoint)
			self.inAnomaly = True
			self.inCoolDown = False
			self.coolDownIndex = 0 # ??
		elif(not self.inAnomaly and self.inCoolDown):
			# if we are in coolDown phase and not detect anomaly
			self.anomalyArray.append(dataPoint)
			self.coolDownIndex += 1
			if(self.coolDownIndex > self.previousDataCount):
				returnVal = self.anomalyArray
				self.inAnomaly = False
				self.inCoolDown = False
				self.coolDownIndex = 0
		elif(self.inAnomaly):
			# end of current anomaly. Check next self.previousDataCount data points to see if another anomly starts and if so combine them
			self.anomalyArray.append(dataPoint)
			self.inAnomaly = False
			self.inCoolDown = True

		# add dataPoint to average
		# summ = self.average * self.count
		# summ += abs(dataPoint)
		self.count += 1
		# self.average = summ / self.count
		# add dataPoint to previous DataCircular Buffer
		self.previousData[self.previousDataIndex] = dataPoint
		self.previousDataIndex = (self.previousDataIndex + 1) % self.previousDataCount

		return returnVal

	def parseData(self):
		anomalies = []
		index_x = []
		for data in self.data:
			res = self.parseDataPoint(data)
			if(res != None):
				anomalies.append(res)
				index_x.append(int(self.count - len(res)))
				index_x.append(int(self.count))

		if(len(self.anomalyArray) >= 0):
			anomalies.append(self.anomalyArray)
			index_x.append(int(self.count - len(self.anomalyArray)))
			index_x.append(int(self.count))

		return anomalies, index_x

	def calcStandardDevation(self, dataArray):
		# calc mean
		summ = 0.0
		for data in dataArray:
			summ += data
		mean = summ / len(dataArray)
		# num - mean squared
		newData = []
		for data in dataArray:
			res = pow((data - mean), 2)
			newData.append(res)
		# calc new mean
		newSumm = 0.0
		for data in newData:
			newSumm += data
		newMean = newSumm / len(newData)
		standardDevation = pow(newMean, 0.5)
		return standardDevation, mean
