class Pile :
    '''classe Pile '''
    def __init__(self) :
        self.__pile = []
    
    def __repr__(self) :
        return self.__pile.__repr__()
    
    def vide(self) :
        ''' Pile est vide (booleen'''
        return len(self.__pile) == 0
    
    def empile(self, v) :
        '''Empile v sur la pile'''
        self.__pile.append(v)
    
    def depile(self) :
        '''Depile un element de la pile'''
        if (self.vide()) : raise IndexError('La pile est vide')
        return self.__pile.pop()

class File :
    '''classe File '''
    def __init__(self) :
        self.__file = []
    
    def __repr__(self) :
        return self.__file.__repr__()
    
    def vide(self) :
        ''' File est vide (booleen)'''
        return len(self.__file) == 0
    
    def enfile(self, v) :
        '''Emfile v sur la file'''
        self.__file.append(v)
    
    def defile(self) :
        '''Defile un element de la file'''
        if (self.vide()) : raise IndexError('La file est vide')
        return self.__file.pop(0)

