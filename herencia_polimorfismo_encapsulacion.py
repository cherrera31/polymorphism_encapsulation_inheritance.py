class Empleado:
    compania = "corporacionCosa"
    aumento = 1.05

    def __init__(self,nombre,idEmp,rol="Oficinista",salario=18_000):
        self.nombre = nombre
        self.idEmp = idEmp
        self.rol = rol
        self._salario = salario

    def gererarCorreo(self):
        correo = self.nombre+"@"+Empleado.compania+".com"
        return correo
    
    def getSalario(self): #obtiene valor privado
        return self._salario
    
    def getSalario(self, nuevoSalario):#modifica el valor privado
        self._salario = nuevoSalario

    def __str__(self):
        return f"Hola,soy {self.nombre}con id{self.idEmp}"
        def aumento_salario(self):
            self._salario = int(self._salario*self.aumento)

class Ingeniero(Empleado):
    def __init__(self,idEmp, rol="ingeniero",especialidad="IT"):
        super().__init__(nombre,idEmp,rol)
        self.especialidad = especialidad 

    def generarCorreo(self): #Polimorfismo
        correo = self.rol+self.nombre+"@"+Empleado.compania+".com"   
        return correo
   # print(help(Ingeniero))
    
class Gerente(Empleado):
    def __init__(self, nombre, idEmp, rol="Gerente", empleados=None ):
        super().__init__(nombre, idEmp, rol)
        if empleados is None:
            self.empleados = []
        else:
            self.empleados = empleados
    
    def contratar_emp(self,emp):
        if emp in self.empleados: 
            self.empleados.append(emp)

    def quitar_emp(self,emp):
        if emp in self.empleados: 
            self.empleados.remove(emp)
    
    def imprime_emp(self):
        for emp in self.empleados:
            print("-->", emp)
#Main
gnr = Gerente("AMLO", 666, [emp2])
print(gnr.imprime_emp)


#Main
#emp1 = Empleado("Juan",850)
emp2 = Ingeniero("Ana", 123)
#emp1.nombre = "Juana"
#correo1 = emp1.generarCorreo()
#correo2 = emp2.generarCorreo()

#print(emp1, correo1, emp1.rol, emp2, correo2. emp2.rol)
#emp1.setSalario(20_000)
#print(emp1, emp1.getSalario())
#print(emp2.getSalario())
