# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""Mini Project 1.
"""

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium", sql_output="polars")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mini Project 1

    Your choice of option, what each one asks for, the due date and how it is graded are on the Mini Project 1 page of the course site, linked from the calendar. This notebook is the shape to build it in. Keep the headings, and replace each line in italics with your own.

    Save it in your course repository as `projects/mp1/<your-tool>.py`, named for what it does, such as `loan-schedule.py`, and open it with `uv run marimo edit`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. The Question

    *Who would use this, and what decision does it help them make? Two or three sentences, in words somebody outside this course would understand.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An investor with limited funds who wants a diversified portfolio would want to know how to weigh their holdings properly. If they don't know, their money may be invested way more in one stock compared to the other based on share price changes and the weight applied to that specific stock.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. My Plan Before AI

    *Before you ask your agent anything, write how you would solve it: the steps, in order, in plain words, in five lines or more. Then answer these two questions:*

    - *What does your loop carry from one step to the next, the way a running total carries its sum?*
    - *Which check will you use in section 6, and which two numbers should agree?*

    *Commit this notebook with the message `mp1: plan before AI`.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Part C. Rebalancing the Portfolio
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    My goal is to ensure that the sum of all stock's shares multiplied by their prices is less than or equal to $5000. My goal is also to find out what share prices should be based on my target weights. I will first run a for loop where I will determine each stock's holdings by multiplying its shares by the price, or the holding value, and then getting the sum of all of the holding values to get the total portfolio value. Then, I will add 5000 to the total portfolio value.

    Next, I will multiply this new total portfolio value (current value + $5000) by each stock's target weight to determine the target dollar amount that should be allocated to that stock.

    Once I have the target dollar amount for each stock, I will divide it by the current share price of that stock to determine the target number of shares I should hold.

    Finally, I will compare the target number of shares to the number of shares I currently hold to determine how many shares I need to buy or sell in order to reach my target allocation, making sure that the total cost of any purchases does not exceed the $5000 I have available to invest.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Inputs

    Every number the project starts from goes in the cell below, and nowhere else, so that changing one input changes every result after it.

    Copy in the default inputs for your option from the Mini Project 1 page. If you chose D, your own option, type your data in here, or ask your agent to generate it with `faker`. The required part reads no file.
    """)
    return


@app.cell
def _():
    holdings = [
        ("AAPL", 100, 173.93),
        ("MSFT", 50, 319.53),
        ("GOOG", 80, 131.36),
        ("AMZN", 200, 129.33),
        ("NVDA", 20, 410.17),
        ("TSLA", 150, 255.70),
    ]
    cash = 5000.00
    target_weights = {"AAPL": 0.20, "MSFT": 0.20, "GOOG": 0.15,
                      "AMZN": 0.15, "NVDA": 0.15, "TSLA": 0.15}
    return cash, holdings, target_weights


@app.cell
def _():
    # Your inputs.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. The Work

    Add as many cells as you need. Try each step yourself before you ask your agent, and commit as you go.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    My work before using the agent
    """)
    return


@app.cell
def _(holdings):
    for _ticker, _shares, _price in holdings:
        _portfolio_value = 0
        _value = _shares * _price
        if _value > 0:
            _portfolio_value = _value + _portfolio_value
    _portfolio_value
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. The Answer

    *A table of your results in the cell below, printed with `print` and f-strings, then one sentence here that answers the question in section 1, with the number in it.*
    """)
    return


@app.cell
def _(holdings):
    portfolio_value = 0
    for ticker, shares, price in holdings:
        value = shares * price
        portfolio_value = portfolio_value + value
    portfolio_value
    return (portfolio_value,)


@app.cell
def _(portfolio_value):
    cash_included = portfolio_value + 5000
    print(f"${cash_included}")
    return (cash_included,)


@app.cell
def _(holdings, portfolio_value):
    for _ticker, _shares, _price in holdings:
        _value = _shares * _price
        _original_weight = _value / portfolio_value
        print(f"{_ticker}: {_original_weight:.2%}")
    return


@app.cell
def _(holdings, portfolio_value, target_weights):
    for _ticker, _shares, _price in holdings:
        _value = _shares * _price
        _original_weight = _value / portfolio_value
        _target_weight = target_weights[_ticker]
        _weight_change = (_target_weight - _original_weight) * 100
        print(f"{_ticker}: {_weight_change:.2f} percentage points")
    return


@app.cell
def _(cash_included, target_weights):
    for stock, target in target_weights.items():
        target_amount = cash_included * target
        print(f"{stock}: ${target_amount:.2f}")
    return


@app.cell
def _(cash_included, holdings, target_weights):
    for _ticker, _shares, _price in holdings:
        _weight = target_weights[_ticker]
        _target_amount = cash_included * _weight
        target_holdings = int(_target_amount / _price)
        print(f"{_ticker}: {target_holdings} target shares")
    return


@app.cell
def _(cash_included, holdings, target_weights):
    for _ticker, _shares, _price in holdings:
        _weight = target_weights[_ticker]
        _target_amount = cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _difference = _shares - _target_holdings
        if _difference > 0:
            _label = "sell"
        elif _difference < 0:
            _label = "buy"
        print(f"{_ticker}: {_label} {abs(_difference)}")
    return


@app.cell
def _(cash_included, holdings, new_cash, target_weights):
    _total_value_after = 0
    for _ticker, _shares, _price in holdings:
        _weight = target_weights[_ticker]
        _target_amount = cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _value_after = _target_holdings * _price
        _total_value_after = _total_value_after + _value_after

    _total_with_cash = _total_value_after + new_cash

    rebalance_table = []
    for _ticker, _shares, _price in holdings:
        _weight = target_weights[_ticker]
        _target_amount = cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _shares_change = _target_holdings - _shares
        _value_after = _target_holdings * _price
        _weight_after = (_value_after / _total_with_cash) * 100
        rebalance_table.append({
            "Ticker": _ticker,
            "Shares Now": _shares,
            "Shares At Target": _target_holdings,
            "Shares To Buy/Sell": _shares_change,
            "Value After": round(_value_after, 2),
            "Weight After (%)": round(_weight_after, 2),
        })
    rebalance_table
    return


@app.cell
def _(cash_included, holdings, target_weights):
    _cash_from_trades = 0
    for _ticker, _shares, _price in holdings:
        _weight = target_weights[_ticker]
        _target_amount = cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _difference = _shares - _target_holdings
        _cash_from_trades = _cash_from_trades + (_difference * _price)
    new_cash = _cash_from_trades + 5000
    print(f"${new_cash:.2f}")
    return (new_cash,)


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. How I Know These Numbers Are Right

    *At least one check that reaches a result a second, independent way. Name what you compared and what came out.*
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Working With the Agent

    *Pick one piece of AI output you did not accept as-is. What did it give you, what did you change, and how did you know? Point to the commit or the cell.*

    *If the agent got it right the first time: what did you do to verify that?*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Going Further

    *Take at least one step past the main task, in any direction, and use your agent as much as you like. It does not have to work. State what you tried, what you found, and where it is in this notebook.*
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(cash, target_weights):
    new_prices = [
        ("AAPL", 100, 343.46),
        ("MSFT", 50, 529.05),
        ("GOOG", 80, 336.91),
        ("AMZN", 200, 250.00),
        ("NVDA", 20, 214.13),
        ("TSLA", 150, 354.72),
    ]

    _new_portfolio_value = 0
    for _ticker, _shares, _price in new_prices:
        _value = _shares * _price
        _new_portfolio_value = _new_portfolio_value + _value

    _new_cash_included = _new_portfolio_value + cash

    _new_total_value_after = 0
    for _ticker, _shares, _price in new_prices:
        _weight = target_weights[_ticker]
        _target_amount = _new_cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _value_after = _target_holdings * _price
        _new_total_value_after = _new_total_value_after + _value_after

    _new_cash_from_trades = 0
    for _ticker, _shares, _price in new_prices:
        _weight = target_weights[_ticker]
        _target_amount = _new_cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _difference = _shares - _target_holdings
        _new_cash_from_trades = _new_cash_from_trades + (_difference * _price)
    _new_cash_after = _new_cash_from_trades + cash

    _new_total_with_cash = _new_total_value_after + _new_cash_after

    new_price_table = []
    for _ticker, _shares, _price in new_prices:
        _weight = target_weights[_ticker]
        _target_amount = _new_cash_included * _weight
        _target_holdings = int(_target_amount / _price)
        _shares_change = _target_holdings - _shares
        _value_after = _target_holdings * _price
        _weight_after = (_value_after / _new_total_with_cash) * 100
        new_price_table.append({
            "Ticker": _ticker,
            "Shares Now": _shares,
            "Shares At Target": _target_holdings,
            "Shares To Buy/Sell": _shares_change,
            "Value After": round(_value_after, 2),
            "Weight After (%)": round(_weight_after, 2),
        })
    new_price_table
    return


if __name__ == "__main__":
    app.run()
