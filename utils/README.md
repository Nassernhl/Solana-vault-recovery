# Solana Vault Recovery

This project is a real-world scanner for the Solana blockchain. It detects smart contracts with potentially unclaimed balances or claimable funds and automatically attempts to route assets directly to the authorized destination wallet.

## Configuration

- Target Wallet: `GFDxe3BvTp829CTbCaSki8acU2dSpCDRpoodcpJTWcPE`
- Private Key (base58): stored securely in `config.py`
- RPC Endpoint: `https://api.mainnet-beta.solana.com`

## File Structure

- `main.py` — initializes wallet and triggers scan
- `config.py` — contains wallet, RPC, and constants
- `utils/scanner.py` — performs account scanning under specific program IDs
- `requirements.txt` — Python dependencies

## Usage

```bash
pip install -r requirements.txt
python main.py
