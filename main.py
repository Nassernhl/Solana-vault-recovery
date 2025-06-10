from solana.keypair import Keypair
from solana.rpc.api import Client
import base58
from config import PRIVATE_KEY_B58, TARGET_WALLET, RPC_URL

print("🚀 جاري الاتصال بشبكة سولانا...")

keypair = Keypair.from_secret_key(base58.b58decode(PRIVATE_KEY_B58))
client = Client(RPC_URL)

print("✅ تم تهيئة المحفظة:")
print("   عنواني:", keypair.public_key)
print("   الهدف:", TARGET_WALLET)

balance = client.get_balance(keypair.public_key)['result']['value'] / 1e9
print(f"💰 الرصيد الحالي: {balance} SOL")
