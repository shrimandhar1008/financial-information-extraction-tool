from django.shortcuts import render
import openai
from secret_key import openai_key
import json
import pandas as pd
openai.api_key = openai_key



# Create your views here.
def exract_financial_data(text):
    prompt = get_prompt_financial() + text

    response  = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
    messages=[
        
            {"role": "user", "content": prompt},
        
        ]
    )
    content = response['choices'][0]['message']['content']
    try:
        return pd.DataFrame(json.loads(content).items(),columns=['Measure','Value'])
    except Exception:
        pass
    return pd.DataFrame({"Measure":['Company Name','Stock Symbol','Revenue','Net Income','EPS'],
        "Value":["","","","",""]})


def get_prompt_financial():
    return '''Please retrieve company name, revenue, net income and earnings per share
    (a.k.a. EPS) from the following news article. If you can't find the information from 
    this article then return "". Do not make things up.
    Then retrieve a stock symbol corresponding to that company. For this you can use
    you general knowledge (It doesn't have to be from this article). Always return your 
    response as a valid JSON string. The format of that string should be this,
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    '''
# exract_financial_data('''Tesla (TSLA) stock is slipping after the bell as the electric-vehicle maker reported slight revenue and profit misses and gross margin that dipped below 20% to 19.3% as the cost of recent price cuts hit profitability.

# For the quarter, Tesla reported Q1 revenue of $23.33 billion, slightly below Street estimates of $23.35 billion, with Q1 adjusted EPS coming in at $0.85, below Street estimates of $0.86. That revenue figure for Q1 represents a slight dip from the $24.32 billion Tesla reported in Q4, but still 24% higher than a year ago.

# On the profitability end, Tesla reported adjusted net income of $2.9 billion, less than the $3.03 billion estimated by the Street, and a billion less than last quarter and $700 million less than a year ago. With revenue staying flat-ish and profit dipping, the effects of margin compression could be at play here.''')
    
    
