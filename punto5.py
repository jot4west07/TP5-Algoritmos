from cola import  Queue
from arbol import BinaryTree
from arbol_avl import BinaryTree

# Nuevas funciones 
def listar_villanos(tree):
    tree.inorden_villanos()

def superheroes_con_c(tree):
    tree.inorden_superheros_start_with('C')

def contar_superheroes(tree):
    return tree.contar_super_heroes()

def corregir_doctor_strange(tree):
    def __buscar_y_corregir(root):
        if root is not None:
            __buscar_y_corregir(root.left)
            if root.value == "Doctor Strange":
                print("Encontrado:", root.value)
                root.value = "Doctor Stephen Strange"  # Corrección del nombre
                print("Nombre corregido a:", root.value)
            __buscar_y_corregir(root.right)

    if tree.root is not None:
        __buscar_y_corregir(tree.root)


def listar_superheroes_descendente(tree):
    tree.postorden()

def crear_bosque(tree):
    heroes_tree = BinaryTree()
    villanos_tree = BinaryTree()
    
    def dividir_arbol(root): # funcion recursiva
        if root is not None:
            if root.other_value.get('is_hero'): # si es un heroe
                heroes_tree.insert_node(root.value, root.other_value) # insertar nodo
            else:
                villanos_tree.insert_node(root.value, root.other_value) # si villano insertarlo en el arbol villanos
            dividir_arbol(root.left) # ingresa la raiz izquierda y procesa
            dividir_arbol(root.right) # ingresa la raiz derecha y procesa
    
    dividir_arbol(tree.root)
    
    return heroes_tree, villanos_tree # devuelve los arboles creados


# Funciones para listar héroes y villanos en orden alfabético en sus respectivos árboles
def listar_heroes_alfabetico(heroes_tree):
    print("Árbol de Héroes en orden alfabético:")
    heroes_tree.inorden()

def listar_villanos_alfabetico(villanos_tree):
    print("Árbol de Villanos en orden alfabético:")
    villanos_tree.inorden()

# Función para contar nodos de un árbol
def contar_nodos(tree): # ingresa el arbol como argumento
    def __contar(root):
        if root is None:
            return 0
        return 1 + __contar(root.left) + __contar(root.right)

    return __contar(tree.root) # funcion recursiva 

# Crear el bosque de héroes y villanos y contar sus nodos
def crear_bosque_y_contar_nodos(tree):
    heroes_tree, villanos_tree = crear_bosque(tree)
    
    # Contar nodos en cada árbol
    cantidad_heroes = contar_nodos(heroes_tree)
    cantidad_villanos = contar_nodos(villanos_tree)
    
    print("Cantidad de nodos en el árbol de héroes:", cantidad_heroes)
    print("Cantidad de nodos en el árbol de villanos:", cantidad_villanos)
    
    return heroes_tree, villanos_tree

# Crear el árbol y cargar héroes y villanos
mcu_tree = BinaryTree()

# Insertar héroes
mcu_tree.insert_node("Captain America", {"is_hero": True})
mcu_tree.insert_node("Iron Man", {"is_hero": True})
mcu_tree.insert_node("Captain Marvel", {"is_hero": True})
mcu_tree.insert_node("Doctor Strange", {"is_hero": True})

# Insertar villanos
mcu_tree.insert_node("Thanos", {"is_hero": False})
mcu_tree.insert_node("Loki", {"is_hero": False})
mcu_tree.insert_node("Ultron", {"is_hero": False})
mcu_tree.insert_node("Hela", {"is_hero": False})

# b. listar los villanos ordenados alfabéticamente
print("Villanos en orden alfabético:")
listar_villanos(mcu_tree)
print("\n")

# c. mostrar todos los superhéroes que empiezan con C
print("Superhéroes que empiezan con 'C':")
superheroes_con_c(mcu_tree)
print("\n")

# d. determinar cuántos superhéroes hay el árbol
num_heroes = contar_superheroes(mcu_tree)
print(f"Cantidad de superhéroes en el árbol: {num_heroes}")
print("\n")

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre
print("Corrección de Doctor Strange:")
corregir_doctor_strange(mcu_tree)
print("\n")

# f. listar los superhéroes ordenados de manera descendente
print("Superhéroes en orden descendente:")
listar_superheroes_descendente(mcu_tree)
print("\n")

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas
# Crear bosque y listar héroes y villanos en sus árboles separados
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
heroes_tree, villanos_tree = crear_bosque_y_contar_nodos(mcu_tree)
print("")
listar_heroes_alfabetico(heroes_tree)
listar_villanos_alfabetico(villanos_tree)