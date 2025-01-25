# utils/ledger_utils.py
from xrpl.models.requests import AccountLines

def get_token_holders(client, issuer_address, currency_code):
    """Fetch all accounts holding the token."""
    holders = {}
    response = client.request(AccountLines(account=issuer_address))
    for line in response.result["lines"]:
        if line["currency"] == currency_code:
            holders[line["account"]] = float(line["balance"])
    return holders
