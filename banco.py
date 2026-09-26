class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self._cuentas = {}

    def agregar_cuenta(self, cuenta):
        if cuenta.numero in self._cuentas:
            raise ValueError(f"Ya existe la cuenta {cuenta.numero}")
        self._cuentas[cuenta.numero] = cuenta

    def buscar_cuenta(self, numero):
        return self._cuentas.get(numero)

    def transferir(self, numero_origen, numero_destino, monto):
        origen = self.buscar_cuenta(numero_origen)
        destino = self.buscar_cuenta(numero_destino)
        if origen is None or destino is None:
            raise ValueError("Cuenta de origen o destino inexistente")
        origen.extraer(monto)
        destino.depositar(monto)

    def total_depositado(self):
        total = 0
        for cuenta in self._cuentas.values():
            total += cuenta.saldo
        return total

    def listar_cuentas(self):
        print(f"--- {self.nombre} ---")
        for cuenta in self._cuentas.values():
            print(cuenta)