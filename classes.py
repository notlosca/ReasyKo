####### classe giocatore  #######
class player:
    '''
    classe giocatore, avrà:
    - nome (colore)
    - numero di carri armati
    - stati conquistati
    - carte da usare
    - carta obiettivo
    Un giocatore deve perseguire il proprio obiettivo.
    Ad ogni turno aggiunge num_states/3 arrotondato per difetto di tank e li divide tra i suoi stati.
    Può conquistare uno o più territori, otterrà sempre e solamente una carta territorio.
    Infine, può effettuare uno spostamento di n tank in un territorio adiacente
    '''
    def __init__(self, name):
        self.name = name
        self.tank = 0
        self.states = None
        self.objective = None
        self.cards = None
    
    def add_tank(self, tanks:int):
        self.tank += tanks 
        
    def conquer(self, country:country):
        pass
        
####### classe carta territorio  #######

class card:
    '''
    Classe carta territorio.
    Viene pescata da un giocatore quando esso conquista almeno un nuovo territorio durante il turno.
    Può essere di 4 tipi:
    - Cannone
    - Fante
    - Cavaliere
    - Jolly
    Una combinazione di 3 carte uguali, 3 diverse (no jolly) o 2 uguali + 1 jolly 
    consente di riscattare un determinato numero di tank aggiuntivi a inizio turno.
    Inoltre, se le carte territorio utilizzate sono territori conquistati, 
    si ottengono +2 tank per ognun territorio che soddisfa la condizione.
    Se jolly non ha territorio/continente
    '''
    def __init__(self, country:str, type:str='cannon'):
        self.country = country
        self.type = type # va bene anche come jolly
        
####### classe carta obiettivo  #######

class objective:
    '''
    carta contenente l'obiettivo da raggiungere per ottenere la vittoria. 
    Ovvero, gli stati da conquistare
    '''
    def __init__(self, countries_to_conquer:list):
        self.countries_to_conquer = countries_to_conquer
    
####### classe stato  #######
    
class country:
    '''
    Uno stato ha un nome, un numero di punti e fa parte di un continente
    '''
    def __init__(self, name:str, points:int, continent:str):
        self.name = name
        self.continent = continent
        self.points = points
        self.tanks = 0
    
    def conquered(self, player:player, num_tanks:int):
        self.player = player
        self.tanks = num_tanks
        
class continent:
    '''
    Un continente è composto da n stati. 
    Se un giocatore conquista un intero continente, 
    ha diritto a x tank in più ad ogni turno.
    '''
    def __init__(self, name:str, countries:list, points:int) -> None:
        self.name = name
        self.countries = countries
        self.points = points
        
    def get_points(self):
        return self.points
    
    
        