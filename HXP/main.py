# main.py
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import TrustSet
from xrpl.transaction import safe_sign_and_autofill_transaction, send_reliable_submission
from xrpl.utils import xrp_to_drops
import config

# Connect to the XRP Ledger Testnet
client = JsonRpcClient(config.XRPL_NETWORK)

# Set up the issuer wallet
issuer_wallet = Wallet(config.ISSUER_SEED, 0)

# Define the HXRP token
hxrp_currency = config.HXRP_CURRENCY  # Currency code in HEX (e.g., '58485250' for HXRP)
hxrp_limit = "1000000000"  # Total supply: 1 billion tokens


def issue_token():
    try:
        # Create a TrustSet transaction
        trust_set_tx = TrustSet(
            account=issuer_wallet.classic_address,
            limit_amount={
                "currency": hxrp_currency,
                "issuer": issuer_wallet.classic_address,
                "value": hxrp_limit,
            },
        )

        # Autofill transaction details (e.g., fee, sequence number)
        signed_tx = safe_sign_and_autofill_transaction(trust_set_tx, issuer_wallet, client)

        # Submit the transaction
        response = send_reliable_submission(signed_tx, client)

        print(f"HXRP Token Creation Response: {response.result}")
    except Exception as e:
        print(f"Error during token issuance: {e}")


if __name__ == "__main__":
    issue_token()

