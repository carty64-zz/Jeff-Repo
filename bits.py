from coinbase.wallet.client import Client

SANDBOX_URL = 'https://api.sandbox.coinbase.com'
client = Client('XkeNVpuPu8gg6ooT','AzOlNhddoZQaKjaEw2QXEjaO1I8Gqpgs',base_api_uri=SANDBOX_URL)

accounts = client.get_accounts()
wallets = []

for index,account in enumerate(accounts.data):
  name = account['name']
  balance = account.balance
  wallets.append(name)
  print "%i) %s:  %s" % (index+1, name, balance)

src = int(raw_input("From account? "))-1
dest = int(raw_input("To account? "))-1
amount = raw_input("Amount: ")
note = raw_input("Transaction Note (optional): ")

src_id = accounts[src]['id']
dest_id = accounts[dest]['id']

tx = client.transfer_money(src_id,to=dest_id,amount=amount,currency='BTC',description=note)

print tx


#print wallets[src]
#print amount
#print wallets[dest]

#try:
#  while(1):
#first = raw_input('From acct: 1)%s', wallets)

#for account in accounts.data:
#  print account.name


#for account in accounts.data:
#  balance = account.balance
#  wallet_id = account.id
#  print "%s: %s %s (%s)" % (account.name, balance.amount, balance.currency, wallet_id)
#  print account.get_transactions()

#print accounts.data
