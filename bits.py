from coinbase.wallet.client import Client
import sys

SANDBOX_URL = 'https://api.sandbox.coinbase.com'
client = Client('XkeNVpuPu8gg6ooT','AzOlNhddoZQaKjaEw2QXEjaO1I8Gqpgs',base_api_uri=SANDBOX_URL)

accounts = client.get_accounts()
price = client.get_buy_price(currency='USD')
price = float(price.amount)

#print accounts.data

for index,account in enumerate(accounts.data):
  if account['currency'] == 'USD':
    continue    
  name = account['name']
  balance = account.balance.amount
  usd_value = float(balance) * price
  print "%i) %s: %s %s (%.2f USD)" % (index+1, name, balance, account.balance.currency, round(usd_value,2))  

src = int(raw_input("\nFrom account: "))-1
dest = int(raw_input("To account: "))-1
amount = raw_input("Amount: ")

#def transaction():
if float(amount) > float(accounts[src]['balance']['amount']):
  sys.exit("\nYou don't have that much bitcoin.")

note = raw_input("Transaction Note (optional): ")

src_id = accounts[src]['id']
dest_id = accounts[dest]['id']

print "\nAbout to send\n%s BTC from %s to %s\n" % (amount, accounts[src]['name'], accounts[dest]['name'])
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
print "%s: %.8f %s (%.2f USD)" % (accounts[src]['name'], new_src,accounts[src]['balance']['currency'],price*new_src)
print "%s: %.8f %s (%.2f USD)" % (accounts[dest]['name'], new_dest,accounts[dest]['balance']['currency'],price*new_dest)

