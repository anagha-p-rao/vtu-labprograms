# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
import math
import statistics

#1
def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    dataset = dataset[1:]  # Removing the header from the dataset
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

#2
def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = dataset[:trainSize]
    copy = dataset[trainSize:]
    return [trainSet, copy]

#4
def separateByClass(dataset):
    # seperating data set where results are either 1.0 or 0.0,as dictionary where ,eg: result with 1.0 are in that list
    separated = {1.0:[],0.0:[]}
    for i in dataset:
        separated[i[-1]].append(i)
    return separated

#5
def summarize(dataset): # for every attribute in dataset find mean and standard deviation
    summaries = [(statistics.mean(attribute), statistics.stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

#3
def summarizeByClass(dataset):   # in summarizeByClass by class : SeperateByClass + Summarize
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        # here classvalue = 1.0 or 0.0 and instances are the values of the dictionary
        # summaries by class are getting summarised
        summaries[classValue] = summarize(instances)
    return summaries

#9
def calculateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

#8
def calculateClassProbabilities(summaries, inputVector):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = inputVector[i]
            probabilities[classValue] *= calculateProbability(x, mean,stdev)
    return probabilities

#7
def predict(summaries, inputVector):
    probabilities = calculateClassProbabilities(summaries, inputVector)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel

#6
def getPredictions(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions

# get the values if testset last value is same as predicted value
def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1        
    return (correct/float(len(testSet))) * 100.0


filename = 'NaiveBayesDiabetes.csv'
splitRatio = 0.67

dataset = loadCsv(filename)
trainingSet,testSet=splitDataset(dataset, splitRatio)

print('Split ',len(dataset),' rows into train=',{len(trainingSet)},' and test=',{len(testSet)},' rows')
 # prepare model
    
summaries = summarizeByClass(trainingSet)
 # test model
predictions = getPredictions(summaries, testSet)
accuracy = getAccuracy(testSet, predictions)
print('Accuracy: {0}%'.format(accuracy))
print('Prediction:{0}'.format(predictions))