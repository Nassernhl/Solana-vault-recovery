# utils/scanner.py

from solana.rpc.api import Client
from solana.publickey import PublicKey

def scan_program_accounts(client: Client, program_id: str):
    print(f"🔍 البحث عن حسابات تحت البرنامج {program_id} ...")
    try:
        res = client.get_program_accounts(PublicKey(program_id))
        return res['result']
    except Exception as e:
        print("❌ خطأ:", e)
        return []
