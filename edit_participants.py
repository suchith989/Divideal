import sqlite3

class database_entry:

	def get_connection(self):
		connection = sqlite3.connect("database.db")
		
		return connection
	
	def add_single_participant(self,pot_id,user_name,email):
		conn = self.get_connection()
		curr = conn.cursor()
		curr.execute("INSERT INTO participants (pot_id,participant_name,mail,paid,consumed,net) VALUES(?,?,?,?,?,?)",(pot_id,user_name,email,0,0,0))
		user_id = curr.execute("SELECT uid FROM participants WHERE pot_id = ? and participant_name=?",(pot_id,user_name)).fetchone()
		return user_id[0]

	def get_every_participant(self,pot_id):
		conn = self.get_connection()
		curr = conn.cursor()
		users = curr.execute("SELECT uid,participant_name,mail FROM participants WHERE pot_id = ?",(pot_id,)).fetchall()
		return users

	def add_every_participant(self,pot_id,userMap):
		conn = self.get_connection()
		curr = conn.cursor()
		for user in userMap:
			curr.execute("INSERT INTO participants(pot_id,participant_name,paid,consumed,net) VALUES(?,?,?,?,?)",(pot_id,user,'0','0','0'))
		conn.commit()
		conn.close()

	def edit_entry(self,trans,pot_id):
		conn = self.get_connection()
		cur = conn.cursor()
		query = """SELECT "1"
WHERE EXISTS(SELECT 1 FROM participants 
       WHERE participant_name = ? and pot_id= ?)"""
		check_cond = cur.execute(query,(trans[1],pot_id)).fetchone()
		if trans[0]=="ADD":
			if check_cond != None:
				values = cur.execute("SELECT * FROM participants WHERE participant_name = ? and pot_id = ?",(trans[1],pot_id,)).fetchone()
				#print(values)
				cur.execute("UPDATE participants SET paid= ?, net= ? WHERE participant_name= ? and pot_id = ?",(str(int(values[2])+int(trans[2])),str(int(values[2])+int(trans[2])-int(values[3])),trans[1],pot_id,))
			else:
				cur.execute("INSERT INTO participants (pot_id,participant_name, paid, consumed, net) VALUES (?,?, ?, ?, ?)",(pot_id,trans[1],trans[2],0,trans[2]))

		elif trans[0] == "DEDUCT":
			if check_cond != None:
				values = cur.execute("SELECT * FROM participants WHERE participant_name = ? and pot_id = ?",(trans[1],pot_id,)).fetchone()
				#print(values)
				cur.execute("UPDATE participants SET consumed= ?, net= ? WHERE participant_name= ? and pot_id = ?",(str(int(values[3])+int(trans[2])),str(int(values[2])-int(trans[2])-int(values[3])),trans[1],pot_id,))
			else:
				cur.execute("INSERT INTO participants (pot_id,participant_name, paid, consumed, net) VALUES (?,?, ?, ?, ?)",(pot_id,trans[1],'0',trans[2],-trans[2]))
		conn.commit()
		conn.close()



if __name__ == "__main__":
	test = database_entry()

	test.edit_entry("SUCHITH","1000","ADD")

			