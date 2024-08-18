import pandas as pd
def definir_posiciones(equipo):
    tactica1 = '4-3-3'
    tactica2 = '4-2-4'
    tactica3 = '3-5-2'
    tactica4 = '4-5-1'
    tactica5 = '4-4-2'
    tactica6 = '5-3-2'
    
    
    
    print(equipo)

def posicion_generica(posicion):
    
    defensalist = ['Defensa-Central', 'Lateral-Derecho', 'Lateral-Izquierdo']
    mediocampolist = ['Centrocampista-Central', 'Centrocampista-Defensivo', 'Centrocampista-Ofensivo',
                      'Interior-Derecho', 'Interior-Izquierdo']
    delanterolist = ['Delantero-Centro', 'Segundo-Delantero', 'Extremo-Derecho',
                     'Extremo-Izquierdo']
    
    if posicion in defensalist:
        return 'Defensa'
    
    if posicion in mediocampolist:
        return 'Centrocampista'
    
    if posicion in delanterolist:
        return 'Delantero'
    
    return 'Portero'

def filtrar_top_jugadores(grupo):
    if grupo.name[1] == 'Defensa':
        return grupo.head(4)
    elif grupo.name[1] == 'Centrocampista':
        return grupo.head(3)
    elif grupo.name[1] == 'Delantero':
        return grupo.head(3)
    elif grupo.name[1] == 'Portero':
        return grupo.head(1)
    else:
        return pd.DataFrame()  # En caso de posiciones no especificadas

def asignar_puntos_posicion(Pos):
    
    match Pos:
        case 1:
            return 10
        case 2:
            return 9
        case 3:
            return 8
        case 4:
            return 7
        case 5:
            return 6
        case 6: 
            return 5
        case 7:
            return 4
        case 8:
            return 3
        case 9:
            return 2
        case 10:
            return 1
        case _:
            return 0
    
    