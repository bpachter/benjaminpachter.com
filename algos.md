---
layout: page
title: Algorithms
permalink: /trade_algos/
---
<img src="/john.gif" alt="GBM" title="GBM" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">

Hey there! Thanks for your patience as I build out this page and make it better with integrated Jupyter Notebooks.


Let's dive into some basic trading algorithms and blockchain technologies, as well as more complex equity momentum simulation!


## Implementing a Simple Trading Strategy using C++

Let's start with a simple trading strategy using C++. This example demonstrates a moving average crossover strategy, which generates buy/sell signals based on short-term and long-term moving averages of stock prices. Moving averages help smooth out price data and identify trends over a specific period.


### Code

```cpp
#include <iostream>
#include <vector>

// Function to calculate the moving average for a given period
double calculateMovingAverage(const std::vector<double>& prices, int period) {
    if (prices.size() < period) return 0.0; // Not enough data points
    double sum = 0.0;
    for (int i = prices.size() - period; i < prices.size(); ++i) {
        sum += prices[i];
    }
    return sum / period;
}

int main() {
    // Sample stock prices (example data)
    std::vector<double> prices = {234.56, 230.12, 240.00, 245.67, 250.89, 255.45, 260.00};
    int shortPeriod = 3; // Short-term moving average period (e.g., 3 days)
    int longPeriod = 5;  // Long-term moving average period (e.g., 5 days)

    // Loop through the prices to generate buy/sell signals based on moving averages
    for (int i = longPeriod; i <= prices.size(); ++i) {
        // Calculate short-term and long-term moving averages
        double shortMA = calculateMovingAverage(std::vector<double>(prices.begin(), prices.begin() + i), shortPeriod);
        double longMA = calculateMovingAverage(std::vector<double>(prices.begin(), prices.begin() + i), longPeriod);

        // Generate trading signals based on moving average comparison
        if (shortMA > longMA) {
            std::cout << "Buy signal at price: $" << prices[i - 1] << std::endl;
        } else if (shortMA < longMA) {
            std::cout << "Sell signal at price: $" << prices[i - 1] << std::endl;
        } else {
            std::cout << "Hold at price: $" << prices[i - 1] << std::endl;
        }
    }

    return 0;
}

```
<br>

### Explanation

#### Moving Average Calculation:
The `calculateMovingAverage` function computes the average of stock prices over a specified period.
#### Trading Logic:
The `main` function initializes stock prices and periods for short-term and long-term moving averages. It then iterates through the prices, calculating moving averages and generating buy/sell signals based on their comparison.

<br>

## Automated Trading with Interactive Brokers (IBKR) through Python
For retail traders like myself, Interactive Brokers (IBKR) offers an awesome and powerful platform for automated trading, enabling us to *almost* compete with institutional investors to execute advanced trading strategies using real-time data and historical pricing (okay I'm joking). But regardless, implementing automated trading through IBKR can be a fantastic method of understanding complex option stategies.

I usually implement my personal projects using the **ib_insync** library in Python, which provides an intuitive way to work with the IBKR API. This approach allows for the development of strategies ranging from simple moving average crossovers to more complex algorithmic trading strategies involving machine learning predictions.

# Automated Straddle Trading on SPX with Interactive Brokers (IBKR)
Automated trading strategies using Interactive Brokers (IBKR) can be highly effective for options trading, particularly for neutral strategies like straddles that benefit from large directional market moves or spreads where your risk is defined.

In this example, I am showcasing a straddle, which involves buying a call and a put option with the same strike price and expiration date, anticipating high volatility that will move the stock price significantly in either direction. This particular strategy is useful if a large move is expected in the underlying, for example, a CPI/GDP print or Federal Reserve FOMC meeting.

Example: Straddle Trading Strategy
```py
from ib_insync import *

# Function to simulate fetching EMA data from TradingView or another source

def get_ema_values():
    ema30 = 3000
    ema50 = 3050
    ema200 = 3100
    return ema30, ema50, ema200

# Function to determine trade signal based on key EMA crossovers
def check_ema_signals(ema30, ema50, ema200):
    if ema30 > ema200:
        return 'call'  # Bullish signal
    elif ema30 < ema200:
        return 'put'   # Bearish signal
    else:
        return 'neutral'

# Main trading logic
def trade_spx_straddle():
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)

    # Define the SPX option contracts for a straddle at specific strike and date
    spx_call = Option('SPX', '20240621', 5300, 'C', 'SMART')
    spx_put = Option('SPX', '20240621', 5300, 'P', 'SMART')

    # Request market data for the options
    ib.reqMktData(spx_call)
    ib.reqMktData(spx_put)
    ib.sleep(2)  # Sleep to allow time for data retrieval

    # Place the straddle order
    call_order = MarketOrder('BUY', 1)
    put_order = MarketOrder('BUY', 1)
    call_trade = ib.placeOrder(spx_call, call_order)
    put_trade = ib.placeOrder(spx_put, put_order)

    # Fetch EMA values
    ema30, ema50, ema200 = get_ema_values()

    # Determine signal based on EMA crossovers
    signal = check_ema_signals(ema30, ema50, ema200)
    if signal == 'call':
        print("Closing put leg, market bullish")
        close_put = MarketOrder('SELL', 1)
        ib.placeOrder(spx_put, close_put)
    elif signal == 'put':
        print("Closing call leg, market bearish")
        close_call = MarketOrder('SELL', 1)
        ib.placeOrder(spx_call, close_call)

    # Disconnect from IB after trades
    ib.disconnect()

# Assuming this script runs within a trading environment setup
trade_spx_straddle()
```
### Explanation

#### Fetching EMA Data:
The `get_ema_values` function simulates fetching Exponential Moving Average (EMA) values.
#### EMA Signals:
The `check_ema_signals` function determines the trading signal (call, put, neutral) based on EMA crossovers.
#### Trading Logic:
The `trade_spx_straddl`e function connects to IBKR, defines SPX options for a straddle, fetches market data, places orders, and determines signals to adjust the strategy based on EMA crossovers.
<br><br><br>

## Distributed Systems and Blockchain

Distributed systems are critical for handling large-scale financial data processing. Technologies like Apache Kafka, Spark, and Cassandra are used to manage, process, and analyze data in real-time, providing scalability and fault tolerance.

### Example: Real-time Data Processing with Apache Kafka and Spark
This example demonstrates real-time data processing using Apache Kafka and Spark. It reads data from a Kafka topic, processes it with Spark, and writes the processed data to a Cassandra database.
```py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder \
    .appName("Financial Data Processing") \
    .getOrCreate()

# Read data from Kafka
df = spark.read.format("kafka").options(
    kafka.bootstrap.servers="localhost:9092",
    subscribe="financial_data"
).load()

# Process data
processed_df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .withColumn("value", col("value").cast("double"))

# Write processed data to Cassandra
processed_df.write \
    .format("org.apache.spark.sql.cassandra") \
    .options(table="financial_data", keyspace="finance") \
    .save()

```

### Explanation

#### Spark Session:
A Spark session is created to manage the Spark application.

#### Reading Data from Kafka:
Data is read from a Kafka topic named "financial_data".

#### Processing Data:
The data is cast to appropriate types for processing.
<br><br>
#  Blockchain for Financial Transactions
Blockchain technology ensures secure and transparent transactions in financial systems. Smart contracts can automate financial agreements, and distributed ledgers provide a tamper-proof record of transactions.

### Example: Smart Contract for Automated Payments
This example demonstrates a simple smart contract for automated payments using Solidity. The contract allows a payer to send a specified amount to a payee.

```js
pragma solidity ^0.8.0;

contract PaymentContract {
    address public payer;
    address public payee;
    uint256 public amount;

    constructor(address _payee, uint256 _amount) {
        payer = msg.sender;
        payee = _payee;
        amount = _amount;
    }

    function makePayment() public payable {
        require(msg.sender == payer, "Only the payer can make the payment");
        require(msg.value == amount, "Incorrect payment amount");

        payable(payee).transfer(amount);
    }
}
```
### Explanation

#### Contract Initialization:
The `constructor` initializes the payer, payee, and payment amount.

#### Payment Function:
The `makePayment` function allows the payer to send the specified amount to the payee, ensuring only the payer can make the payment and the correct amount is sent.

<br>

## Stock Price Simulation Using Geometric Brownian Motion (GBM)

Geometric Brownian Motion (GBM) is a mathematical model widely used in finance to simulate the price paths of stocks and other financial assets. The GBM model incorporates both the deterministic trend and the stochastic component of asset prices, making it suitable for modeling the random behavior of stock prices over time.

<img src="/GBM2.png" alt="GBM" title="GBM" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">

### Mathematical Formulation of GBM

The Geometric Brownian Motion model is defined by the stochastic differential equation (SDE):
<img src="/GBM.png" alt="GBM" title="GBM" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 60%;">

where:
- **S_t**  is the stock price at time t .
- **μ** is the drift term, representing the expected return.
- **σ** is the volatility term, representing the standard deviation of the stock's returns.
- **dW_t** is a Wiener process (or Brownian motion), representing the random component.
The solution to this SDE gives the following formula for simulating stock prices:
<img src="/StockPriceSim.png" alt="GBM" title="GBM" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 75%;">

### C++ Implementation

To frame up this simulation in C++, here are the three main components of GBM we will need to implement for simulating randomized stock price behavior:

 **Generating Gaussian Noise**:
   The function `generateGaussianNoise()` generates normally distributed random numbers using the Box-Muller transform, which converts uniformly distributed random numbers into Gaussian distributed random numbers.

 **Simulating Stock Prices**:
   The function `simulateStockPrices()` generates a vector of stock prices over a specified number of days using the GBM model. It starts with an initial stock price S_0 and iteratively applies the GBM formula to compute the stock price for each subsequent day.

 **Main Function**:
   The `main()` function initializes the parameters, calls the `simulateStockPrices()` function, and prints the simulated stock prices.

### C++ Code

# Simulating Stock Prices using Geometric Brownian Motion in C++:

```cpp

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>

// Function to generate Gaussian noise using Box-Muller transform
double generateGaussianNoise() {
    static double z1;
    static bool generate;
    generate = !generate;

    if (!generate) return z1;

    double u1, u2;
    do {
        u1 = rand() * (1.0 / RAND_MAX);
        u2 = rand() * (1.0 / RAND_MAX);
    } while (u1 <= std::numeric_limits<double>::min());

    double z0;
    z0 = sqrt(-2.0 * log(u1)) * cos(2 * M_PI * u2);
    z1 = sqrt(-2.0 * log(u1)) * sin(2 * M_PI * u2);
    return z0;
}

// Function to simulate stock prices using Geometric Brownian Motion
std::vector<double> simulateStockPrices(double S0, double mu, double sigma, int days) {
    std::vector<double> prices;
    prices.push_back(S0);
    for (int i = 1; i <= days; ++i) {
        double dt = 1.0 / 252; // Assuming 252 trading days in a year
        double dW = sqrt(dt) * generateGaussianNoise();
        double St = prices.back() * exp((mu - 0.5 * sigma * sigma) * dt + sigma * dW);
        prices.push_back(St);
    }
    return prices;
}

int main() {
    srand(time(0)); // Seed the random number generator

    double S0 = 100.0;   // Initial stock price
    double mu = 0.1;     // Expected return (drift)
    double sigma = 0.2;  // Volatility
    int days = 252;      // Number of days to simulate

    std::vector<double> prices = simulateStockPrices(S0, mu, sigma, days);

    for (double price : prices) {
        std::cout << "Price: $" << price << std::endl;
    }

    return 0;
}

```
### Explanation

#### Generating Gaussian Noise:
The `generateGaussianNoise()` function uses the Box-Muller transform to generate normally distributed random numbers. This is necessary for simulating the random component of the stock price changes.

#### Simulating Stock Prices:

The `simulateStockPrices()` function initializes the stock price vector with the initial price S_0.
​

For each day, it calculates the change in stock price using the GBM formula.
The stock price for the next day 
S_t+1 is computed using the previous day's price, the drift term, and the random shock generated by `generateGaussianNoise()`.

#### Main Function:

The `main()` function sets the initial parameters and calls the `simulateStockPrices()` function.
It then prints each simulated stock price to the console.
Practical Applications

#### Risk Management:

Simulating future stock prices helps in assessing the potential risks and returns associated with different investment strategies.

#### Option Pricing:

GBM is used in the Black-Scholes model to price European options by simulating the underlying asset's price paths.

#### Portfolio Optimization:

Simulated price paths can be used to evaluate the performance of different portfolio compositions under various market conditions.

#### Stress Testing:

Financial institutions use simulations to test how their portfolios would perform under extreme market conditions.

## Advanced AI Algorithms in Finance

### Predictive Modeling and Machine Learning
Machine learning algorithms are essential for predictive modeling in finance. Techniques such as regression, classification, clustering, and time series analysis can forecast market trends, asset prices, and financial risks. These models help in making informed decisions by analyzing historical data and identifying patterns that can predict future movements.

#### Example: Time Series Forecasting with LSTMs

Long Short-Term Memory (LSTM) networks are a type of recurrent neural network (RNN) capable of learning long-term dependencies, making them suitable for time series forecasting. In finance, LSTMs can be used to predict stock prices, market trends, and other financial metrics based on historical data.

### Code

```python
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data
data = pd.read_csv('financial_data.csv')
prices = data['price'].values

# Prepare data for LSTM
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 3
X, Y = create_dataset(prices.reshape(-1, 1), look_back)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Build LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(look_back, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(X, Y, epochs=20, batch_size=1, verbose=2)

# Make predictions
predictions = model.predict(X)
```
### Explanation

Loading the data with a csv as an example:
```py
data = pd.read_csv('financial_data.csv')
prices = data['price'].values
```
#### Data Source:
The financial data is loaded from a CSV file named financial_data.csv. The data contains historical price information.

#### Extracting Prices:
The prices are extracted from the 'price' column and stored in the prices array.

#### Preparing Data for LSTM:

```py
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 3
X, Y = create_dataset(prices.reshape(-1, 1), look_back)
X = np.reshape(X, (X.shape[0], X.shape[1], 1))
```
- Function Definition: The `create_dataset` function transforms the time series data into a format suitable for LSTM. It creates input-output pairs where the input is a sequence of prices and the output is the price at the next time step.
- Look-back Period: The `look_back` variable defines the number of previous time steps to use as input for predicting the next value. In this case, it is set to 3.
- Reshaping Data: The input data X is reshaped to be compatible with the LSTM layer's expected input shape.

#### Building the LSTM Model:

```py
model = Sequential()
model.add(LSTM(50, input_shape=(look_back, 1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
```
#### Sequential Model Initialization:
- LSTM Layer: An LSTM layer with 50 units is added to the model. The input shape is specified as (look_back, 1), indicating the model expects sequences of 3 time steps with 1 feature per step.
- Dense Layer: A dense layer with a single unit is added, which will output the predicted price.
- Compilation: The model is compiled with the mean squared error loss function and the Adam optimizer, which is commonly used for training deep learning models.

#### Training the Model:
```py
model.fit(X, Y, epochs=20, batch_size=1, verbose=2)
```

#### Model Training:
The model is trained using the input-output pairs (X, Y) for 20 epochs with a batch size of 1. The verbose level is set to 2 to provide detailed logs during training.
Making Predictions:
```py
predictions = model.predict(X)
```
- Generating Predictions: The trained model is used to make predictions on the input data X. The predicted values are stored in the predictions array.

### Practical Applications

#### Stock Price Prediction:

LSTM models can predict future stock prices based on historical data, helping traders and investors make informed decisions.

#### Market Trend Analysis:

By analyzing historical market data, LSTM models can identify trends and potential turning points in the market.

#### Risk Management:

Predictive models can assess potential risks and returns, enabling better risk management strategies for investment portfolios.

#### Algorithmic Trading:

Integrating LSTM models into trading algorithms can automate trading strategies based on predicted market movements.
<br><br>
By leveraging advanced AI algorithms like LSTMs, financial institutions and traders can enhance their predictive modeling capabilities, leading to more accurate forecasts and improved decision-making in the financial markets.

<br><br><br>
More to Come!
Stay tuned for more demonstrations and code examples showcasing various algorithms and technologies. From advanced trading strategies and AI models to distributed systems and blockchain implementations, this page will be continually updated with cutting-edge solutions and insights.

Feel free to check back regularly for new content and detailed explanations of complex financial and technological concepts!

