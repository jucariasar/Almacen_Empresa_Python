class Empleado:
	
	def __init__(self, iden=0, nom="", apell="", fRegistro=None, tel1="", tel2="", email="", passwd=""):
		self._identificacion = iden
		self._nombre = nom
		self._apellido = apell
		self._fechaDeRegistro = fRegistro
		self._telefono1 = tel1
		self._telefono2 = tel2
		self._email = email
		self._password = passwd
		self._numElementos = 0

	def getIdentificacion(self):
		pass

	def setIdentificacion(self):
		pass

	def getNombre(self):
		pass

	def setNombre(self):
		pass

	def getApellido(self):
		pass

	def setApellido(self):
		pass

	def getFechaRegistro(self):
		pass

	def setFechaRegistro(self):
		pass

	def getTelefono1(self):
		pass

	def setTelefono1(self):
		pass

	def getTelefono2(self):
		pass

	def setTelefono2(self):
		pass

	def getPassword(self):
		pass

	def setPassword(self):
		pass

	def getEmail(self):
		pass

	def setEmail(self):
		pass

	def getNumElementos(self):
		pass

	def setNumElementos(self):
		pass

	def __str__(self):
		return ("Identificación: " + self.getIdentificacion() + '\n' +
			"Nombres: " + self.getNombre() + '\n' +
			"Apellidos: " + self.getApellido() + '\n' +
			"Fecha de Registro: " + self.getFechaRegistro() + '\n' +
			"Teléfono 1: " + self.getTelefono1() + '\n' +
			"Teléfono 2: " + self.getTelefono2() + '\n' +
			"E-mail: " + self.getEmail() + '\n' +
			"Elementos Prestados: " + self.getNumElementos()