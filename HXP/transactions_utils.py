# utils/transaction_utils.py
from xrpl.models.transactions import Payment
from xrpl.transaction import safe_sign_and_submit_transaction

def distribute_rewards(wallet, rewards, client):
    """Distribute XRP rewards to token holders."""
    for holder, reward in rewards.items():
        payment_tx = Payment(
            account=wallet.classic_address,
            destination=holder,
            amount=str(int(reward * 1000000)),  # XRP to drops
        )
        response = safe_sign_and_submit_transaction(payment_tx, wallet, client)
        print(f"Sent {reward:.2f} XRP to {holder}: {response}")
