from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    cedula=''
    nombres=''
    mesActual=''
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    
    corriente = CuentaCorriente()
    ahorros = CuentaAhorros()
    cdt = CDT()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    