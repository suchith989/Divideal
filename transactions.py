import sqlite3

class transact:

	def get_connection(self):
		connection = sqlite3.connect("database.db")
		return connection

	def update_items(self,transaction_details,des,pot_id):
		conn = self.get_connection()
		curr = conn.cursor()
		item_id = 0
		for detail in transaction_details:
			if detail[0] == "ADD":
				curr.execute(" INSERT INTO transactions (pot_id,description,amount,paidby) VALUES(?,?,?,?)",(pot_id,des,detail[2],detail[1]))
				item_id = curr.execute("SELECT t_id FROM transactions WHERE description = ? and pot_id = ?",(des,pot_id,)).fetchone()
			elif detail[0] == "DEDUCT":
				curr.execute("INSERT INTO consumers (transaction_id,consumer_name,amount) VALUES(?,?,?)",(item_id[0],detail[1],detail[2]))
		conn.commit()
		conn.close()

