class BayesianNetwork:
    prob_dict = {}
    probBurglary = 0.001
    probEarthquake = 0.002
    prob_dict['maryTrue'] = {'alarmTrue':0.70,'alarmFalse':0.01}
    prob_dict['johnTrue'] = {'alarmTrue':0.90,'alarmFalse':0.05}
    prob_dict['alarmTrue'] = {'BTrue_ETrue':0.95,'BTrue_EFalse':0.94,'BFalse_ETrue':0.29,'BFalse_EFalse':0.001}


    def calculateProbability(self, burglary, earthquake, alarm, john, mary, conditions):
        pJohnCall = 0.00
        pMaryCall = 0.00
        pAlarm = 0.00
        probability = 1
        burglary_new = 0.00
        earthquake_new = 0.00
        denominator = 1.00

        if earthquake:
            earthquake_new = self.probEarthquake
        else:
            earthquake_new = 1 - self.probEarthquake

        if burglary:
            burglary_new = self.probBurglary
        else:
            burglary_new = 1 - self.probBurglary

        if alarm:
            if john:
                pJohnCall = self.prob_dict['johnTrue']['alarmTrue']
            else:
                pJohnCall = 1 - self.prob_dict['johnTrue']['alarmTrue']
            if mary:
                pMaryCall = self.prob_dict['maryTrue']['alarmTrue']
            else:
                pMaryCall = 1 - self.prob_dict['maryTrue']['alarmTrue']
        else:
            if john:
                pJohnCall = self.prob_dict['johnTrue']['alarmFalse']
            else:
                pJohnCall = 1 - self.prob_dict['johnTrue']['alarmFalse']
            if mary:
                pMaryCall = self.prob_dict['maryTrue']['alarmFalse']
            else:
                pMaryCall = 1 - self.prob_dict['maryTrue']['alarmFalse']

        if burglary and earthquake:
            if alarm:
                pAlarm = self.prob_dict['alarmTrue']['BTrue_ETrue']
            else:
                pAlarm = 1 - self.prob_dict['alarmTrue']['BTrue_ETrue']
        if (not burglary) and earthquake:
            if alarm:
                pAlarm = self.prob_dict['alarmTrue']['BFalse_ETrue']
            else:
                pAlarm = 1 - self.prob_dict['alarmTrue']['BFalse_ETrue']
        if burglary and (not earthquake):
            if alarm:
                pAlarm = self.prob_dict['alarmTrue']['BTrue_EFalse']
            else:
                pAlarm = 1 - self.prob_dict['alarmTrue']['BTrue_EFalse']
        if (not burglary) and (not earthquake):
            if alarm:
                pAlarm = self.prob_dict['alarmTrue']['BFalse_EFalse']
            else:
                pAlarm = 1 - self.prob_dict['alarmTrue']['BFalse_EFalse']

        for condition in conditions:
            if condition == 'B':
                denominator*=burglary_new
            if condition == 'E':
                denominator*=earthquake_new
            if condition == 'A':
                denominator*=pAlarm
            if condition == 'J':
                denominator*=pJohnCall
            if condition == 'M':
                denominator*=pMaryCall

        numerator = (pJohnCall*pMaryCall*pAlarm*burglary_new*earthquake_new)
        return numerator/denominator
