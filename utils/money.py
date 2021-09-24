from decimal import Decimal

gold = Decimal(1)
silver = gold / 10
copper = silver / 10
platinum = gold * 10

currencies_text = ["CP", "SP", "GP", "PP"]
currencies_HTML = [
    "<span class='cp'>CP</span>",
    "<span class='sp'>SP</span>",
    "<span class='gp'>GP</span>",
    "<span class='pp'>PP</span>"
]

use_platinum = False


def digitize(n):
    digits = []
    i = 0
    if n == 0:
        return [0]
    while n:
        i += 1
        if i > (3 if use_platinum else 2):
            digits.append(n)
            return digits
        n, d = divmod(n, 10)
        digits.append(d)
    return digits


def format_money(money: Decimal, html=False) -> str:
    if not money:
        return ""
    currencies = currencies_HTML if html else currencies_text
    output = []
    cp = round(money / copper, ndigits=0)

    for i, value in enumerate(digitize(cp)):
        if value:
            output.append(str(value) + " " + currencies[i])
    return " ".join(reversed(output))
