import sqlite3
from balance_sheet import *

class pots:

	def get_connection(self):
		connection  = sqlite3.connect("database.db")
		return connection

	def get_pots(self):
		conn = self.get_connection()
		curr = conn.cursor()

		vals = curr.execute("SELECT p_id,pot_name FROM pots").fetchall()
		conn.close()
		return vals

	def set_pot(self,pot_name,pot_link):
		conn = self.get_connection()
		curr = conn.cursor()

		curr.execute("INSERT INTO pots (pot_name,pot_link) VALUES(?,?)",(pot_name,pot_link))
		conn.commit()
		conn.close()

	def get_potid(self,pot_name):
		conn = self.get_connection()
		curr = conn.cursor()

		val = curr.execute("SELECT p_id FROM pots WHERE pot_name = ?",(pot_name,)).fetchone()
		conn.close()
		return val


	def getbalance(self,pot_id):
		get = balancesheet()
		sheet = get.get_balance_sheet(pot_id)
		return sheet