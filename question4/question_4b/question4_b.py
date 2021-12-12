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
portfolio_ = [portfolio[st] for st in portfolio]
daily_return = []
for i in range(len(aapl)-1):
    daily_return.append(portfolio['AAPL']*(aapl['Close'][i+1] - aapl['Close'][i])/aapl['Close'][i] +
                                portfolio['IBM']*(ibm['Close'][i+1] - ibm['Close'][i])/ibm['Close'][i] +
                                portfolio['GOOG']*(goog['Close'][i+1] - goog['Close'][i])/goog['Close'][i] +
                                portfolio['BP']*(bp['Close'][i+1] - bp['Close'][i])/bp['Close'][i] +
                                portfolio['XOM']*(xom['Close'][i+1] - xom['Close'][i])/xom['Close'][i] +
                                portfolio['COST']*(cost['Close'][i+1] - cost['Close'][i])/cost['Close'][i] +
                               portfolio['AAPL']*(gs['Close'][i+1] - gs['Close'][i])/gs['Close'][i] )

def stock_daily_return(stock):
    result = []
    for i in range(len(stock) - 1):
        result.append((stock['Close'][i+1]-stock['Close'][i])/stock['Close'][i])
    return result
portfolio_mean_return = np.mean(np.array(daily_return))
portfolio_mean_loss = -portfolio_mean_return
cov_matrix = np.cov(np.array([stock_daily_return(stock) for stock in list_of_stocks]))
portfolio_variance = np.array(portfolio_).dot(cov_matrix).dot(np.array(portfolio_))
portfolio_deviation = np.sqrt(portfolio_variance)
daily_VaR = 1.65*portfolio_deviation + portfolio_mean_loss
print('Daily VaR at 95% of the portfolio is: ', daily_VaR)




