# Crawling Notes
Notes used for writing a crawler for financial news sites in order to avoid filtering plain text for stock symbols...

## Site: marketwatch.com

```
<meta name="news_keywords" content="Category,US:SYMBOL" />
```

#### Example

```
<meta name="news_keywords" content="Software,US:ORCL,US:GOOG,US:GOOGL,US:AMZN,US:MSFT,US:SAP,US:DJIA,US:SPX,US:COMP" />
```

## Site: investopedia.com

```
<meta name="sailthru.date" content="..." /><meta name="sailthru.title" content="..." /><meta property="emailtickers" content="SYMBOL" /><meta name="emailt1" content="..." />	
```

#### Example
```
<meta name="sailthru.date" content="2020-01-29T16:45:57.578Z" /><meta name="sailthru.title" content="What Makes Apple So Valuable?" /><meta property="emailtickers" content="AAPL" /><meta name="emailt1" content="Investing" />	
```

