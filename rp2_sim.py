def asm_pio(*args, **kwargs):
    """ 
        Es un decarador padre en el cual se reciben los argumentos que se guardan en listas,
        *args: argumentos que no tiene asignacion variable
        **kawrgs: argumentos que tiene asignacion variable=asignacion
    """
    def decorador(programa):
        """ 
            Es un decarador hijo en el cual se reciben la funcion a modificar en el parametro de programa.
        """
        def compilador():
            """
                Funcion que se ejecuta en la funcion que recibida en el decorador hijo
            """
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
    """ Decorador de la funcion recibida en el parametro fun_inst """
    def decoracion_instr(self,*args, **kwargs):
        """ Funcion que no hace nada, solamente llama a fun_inst y le envia todo tal cual """
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
        """
            Contructor de la clase StateMachine, se iniciala con estos parametros
            id_: id de la maquina a usar
            progra: programa a ejecutar en la clase de StateMachine
            freq: frecuencia de la maquina de estado
            **kwargs: argumentos en una lista   
            Este contructor ejecutar el programa enviado en program,
            imprime las instrucciones leidas que llegan mediante el parametro **kwargs, 
            resetea la variable sm_inciandose, que indica el id de la maquina de estado que se esta ejecutando,
            asigna en el arreglo de fsms en la posicion del id_ la StateMachine
        """
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
      
        
  def active(self, x=None):
    '''Esta rutina simula exclusivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        """
            Contructor de la clase nop (con el decorador @decorador_instr), el cual realiza lo siguiente:
            imprime el nombre de la clase que se le envia en el paramatero de self
            selecciona la variable globar sm_iniciandose y le agrega la clase de self 
        """
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def __getitem__(self,name):
        """
            Funcion donde se adquiere un item, aun no esta desarrollada 
        """
        #print('nop.__getattr__',name)
        pass
        
class set(nop):
    def __init__(self,*args, **kwargs):
        """
            Contructor de la clase set donde usa el init de la clase enviada mediante el parametro 
            usando el metodo super
        """
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
        """
            Contructor de la clase set donde usa el init de la clase enviada mediante el parametro 
            usando el metodo super
        """
        super().__init__(*args, **kwargs)
        pass 
  
class wrap(nop):
    def __init__(self,*args, **kwargs):
        """
            Contructor de la clase set donde usa el init de la clase enviada mediante el parametro 
            usando el metodo super
        """
        super().__init__(*args, **kwargs)
        pass 
         
         
