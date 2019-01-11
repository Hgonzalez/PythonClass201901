class CreditCardValidator():
	def __init__(self, raw_number):
		self.credit_card_number = raw_number
		self.card_length = self.cardlen()
		self.card_type = self.cardcomp()
		self.valid = False
		
	def cardlen(self):
		length_of_card = len(self.credit_card_number)
		if length_of_card == 15 or length_of_card == 16:
			self.card_length = True
		else:
			self.card_length = False
		return self.card_length
	
	def cardcomp(self):
		if self.card_length:
			if self.credit_card_number[0:2] in "51,52,53,54,55":
				self.card_type = "MasterCard"
				self.valid = True
			elif self.credit_card_number[0:2] in "34,37":
				self.card_type = "AMEX Card"
				self.valid = True
			elif self.credit_card_number[0:4] == "6011":
				self.card_type = "Discover Card"
				self.valid = True
			elif self.credit_card_number[0] == "4":
				self.card_type = "Visa Card"
				self.valid = True
			else:
				self.card_type = "Not Valid"
				self.valid = False
		else:
			self.card_type = "Not Valid"
			self.valid = False
		return self.card_type
	
	def validation(self):
		luhn_part_one = credit_card_number[-2::-2]
		doubled_list = []
		every_other_number = []
		totals =[]
		for i in luhn_part_one:
			if i > 9:
				doubled_list.append(int(i)*2)
		for i in doubled_list:
			if i > 9:
				i -= 9
				totals.append(i)
			else:
				totals.append(i)
		c2 = self.credit_card_number[-1::-2]
		for i in c2:
			totals.append(int(i))
		
		finished = sum(totals)%10
		if total == 0:
			self.valid = True
		else:
			self.valid = False
		return self.valid
			
creditcard = CreditCardValidator('601105371107579'
print(creditcard.valid)
print(creditcard.card_type)		