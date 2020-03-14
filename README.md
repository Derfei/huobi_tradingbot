# huobi_tradingbot
A python robot to trade on HuoBiGloal. The trading strategy is powered by the reinforce leanring.

## description

To have a try on the trading on bitcoin, I build a trading robot to enter the Houbi Global Market. 


The trading decesion is  only two decesions:
* long (做多)
* short (做空)

The base trading strategy is that the robot decide to long or short in the best price.

There are five python scripts in total. They are:
* `main.py` : This file provide the arguments for the users.
* `server.py`: This file provide the interference for necessary information to the users. 
* `utils.py` : This file provide the basic functions, like get the maket data, get the balance.
*  `learning.py`: This file provide the reinforce learning algorithm for the robot.
*  `trading_robot`: This file integreate the learning algorithm and the market operation.

## logs

