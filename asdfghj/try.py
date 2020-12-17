# User Define Exception

class BalanceException(Exception):
	pass

def checkbalance():
	money=10000
	withdraw = 8000
	try:
		balance = money-withdraw
		if(balance<=2000):
			raise BalanceException('Insufficient Balance')
		print(balance)
	except BalanceException as be:
		print(be)


checkbalance()