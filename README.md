# Linewipe
A simple screen/scanner of Crypto markets, was gonna build it for ASX listed equities but free API's for the stock market are like the teeth of golden geese. Idea changed a bit, will avoid any GUI aspects for a bit, focus on data parsing.

## An attempt to get the logic out of my head.
> I've found myself struggling quite a bit with actually thinking about how to implement many programmable ideas, but have been reading (on and off) some books on how to engineer a solution, I'll be writing down higher-level-than-pseudo-code instructions for how I see the program working.

Request CoinMarketCap API.
Parse the JSON for all ticker names.
Create an iterable data structure that holds the ticker names.
Create a count incrementor object that identifies number of tickers.
With the count_of object and data_struct of ticker names, iterate through the list.
Craft URL's with each ticker name.
Ensuring that calls are made at a frequency of 1req/6sec (to stay in line with API policies)...
Call the API for each ticker.
Parse the JSON data on arrival.
Put the parsed data into DB tables, preferably a time-series DB (this may change but I've heard for fin data, these are good).
Form a large database.
????
Profit

But in all seriousness, this is the flow I can see so far, naturally, this will be refactored into something a bit more illustrious, the intention is to build a screener that can provide adequate levels of detail for investment decisions, ie: Whether or not the asset is being actively developed, how it is going in the media, blah blah. I guess in reality it's Algorithmic trading. Or, a bad attempt at it.



