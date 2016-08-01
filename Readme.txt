Name: Suyog Swami

The code for learning probabilities from training data is in the file LearningProbability.py
	We have training_data.txt which has the data for four dependent events.
	We should use the following command to execute the program.
		python LearningProbability.py training_data.txt
	The code accepts training_data.txt as input.
	The table required is in the Q2.docx

	1) This implementation of bayesian network contains 2 files BayesianNetwork.py and bn.py.
	2) BayesianNetwork.py is a class file containing one function CalculateProbability. Also it contains initial probability values given in the diagrams stored in an dictionary.
	3) The function CalculateProbability takes six parameters, the boolean values for the five variables burglary, earthquake, alarm, john calling, mary calling and a list of variables that are given as condition.
	5) The file bn.py contains createRow which takes an empty list and the list of values for the variables and returns a list of boolean values that represents a row in the truth table for the variables.
	6) The function readInput creates list of boolean values depending on the given input.
		To execute use the following command
		python bn.py Bt Af Mf Jt Et
		python bn.py Jt Af given Bt Ef
		python bn.py Bt Af given Mf
		python bn.py Af Et

 
 