from coinbase.wallet.client import Client
import sys
import os

SANDBOX_URL = 'https://api.sandbox.coinbase.com'
API_KEY = os.environ["CB_API"]
API_SECRET = os.environ["CB_SECRET"]
client = Client(API_KEY,API_SECRET,base_api_uri=SANDBOX_URL)

accounts = client.get_accounts()
price = client.get_buy_price(currency='USD')
price = float(price.amount)

#print accounts.data
while 1:
  for index,account in enumerate(accounts.data):
    if account['currency'] == 'USD':
      continue    
    name = account['name']
    balance = account.balance.amount
    usd_value = float(balance) * price
    print "%i) %s: %s %s ($%.2f)" % (index+1, name, balance, account.balance.currency, round(usd_value,2))  

  src = int(raw_input("\nFrom account: "))-1
  dest = int(raw_input("To account: "))-1
  if src == dest:
    sys.exit("Source and destination cannot be the same")

  amount = raw_input("Amount: ")
  amount_usd = float(amount) * price
  #def transaction():
  if float(amount) > float(accounts[src]['balance']['amount']):
    sys.exit("\nYou don't have that much bitcoin.")

  note = raw_input("Transaction Note (optional): ")

  src_id = accounts[src]['id']
  dest_id = accounts[dest]['id']

  print "\nAbout to send\n%s BTC ($%.2f) from %s to %s\n" % (amount, amount_usd, accounts[src]['name'], accounts[dest]['name'])
  proceed = raw_input("Is this correct? Y/N: ")
  proceed = proceed.lower()

  if proceed == 'y':
    tx = client.transfer_money(src_id,to=dest_id,amount=amount,currency='BTC',description=note)
    print "Done!"
  else:
    sys.exit("User canceled")

  accounts = client.get_accounts()
  new_src = accounts[src]['balance']['amount']
  new_src = float(new_src)
  new_dest = accounts[dest]['balance']['amount']
  new_dest = float(new_dest)

  print "\nNew balances:"
  print "%s: %.8f %s ($%.2f)" % (accounts[src]['name'], new_src,accounts[src]['balance']['currency'],price*new_src)
  print "%s: %.8f %s ($%.2f)" % (accounts[dest]['name'], new_dest,accounts[dest]['balance']['currency'],price*new_dest)

  new_txn = raw_input("\nAnother transaction? Y/N: ")
  new_txn = new_txn.lower()

  if new_txn == 'n':
    sys.exit("All done.")
 
