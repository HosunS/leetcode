class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        '''
        first index of customers = another list
        first index of each customer = arrival
        second index of each customer = time

        have numCustomers for average
        sumOfWait 
        finishingTime
        '''
        numCustomers = len(customers)
        sumOfWait = 0
        finishingTime = customers[0][0]

        for arrival,wait in customers:
            if arrival > finishingTime:
                finishingTime = arrival
            finishingTime += wait
            sumOfWait += finishingTime - arrival

        return sumOfWait/numCustomers


# 7  + 4 - 5 
