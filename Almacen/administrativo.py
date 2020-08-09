
class Administrativo(Empleado):
	roll = {'1':'Oficina','2':'Almacen'}

	def __init__(self, iden=0, nom="", apell="", fRegistro=None, tel1="", tel2="", email="", passwd="", elementos, r):
		super().__init__(iden, nom, apell, fRegistro, tel1, tel2, email, passwd, elementos)
		self._roll = r

	def getRoll(self):
		pass

	def setRoll(self):
		pass

	def __str__(self):
		return (super().__str__() + '\n' + "Roll: " + self.getRoll())