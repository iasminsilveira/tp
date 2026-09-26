# TP POO - Banco Digital

Trabajo práctico grupal de Programación Orientada a Objetos.

## Integrantes
- Rocio Fissore
- Iasmin Silveira
- Alfonsina Ray
- Constanza Tacconi

## Cómo ejecutarlo
python main.py

## Preguntas de cierre

**1. ¿Por qué usamos `_saldo` con guion bajo en lugar de `saldo` a secas?**

Usamos `_saldo` para aplicar el principio de encapsulamiento. En Python, el guion bajo es una convención que indica que el atributo es de uso interno de la clase y no debe modificarse directamente desde afuera. De esta manera, el saldo solo se modifica a través de los métodos `depositar` y `extraer`, que validan que los montos sean positivos y que haya fondos suficientes. Además, mediante el decorador `@property` exponemos el saldo únicamente para lectura (`cuenta.saldo`), sin permitir asignarle un valor directamente. Cabe aclarar que el guion bajo no bloquea técnicamente el acceso, sino que funciona como un acuerdo entre programadores.

**2. ¿Qué ventaja tuvo usar `super().__init__()`?**

`super().__init__()` permite llamar al constructor de la clase madre (`CuentaBancaria`) desde las clases hijas. La principal ventaja es la reutilización de código: la inicialización del titular, el número y el saldo se escribe una sola vez en la clase madre, y cada clase hija solo agrega su atributo propio (`tasa_interes` en `CajaDeAhorro` y `limite_descubierto` en `CuentaCorriente`). Esto evita repetir código, reduce la posibilidad de errores y facilita el mantenimiento: si en el futuro se agrega un atributo común a todas las cuentas, basta con modificar la clase madre para que todas las hijas lo hereden.

**3. ¿Por qué `Banco.transferir` funciona sin saber qué tipo de cuenta recibe?**

Por polimorfismo. El método `transferir` solo llama a `extraer` en la cuenta de origen y a `depositar` en la de destino, métodos que todas las cuentas poseen. Cada objeto ejecuta su propia versión del método según su tipo: `CajaDeAhorro` utiliza el `extraer` heredado de `CuentaBancaria`, que no permite saldo negativo, mientras que `CuentaCorriente` utiliza su versión sobrescrita, que permite quedar en descubierto hasta el límite establecido. Por lo tanto, `Banco` no necesita conocer el tipo de cuenta, y se podrían agregar nuevos tipos de cuenta sin modificar la clase `Banco`, siempre que implementen los métodos `extraer` y `depositar`.