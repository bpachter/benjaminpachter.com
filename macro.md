---
layout: page
title: Macro
permalink: /macro/
---
## Options, Enormous Tail Risk, and Stagflation
# History is repeating itself; a data-driven review on why the 1970s and early 1980s are back in action

With an overwhelming amount of noise in the modern age and an abundance of conflicting narratives regarding the state of the global economy, it's more important than ever to sift through the chatter and focus on the key data that drives central bank decisions. This page is my attempt to quell some of this noise; to have a conversation about the trends and patterns that appear to be repeating from several decades ago, while demonstrating how anyone can shape and analyze this data themselves to validate some of the hyperbolic and wishful headlines and soundbites coming at us from every direction. 

<div class="tradingview-widget-container" style="height:600px; width:100%;">
  <div class="tradingview-widget-container__widget" style="height:100%; width:100%;"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank"><span class="blue-text">Track all markets on TradingView</span></a></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
  {
    "autosize": true,
    "symbol": "NASDAQ:NDX",
    "interval": "M",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "en",
    "allow_symbol_change": true,
    "calendar": false,
    "height": "600",
    "width": "100%"
  }
  </script>
</div>


The S&P 500, Dow Jones, and NASDAQ all are once again at all-time-highs while the economy continues to march ahead, despite the Federal Reserve raising interest rates faster than ever before in 2022-2023. Labor remains substantially stronger than expected with every new data print and higher unemployment is nowhere to be seen, despite recessionistas on Twitter calling for an imminent market crash with every negative economic data print. I will admit I myself have gone short through index put option instruments in anticipation of a severe correction, notably when Silicon Valley Bank, Signature Bank, and Silvergate all blew up in March 2023 due to lousy interest rate exposure. Boy was I wrong.

As I type this, the NASDAQ index is up 56% since these bank failures occured. Everyone went short all at once when the first bank Silvergate went up, and institutions only continued to add to these massive put positions on the indices as the bank news got worse with Sillicon Valley Bank, then Signature next. It was 2008 all over again! But once the Fed cleverly implemented the Bank Term Funding Program (BTFP), it was clear liquidity was back in place and there would be no domino-effect of larger bank failures like in the GFC. All of those short positions got squeezed out, and the entire US stock market effectively became similar to the infamous Gamestop short-squeeze in January 2021. The rapid closing of these huge bearish positions on the SPX, SPY, and QQQ put heavy short-term bullish pressure on the entire market.  

# It's Gamma all the way down...

It's no secret the equity indices and the fundamental macro economy rarely (if ever) align; the two of them should almost be considered mutually exclusive of each other on any time frame but the long run. I've lost count of all of the times a bad data print is released in the morning and the market ends the day higher than it started. Most people see this and simply dismiss the equity markets as casinos designed to take your money, and they have every right reason to do so! Surely the markets should have dropped from this clearly bearish macro data point, but everyone decided halfway through the day to turn bullish for no reason! There is practically no transparancy involved, because that is exactly how the system is designed to work. 

<img src="/Gamma.png" alt="Gamma" title="Gamma" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">

The truth is market maker / dealer mechanics and the predominant options chain positioning on the largest instruments utilized (index options primarily, along with the MAG 7 and ETFs like SPY, QQQ, IWM, etc.) were the reasons the market ended the day higher, despite the bearish data print. This is the same for all volatile market reactions that initially appear to make sence according to the economic data release but eventually turn around, and of course when the initial reaction is the complete opposite than the data would suggest. Those are just the best, aren't they?

Insitutions with megalithic amounts of money at stake usually have an almost unlimited line of credit to throw at at options 0-DTES, weeklies, and futures. If there is a surprising data drop and the market drops 100 bps when a large hedgefund was still holding bullish out-of-the-money calls, you can damn well bet they are going to throw the kitchen sink at their underwater positioning to try and get it back. I'll get to how they are typically saving their positions in a moment, but a fundamental understanding of how gamma ramps work is critical here.

The bar chart above is a snapshot of the total gamma positioning of the SPX options chain (I am writing this on Sunday 5/19/2024). 
**Gamma positioning reflects the influence of options hedging activities on the underlying asset's price.** When large short-dated options positions exist, they carry more gamma-weight and act as "gravitational centers"; this means that significant gamma at specific strike prices creates strong forces that pull the asset's price towards these levels. Larger gamma concentrations at certain strikes (often referred to as "gamma walls") can stabilize the price around these points due to the hedging actions of options dealers/market makers. They adjust their positions by buying as the price drops and selling as it rises, thereby exerting a gravitational effect on the underlying asset. 

Specifically, gamma refers to the rate of change of an option's delta with respect to changes in the price of the underlying asset.

Delta is the first derivative of the option's price with respect to the underlying asset's price. It measures the sensititivity of the option's price to a $1 change in the price of the underlying asset.

So if Delta is the first derivative, Gamma is the second derivative, which measures the rate of change of delta for a $1 change in the price of the underlying. 

When there is a high level of gamma, small movements in the underlying asset can lead to significant changes in delta, prompting market makers and other participants to adjust their hedges more frequently and aggressively.

<a href="https://imgflip.com/i/8qlc9l"><img src="https://i.imgflip.com/8qlc9l.jpg" title="and delta and vega and OI and IV but mostly gamma :)"/></a><a href="https://imgflip.com/memegenerator">

At all times there is a fluctuating amount of delta and gamma open interest depending on what options retail and institutional traders are buying and selling. As there is a symbiotic relationship between calls and puts on the same underlying chain, the price will slip right through strikes that are heavily-skewed one way or the other, and will constantly find gravitational resistance at strikes that are highly contested. 

Additionally, the prices of options are influenced by the implied volatility of the underlying asset established by the market maker. If the demand for puts increases, it can drive up the implied volatility, which in turn can affect the prices of calls as well, since implied volatility is a key input in the pricing models for both types of options.

<img src="/Surf.png" alt="Gamma" title="Gamma" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">

Gamma-neutral positioning involves adjusting a portfolio so its overall gamma, or sensitivity to changes in the underlying asset's price, is zero. This is done to stabilize positions and reduce risk.

When the underlying asset's price is above the gamma-neutral level, market makers are typically net short gamma. They buy the underlying asset as its price rises to hedge their position, which can push prices higher. Conversely, when the price is below the gamma-neutral level, they are net long gamma and sell the underlying asset as its price falls, potentially driving prices lower.

This hedging creates a stabilizing effect, with large gamma positions acting like gravity walls, pulling the underlying asset's price back towards them depending on the size of the positioning at each strike level.

So, now that you have an understanding of gamma mechanics, this will make much more sence.

## How to save billions of dollars of underwater 0-DTEs 

Since the introduction of 0-DTE (days-to-expiry) options in the indices like SPX in 2022, the methods institutional traders utilize to move around the markets as described above have become totally different to what Benjamin Graham, the father of long-term value investing, ever could have imagined. In fact, if he were alive today, he would likely be nothing short of horrified.

The trillions of 401k dollars that are being put at risk by these incredibly risky and dangerous options markets is frightening. Even though the fundamentals of how indices and underlying equities move in the short-term is radically different, the fundamental health of the global economy will always remain king in the long term, since.. you know.. it's actually real.

Macro fundamentals, surprising data points, and earnings releases all matter just as much as the tie color that Jerome Powell is wearing at the FOMC speeches. When there are violent moves with a high degree of continuous momentum, the price is simply riding the gamma-slide of price acceleration that is being put in-place by the overwhelming put-bias at the strikes people are buying. The price stops sliding down when it has reached the end of the gamma ramp on the chain and all those ITM calls begin taking profits. If things are really bearish for whatever reason, people continue to buy at lower OTM strikes. When there is a substantial amount of fear, everyone is piling into puts and driving up IV prices, further enhancing put values, which continues on as gearing effect for the entire market. This is how you get flash crashes with violent recoveries, like volmagedeon in 2018 and the pandemic crash of 2020.

This is also true in the opposite direction, where it seems like market upside will never stop! After the Fed rapidly put the BTFP together, all the bearish calls sold short above 

Once 0-DTE SPX options were introduced, short-term market action became almost entirely controlled by the mechanics described above in regard to the shortest dated options, where there is a continuous gearing effect driven by market maker hedging depending on the net-gamma environment on the underlying indices and stocks. So yeah, this particular aspect of the market is reminiscent of a casio where the biggest bets matter the most. Unfortunately, Big eats Small, and the world has been like this since the beginning of life itself. But, the fortunate side is that most of this is trackable with the right live data packages and work flows. Python and R are both incredible tools for shaping and displaying options chain data in visuals that can assist in rapid trading decision making. 

You wouldn't believe it, but there are active funds out there trading hundreds of millions of dollars in assets every day that are not looking at or are even aware of these market maker mechanics! But most of the biggest players are very aware of how all this really works, and they are determined to use these mechanics alongside with their Liberian-GDP-sized-capital to their advantage wherever necessary. **Here's specifically how they do it, and why it is actually an incredibly large risk to all of us.**

<img src="/Gamma2.png" alt="Gamma2" title="Selling Puts ATM grants large amounts of sudden collected premium liquidity to margin traders, who then throw those funds directly into 0-DTE calls." style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">

Let's take another look at this SPX gamma positioning chart as an example. Anyone who has substantial margin can sell puts out-of-the-money (OTM). **By selling an option rather than buying it as an opening transaction, you are collecting the option's price directly as premium liquidity.** What you are hoping for is that your option will expire OTM and you will get to collect your premium. This is risky if you don't know what you're doing, because if your option goes in-the-money (ITM), you are now deeply underwater. You can close the position at a loss by buying-to-close at the higher ITM price, or you can hold on to it and hope it goes back OTM and expires worthless. 

If you are a GSIB or an extremely well-capitalized trader with market-moving money, this is fantastic news for you! If you happen to suddenly find yourself in a bad trade because of some lousy, data, relax! You can simply sell the hell out of all the options you want for free money, and then throw those funds into buying 0-DTES to push the markets back in your favor to save your underwater positioning!

**Since the March 2023 bank failures, this has been the name of the game:**

 - Buy 0-DTE calls OTM
 - Sell OTM Puts for premiums, buy more OTM calls if all is well
 - If market down and gamma is positive, relax and buy the dip!
 - If things are getting shaky, buy some ES futures chunks to further push the markets in your favor
 - If none of this is working, sell more puts. The closer to the money, the larger the premiums!
 - Rinse and repeat! 

**This is what is known as selling volatiliy.**

So this is totally awesome, and markets are going to go up forever because institutions can just sell all the puts they want, buy 0DTE calls, and keep this circus going into perpetuity! Right?

Nope.

The tail risk here should be obvious. If they sell too many puts and get caught with their sold positioning too far underwater to save it. That is where you get the sharp and compounding downside moves that occur in cyclical fashion in the open markets. There are all sorts of conjured up methods of selling volatility, and they are all equally risky when things go wrong. 

In peak desperation, there have even been instances where puts are being sold in-the-money!!!

A single legitimately bearish headline can instantly see a 100-300bps move downwards as the sold gamma on the chain squeezes downwards. There is no difference in sold gamma and bought gamma. The more puts they sell, the more the market maker has to hedge against those puts. 

**The macro data points, such as CPI, GDP, etc have never mattered to the indices. It has always been options positioning.**



## Breaking down the Dirty 'I-word'

<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=1o3mc&width=725&height=525" scrolling="no" frameborder="0" style="overflow:hidden; width:725px; height:600px;" allowTransparency="true" loading="lazy"></iframe>

Above is the yearly growth rate of the main components of the CPI in the United States. It is really just Food, Energy, and 'Core' CPI, which is everything else. Core CPI removes food and energy due to the claimed higher volatility of these sub-components.  I have separated the Energy index out on the right Y-axis as it is traditionally the most volatile index with much higher year-over-year changes. The BLS further breaks these down into their own sub-indices for which they periodically rebalance the weights:

<img src="/images/BLS1.png" alt="BLSCPI" title="BLS CPI Breakdown" style="border: 0px solid #ddd; padding: 10px; margin: 20px 0; display: block; max-width: 100%;">

So why am I talking about inflation right now? Surely we've all had enough of this since the pandemic!

Unfortunately, anyone who lived through the 1970s and 1980s should understand how annoying and 'sticky' inflationary periods can last in modern economies. While most people know it happened, few understand what ended this period. So just for fun, I am going to break down why we are not likely to see a quick end to inflation. The Fed chair Powell himself recently said that [his confidence that inflation will slow "is not as high as it was."](https://www.msn.com/en-us/money/markets/buckle-up-america-powell-says-interest-rates-will-likely-stay-higher-for-longer-as-inflation-stubbornly-refuses-to-come-down/ar-BB1mvKSB) 

Recently, we’ve seen heightened geopolitical tensions that are significantly impacting economic conditions. The conflict involving the Houthis in the Red Sea has led to disruptions in global shipping routes, forcing major companies to reroute and consequently increasing costs and shipping times. This has exacerbated inflationary pressures, particularly in the energy sector​​. Concurrently, the ongoing Israeli-Hamas conflict is contributing to instability in the Middle East, further complicating the economic outlook.

Given these factors, I remain skeptical about any imminent reduction in interest rates. Despite the Federal Reserve's aggressive rate hikes, inflation is likely to stay above their 2% year-over-year growth target. This persistent inflation, coupled with the added strain of geopolitical risks, suggests we might be facing a period of stagflation ahead very similar to the late 1970s and early 1980s, characterized by sluggish economic growth and high inflation, driven in part by rising oil prices. Understanding these dynamics is crucial as we navigate these uncertain times.

## How similar is this to the last major inflationary cycle?

The 1970s and early 1980s were marked by significant economic turmoil, characterized by high inflation, slow economic growth, and high unemployment. This period gave way to the even dirtier 'S-word': stagflation.

<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=1o3oZ&width=725&height=525" scrolling="no" frameborder="0" style="overflow:hidden; width:725px; height:600px;" allowTransparency="true" loading="lazy"></iframe>

In the first half of this cycle, as consumer- and producer-side prices began to increase exponentially, the Federal Funds Rate (FFR) acheived a peak of 12.92 in July 1974. Most of this first spike was directly caused by heightened geo-political turmoil in the middle east; OAPEC imposed an oil embargo against the United States and other countries supporting Israel during the Yom Kippur War. This led to a dramatic increase in oil prices, quadrupling from about $3 to nearly $12 per barrel, causing widespread global economic disruptions and energy shortages.

The record-high rates (so far) were enough to cause a slowdown in consumer lending and purchasing activity, which naturally led to a soft recession that was officialy declared afterwards to have started in November 1973 and lasted until March 1975.

During this period, the U.S. economy faced large rises in producer prices that were caused from producer-side inflation rather than the demand-driven consumer-side inflation. We saw a deathly combination of stagnant economic growth with high unemployment and rising prices. Inflation was exacerbated by the loose monetary policies of the late 1960s, which had been implemented to finance the Vietnam War and domestic social programs without raising taxes. Additionally, the collapse of the Bretton Woods system in the early 1970s led to the devaluation of the U.S. dollar, further fueling inflation​ (SJSU)​.

Consumers and businesses alike struggled during this recession. Investment spending plummeted, affecting everything from residential construction to business inventories. High inflation rates eroded purchasing power, making everyday goods more expensive. Unemployment rose, and economic uncertainty became pervasive. The Federal Reserve's initial response was to tighten monetary policy, but this only deepened the recession without curbing inflation significantly. It wasn't until Paul Volcker became Fed Chairman in 1979 and implemented aggressive interest rate hikes that inflation was brought under control, albeit at the cost of another recession in the early 1980s​ (Federal Reserve History)​ .








Monetary Policy:

The Federal Reserve's initial monetary policy in the late 1960s and early 1970s was expansionary, aiming to maintain low unemployment. However, it failed to control inflation, resulting in a persistent increase in prices.
The Fed, under Paul Volcker's leadership from 1979, took aggressive measures to combat inflation by significantly raising interest rates. This policy eventually controlled inflation but caused a severe recession in the early 1980s.
Wage-Price Spirals:

High inflation led to higher wage demands, increasing production costs for businesses. Businesses passed these costs onto consumers, creating a cycle of wage and price increases.
Global Economic Conditions:

The breakdown of the Bretton Woods system in 1971, which ended the convertibility of the US dollar to gold, led to currency instability and contributed to inflation.
Fiscal Policy and Government Spending:

Government spending, particularly related to the Vietnam War and Great Society programs, increased the federal budget deficit, adding to inflationary pressures.
Supply-Side Constraints:

Reduced productivity growth and increased raw material costs, beyond just oil, contributed to the inflationary environment.


<iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=1o1Dx&width=900&height=525" scrolling="no" frameborder="0" style="overflow:hidden; width:900px; height:525px;" allowTransparency="true" loading="lazy"></iframe>
