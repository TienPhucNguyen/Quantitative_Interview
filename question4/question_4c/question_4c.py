import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


aapl = pd.read_csv(r'D:\quant_interview\question4\AAPL.csv')
ibm = pd.read_csv(r'D:\quant_interview\question4\IBM.csv')
goog = pd.read_csv(r'D:\quant_interview\question4\GOOG.csv')
bp = pd.read_csv(r'D:\quant_interview\question4\BP.csv')
xom = pd.read_csv(r'D:\quant_interview\question4\XOM.csv')
cost = pd.read_csv(r'D:\quant_interview\question4\COST.csv')
gs = pd.read_csv(r'D:\quant_interview\question4\GS.csv')
list_of_stocks = [aapl, ibm, goog, bp, xom, cost, gs]

def stock_daily_return(stock):
    result = []
    for i in range(len(stock) - 1):
        result.append((stock['Close'][i+1]-stock['Close'][i])/stock['Close'][i])
    return result
sigma = 900*np.cov(np.array([stock_daily_return(stock) for stock in list_of_stocks]))
sigma_t = sigma.transpose()
inverse_sigma = np.linalg.inv(sigma)

r = 0.03
vector1 = np.ones(7)
D = np.array([[1, 0, 0, 0, 0, 0, -1],
              [0, 1, 0, 0, 0, 0, -1],
              [0, 0, 1, 0, 0, 0, -1],
              [0, 0, 0, 1, 0, 0, -1],
              [0, 0, 0, 0, 1, 0, -1],
              [0, 0, 0, 0, 0, 1, -1]])
D_t = D.transpose()
a = D.dot(sigma).dot(sigma_t).dot(D_t)
inverse_a = np.linalg.inv(a)
A = D_t.dot(inverse_a).dot(D)
"Vector c"
I7 = np.identity(7)
e7 = np.array([0, 0, 0, 0, 0, 0, 1])
c = (I7 - A.dot(sigma).dot(sigma_t)).dot(e7)


aapl = pd.read_csv(r'AAPL.csv')
ibm = pd.read_csv(r'IBM.csv')
goog = pd.read_csv(r'GOOG.csv')
bp = pd.read_csv(r'D:BP.csv')
xom = pd.read_csv(r'XOM.csv')
cost = pd.read_csv(r'COST.csv')
gs = pd.read_csv(r'GS.csv')
#Jan 2016
for i in range(len(aapl) - 1):
    months =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    previous_month_returns = []
    sum = 0
    for stock in list_of_stocks:
        previous_month_returns.append((stock['Close'][i+1]-stock['Close'][i])/stock['Close'][i])
    next_month_portfolio = A.dot(np.array(previous_month_returns)) + c
    for j in range(len(next_month_portfolio)):
        sum+= next_month_portfolio[j]
    print(f'The optimal portfolio of {months[i]} is {next_month_portfolio}')


