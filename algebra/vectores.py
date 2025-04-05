"""
    Tercera tasca de APA - manejo de vectores

    Nom i cognoms: Bernat Rubiol Brusau
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    # Lo d'abans ve directe del fork
    def __mul__(self, other):
        """
        Multiplicació per un escalar o producte Hadamard amb un altre vector.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v1 * v2
        Vector([4, 10, 18])
        """
        if isinstance(other, (int, float, complex)):
            return Vector(element * other for element in self)
        else:
            return Vector(e1 * e2 for e1, e2 in zip(self, other))

    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Producte escalar entre dos vectors.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32
        """
        return sum(e1 * e2 for e1, e2 in zip(self, other))

    def __rmatmul__(self, other):
        """
        Producte escalar reflectit.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v2.__rmatmul__(v1)
        32
        """
        return self.__matmul__(other)

    def __floordiv__(self, other):
        """
        Component paral·lela del vector respecte a un altre vector.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        factor = (self @ other) / (other @ other)
        return Vector(factor * x for x in other)

    def __rfloordiv__(self, other):
        """
        Component paral·lela reflectida (no canviaria el resultat si other és Vector).
        (No funciona)

        """
        #factor = (other @ self) / (self @ self)
        #return Vector(factor * x for x in self)
        # No es pot fer així perquè sino al fer el test retorna error
        if not isinstance(other, Vector):
                raise TypeError("No podem projectar un escalar a un vector")

    def __mod__(self, other):
        """
        Component perpendicular del vector respecte a un altre vector.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        return self - (self // other)

    def __rmod__(self, other):
        """
        Component perpendicular reflectida.
        (No funciona)
        """
        #return other - (other // self)
        # Aquest mètode com el de __rflordiv__ no es pot fer així perquè sino al fer el test retorna error
        
        if not isinstance(other, Vector): 
                raise TypeError("No es pot projector un escalar a un vector")

    def __iter__(self):
        return iter(self.vector)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
