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
portfolio = {'AAPL': 0.15, 'IBM': 0.2, 'GOOG': 0.2, 'BP': 0.15, 'XOM':0.1, 'COST': 0.15, 'GS': 0.05}
daily_return = []
for i in range(len(aapl)-1):
    daily_return.append(portfolio['AAPL']*(aapl['Close'][i+1] - aapl['Close'][i])/aapl['Close'][i] +
                                portfolio['IBM']*(ibm['Close'][i+1] - ibm['Close'][i])/ibm['Close'][i] +
                                portfolio['GOOG']*(goog['Close'][i+1] - goog['Close'][i])/goog['Close'][i] +
                                portfolio['BP']*(bp['Close'][i+1] - bp['Close'][i])/bp['Close'][i] +
                                portfolio['XOM']*(xom['Close'][i+1] - xom['Close'][i])/xom['Close'][i] +
                                portfolio['COST']*(cost['Close'][i+1] - cost['Close'][i])/cost['Close'][i] +
                               portfolio['AAPL']*(gs['Close'][i+1] - gs['Close'][i])/gs['Close'][i] )
arr = np.array(daily_return)
loss = arr*-1
daily_significance = 0.95**(1/252)
daily_max_loss = np.percentile(loss, daily_significance*100)
print(f'Daily VaR at significance of {daily_significance} is: {daily_max_loss}')
VaR = 1- (1 - daily_max_loss)**252
print(f'VaR of the portfolio in 31/12/2016 at 95% is: {VaR}')
#Compute CVaR
con_loss = []
for x in loss:
    if x >= daily_max_loss:
        con_loss.append(x)

con_loss_arr = np.array(con_loss)
CVaR = 1 - (1-np.mean(con_loss_arr))**252
print('CVaR of the portfolio in 31/12/2016 at 95% is: ', CVaR)

