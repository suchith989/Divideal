import sqlite3

class balancesheet:

	def get_connection(self):
		connection = sqlite3.connect("database.db")
		
		return connection

	def update_balance_sheet(self,balance_sheet,pot_id):
		conn = self.get_connection()
		curr = conn.cursor()
		query = """SELECT "1"
WHERE EXISTS(SELECT 1 FROM settlement 
       WHERE payee_name = ? and receiver_name = ? and pot_id = ?)"""
		

		for receiver in balance_sheet:
			for payer in balance_sheet[receiver]:

				if balance_sheet[receiver][payer] >= 0:
					#add into sql table
					check_cond = curr.execute(query,(payer,receiver,pot_id,)).fetchone()
					print(check_cond)
					if check_cond != None:
						values = curr.execute("SELECT * FROM settlement WHERE payee_name = ? and receiver_name= ?",(payer,receiver,)).fetchone()
						curr.execute("UPDATE settlement SET  amount= ? WHERE payee_name= ? and receiver_name= ?",(balance_sheet[receiver][payer],payer,receiver,))
					else:
						curr.execute("INSERT INTO settlement (pot_id,payee_name,amount,receiver_name) VALUES(?, ?,?,?)",(pot_id,payer,balance_sheet[receiver][payer],receiver))
		conn.commit()
		conn.close()

	def get_balance_sheet(self,pot_id):
		conn = self.get_connection()
		curr = conn.cursor()

		values = curr.execute("SELECT payee_name,amount,receiver_name FROM settlement WHERE pot_id= ?",(pot_id,)).fetchall()
		print(values)
		b_sheet = {}
		key_values = curr.execute("SELECT participant_name FROM participants WHERE pot_id = ?",(pot_id,)).fetchall()
		print(key_values)
		for key in key_values:
			b_sheet[key[0]] = {}

		for entry in values:
			payee = entry[0]
			amount = entry[1]
			receiver = entry[2]

			b_sheet[payee][receiver] = -amount
			b_sheet[receiver][payee] = amount
			# if payee in b_sheet.keys():
			# 	b_sheet[payee][receiver] = -amount
			# else:
			# 	b_sheet[payee] = { }
			# 	b_sheet[payee][receiver] = -amount
			# if receiver in b_sheet.keys():
			# 	b_sheet[receiver][payee] = amount
			# else:
			# 	b_sheet[receiver] = {}
			# 	b_sheet[receiver][payee] = amount

		conn.close()
		print(b_sheet)
		return b_sheet

