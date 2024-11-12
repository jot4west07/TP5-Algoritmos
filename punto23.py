from arbol_avl import BinaryTree
from cola import Queue

lista_criaturas = [
  {
    "criatura": "Ceto",
    "descripcion": "Diosa marina, madre de monstruos marinos y serpientes míticas; su figura simboliza los terrores ocultos del océano en la mitología griega antigua.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Tifón",
    "descripcion": "Gigantesco monstruo con múltiples cabezas de serpiente, considerado padre de los monstruos y conocido por sus enfrentamientos titánicos contra los dioses del Olimpo.",
    "derrotado_por": "Zeus",
    "capturada": "",
  },
  {
    "criatura": "Equidna",
    "descripcion": "Ser mitad mujer, mitad serpiente, conocida como madre de monstruos; engendró criaturas terroríficas con Tifón, como Cerbero, Hidra y Quimera.",
    "derrotado_por": "Argos Panoptes",
    "capturada": "",
  },
  {
    "criatura": "Dino",
    "descripcion": "Una de las Grayas, hermana de Pefredo y Enio; personifica el terror y posee solo un ojo y un diente, que comparte con sus hermanas.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Pefredo",
    "descripcion": "Una de las tres Grayas; representa la prudencia y comparte un ojo y un diente con sus hermanas para ver y hablar.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Enio",
    "descripcion": "Grayas, hermana de Dino y Pefredo; comparte el ojo y diente mágico con ellas y representa la fuerza en la mitología griega.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Escila",
    "descripcion": "Monstruosa criatura marina con cabezas de perros alrededor de su cintura; habitaba en el estrecho de Mesina, aterrorizando a marineros junto a Caribdis.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Caribdis",
    "descripcion": "Voraz monstruo marino que provoca remolinos gigantescos, situándose cerca de Escila en el estrecho de Mesina, representando los peligros de los mares.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Euríale",
    "descripcion": "Una de las tres Gorgonas, junto a Medusa y Esteno; inmortal, con cabello de serpientes, y capaz de convertir a cualquiera en piedra.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Esteno",
    "descripcion": "Gorgona inmortal hermana de Euríale y Medusa; de aspecto temible y cabello de serpiente, temida por su habilidad de petrificar a los hombres.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Medusa",
    "descripcion": "Única Gorgona mortal; famosa por su cabello de serpientes y mirada petrificante. Decapitada por Perseo, su sangre engendró al caballo Pegaso.",
    "derrotado_por": "Perseo",
    "capturada": "",
  },
  {
    "criatura": "Ladón",
    "descripcion": "Dragón de múltiples cabezas que vigilaba las manzanas de oro del Jardín de las Hespérides; su derrota fue uno de los trabajos de Hércules.",
    "derrotado_por": "Heracles",
    "capturada": "",
  },
  {
    "criatura": "Águila del Cáucaso",
    "descripcion": "Ave gigante enviada por Zeus para devorar el hígado de Prometeo cada día, como castigo por robar el fuego para la humanidad.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Quimera",
    "descripcion": "Bestia híbrida con cabeza de león, cuerpo de cabra y cola de serpiente, que exhalaba fuego. Derrotada por el héroe Belerofonte.",
    "derrotado_por": "Belerofonte",
    "capturada": "",
  },
  {
    "criatura": "Hidra de Lerna",
    "descripcion": "Serpiente monstruosa con múltiples cabezas que se regeneraban al cortarlas; fue vencida por Hércules en uno de sus trabajos.",
    "derrotado_por": "Heracles",
    "capturada": "",
  },
  {
    "criatura": "León de Nemea",
    "descripcion": "Invulnerable criatura con piel impenetrable. Hércules lo derrotó en su primer trabajo, usando su propia piel como armadura.",
    "derrotado_por": "Heracles",
    "capturada": "",
  },
  {
    "criatura": "Esfinge",
    "descripcion": "Criatura con cuerpo de león, alas de águila y rostro de mujer; famosa por sus acertijos, especialmente el de Edipo en Tebas.",
    "derrotado_por": "Edipo",
    "capturada": "",
  },
  {
    "criatura": "Dragón de la Cólquida",
    "descripcion": "Serpiente gigantesca que protegía el Vellocino de Oro en la Cólquida. Derrotado por Jasón en su búsqueda heroica.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Cerbero",
    "descripcion": "Perro de tres cabezas que guarda las puertas del inframundo, impidiendo que los muertos salgan y protegiendo el reino de Hades.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Cerda de Cromión",
    "descripcion": "Jabalí monstruoso devastador, descendiente de Tifón y Equidna; fue derrotado por el héroe Teseo en sus hazañas heroicas.",
    "derrotado_por": "Teseo",
    "capturada": "",
  },
  {
    "criatura": "Ortro",
    "descripcion": "Perro de dos cabezas, hermano de Cerbero y guardián del ganado de Gerión. Fue asesinado por Hércules en uno de sus trabajos.",
    "derrotado_por": "Heracles",
    "capturada": "",
  },
  {
    "criatura": "Toro de Creta",
    "descripcion": "Toro gigantesco que causaba estragos en Creta. Capturado por Hércules en su séptimo trabajo y llevado a Grecia.",
    "derrotado_por": "Teseo",
    "capturada": "",
  },
  {
    "criatura": "Jabalí de Calidón",
    "descripcion": "Bestia enviada por Artemisa para devastar Calidón. Fue cazado en una famosa expedición que reunió a varios héroes griegos.",
    "derrotado_por": "Atalanta",
    "capturada": "",
  },
  {
    "criatura": "Carcinos",
    "descripcion": "Gigantesco cangrejo que ayudó a la Hidra de Lerna en su lucha contra Hércules, quien lo aplastó. Conmemorado en la constelación de Cáncer.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Gerión",
    "descripcion": "Gigante de tres cuerpos y una sola cintura. Poseía un rebaño de ganado guardado por Ortro. Fue derrotado por Hércules.",
    "derrotado_por": "Heracles",
    "capturada": "",
  },
  {
    "criatura": "Cloto",
    "descripcion": "Una de las Moiras, diosa del destino, encargada de hilar el hilo de la vida de cada persona, representando el inicio de sus destinos.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Láquesis",
    "descripcion": "Moira que mide el hilo de la vida de cada ser, determinando cuánto vivirán; representa el transcurso y las decisiones de la vida.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Átropos",
    "descripcion": "La Moira que corta el hilo de la vida, poniendo fin a la existencia; simboliza la inevitabilidad de la muerte en la mitología griega.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Minotauro de Creta",
    "descripcion": "Criatura mitad hombre, mitad toro, encerrada en el Laberinto de Creta. Teseo lo derrotó con la ayuda de Ariadna.",
    "derrotado_por": "Teseo",
    "capturada": "",
  },
  {
    "criatura": "Harpías",
    "descripcion": "spíritus alados, mitad mujeres mitad aves, conocidas por robar comida y atormentar con pestilencia; servían como agentes de castigo divino.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Argos Panoptes",
    "descripcion": "Gigante con cien ojos, guardián vigilante y servicial de Hera. Sus ojos fueron inmortalizados en la cola del pavo real.",
    "derrotado_por": "Hermes",
    "capturada": "",
  },
  {
    "criatura": "Aves del Estínfalo",
    "descripcion": "Pájaros con plumas metálicas y venenosas; causaban estragos en la región de Estínfalo. Fueron derrotadas por Hércules en otro trabajo.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Talos",
    "descripcion": "Autómata gigante de bronce que protegía Creta lanzando piedras contra intrusos; fue destruido cuando su talón, fuente de vida, fue perforado.",
    "derrotado_por": "Medea",
    "capturada": "",
  },
  {
    "criatura": "Sirenas",
    "descripcion": "Criaturas mitad mujeres, mitad aves o peces, que atraían a los marineros con su canto encantador para hacerlos naufragar.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Pitón",
    "descripcion": "Serpiente gigantesca que habitaba Delfos. Fue derrotada por Apolo, quien estableció su santuario y oráculo en ese lugar.",
    "derrotado_por": "Apolo",
    "capturada": "",
  },
  {
    "criatura": "Cierva de Cerinea",
    "descripcion": "Cierva sagrada de Artemisa, con pezuñas de bronce y cuernos de oro; fue capturada por Hércules en uno de sus trabajos.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Basilisco",
    "descripcion": "Serpiente legendaria cuyo aliento y mirada causaban muerte instantánea; representado a menudo como un pequeño dragón o gallo con habilidades venenosas.",
    "derrotado_por": "",
    "capturada": "",
  },
  {
    "criatura": "Jabalí de Erimanto",
    "descripcion": "Jabalí feroz que devastaba la región de Erimanto; capturado vivo por Hércules como parte de sus doce trabajos heroicos.",
    "derrotado_por": "",
    "capturada": "",
  }
]

class CreatureTree(BinaryTree): # CreatureTree hereda de BinaryTree
    
    # Cargar criaturas en el árbol desde JSON
    def __init__(self):
        super().__init__() # super().__init__() hereda el constructor de la clase padre(BinaryTree) 
        self.defeated_by_count = {} # Diccionario para derrotado por (pueden ser varios)

    def insert_creature(self, data):
        name = data["criatura"] # data["criatura"] es el nombre de cada criatura
        # .get() si la clave existe, se devuelve el valor asociado. Si la clave no existe (es decir, no se encuentra en el diccionario), se devuelve el valor predeterminado "" (una cadena vacía)
        defeated_by = data.get("derrotado_por", "")
        description = data.get("descripcion", "")
        captured_by = data.get("capturada", "")
        other_value = {
            "defeated_by": defeated_by,
            "description": description,
            "captured_by": captured_by
        }
        if defeated_by: # Si existe defeated_by
            # Esta línea de código actualiza un diccionario llamado defeated_by_count, que lleva un registro de cuántas criaturas han sido derrotadas por cada héroe o dios
            # si nunca antes se ha registrado a ese héroe o dios, se empieza con un conteo de 0
            # se le suma 1, ya que estamos contando una nueva criatura que ese héroe o dios ha derrotado
            self.defeated_by_count[defeated_by] = self.defeated_by_count.get(defeated_by, 0) + 1
        self.insert_node(name, other_value)

    # Listado inorden de criaturas y quién las derrotó
    def inorden_creatures_and_defeated_by(self):
        def __inorden(root): # empieza ejecutando el recorrido en el nodo raíz del árbol binario, que está almacenado en self.root
            if root: # comprueba si el nodo actual (root) es None. Si es None, significa que hemos llegado a una hoja del árbol (o no hay más nodos en ese subárbol), por lo que la función termina la recursión para esa rama.
            # Si el nodo existe (root no es None), se sigue procesando
                __inorden(root.left)
                # get('defeated_by', 'No derrotado') obtiene el valor asociado con la clave 'defeated_by'. Si no se encuentra esa clave (es decir, si la criatura no tiene un héroe o dios registrado como su derrotador), devuelve 'No derrotado' como valor por defecto
                print(f"{root.value}: derrotado por {root.other_value.get('defeated_by', 'No derrotado')}")
                __inorden(root.right)
        __inorden(self.root) # se llama a __inorden(self.root), donde self.root es el nodo raíz del árbol. Esto inicia el recorrido del árbol desde el nodo raíz y procesa todos los nodos del árbol en el orden inorden

    # Metodo by_level ordenando correctamente por nivel (mostrar 1ero el nivel 0, luego 1, 2, 3, y asi...)
    

    # Mostrar toda la información de Talos
    def show_talos_info(self):
        node = self.search("Talos")
        if node: # si node no es None (es decir, si se encontró un nodo con el valor "Talos"), la condición se considera verdadera y el bloque de código dentro del if se ejecutará
            print(f"Talos: {node.other_value}")
        else:
            print("Talos no se encuentra en el árbol")

    # Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
    def top_3_defeaters(self):
        # items() de un diccionario devuelve una lista de tuplas, donde cada tupla tiene la forma (clave, valor) (es decir, (nombre del héroe, cantidad de criaturas derrotadas))
        # sorted() ordena la lista de tuplas obtenida de items() en base a una clave proporcionada por el parámetro key
        # La lambda toma un parámetro x (que es una tupla de la forma (héroe, cantidad)) y devuelve x[1], es decir, el valor de la tupla, que es la cantidad de criaturas derrotadas
        top_3 = sorted(self.defeated_by_count.items(), key=lambda x: x[1], reverse=True)[:3]
        # Al especificar key=lambda x: x[1], le estamos indicando a sorted() que ordene las tuplas por la cantidad de criaturas derrotadas (el segundo valor de cada tupla)
        # reverse=True hace que la ordenación se realice en orden descendente, es decir, de mayor a menor cantidad de criaturas derrotadas
        # Después de ordenar la lista, [:3] selecciona los primeros 3 elementos de la lista ordenada, los 3 con mas victorias
        # top_3 en este punto es: [("Heracles", 12), ("Zeus", 7), ("Perseo", 3)]
        print("Los 3 héroes/dioses que derrotaron más criaturas:")
        for name, count in top_3:
            print(f"{name} derrotó {count} criaturas")

    # Listar criaturas derrotadas por Heracles
    def list_creatures_defeated_by(self, hero_name):
        def __inorden(root):
            if root:
                __inorden(root.left)
                if root.other_value.get("defeated_by") == hero_name:
                    print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    # Listar criaturas que no han sido derrotadas
    def list_undefeated_creatures(self):
        def __inorden(root):
            if root:
                __inorden(root.left)
                if not root.other_value.get("defeated_by"):
                    print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    # Marcar criaturas como capturadas por Heracles
    def mark_captured_by_heracles(self, names):
        for name in names:
            node = self.search(name)
            if node: # Si el nodo existe
                node.other_value["captured_by"] = "Heracles" # Agrega a other_value el ser capturada por Heracles

    # Búsqueda por coincidencia
    def search_by_coincidencia(self, match):
        def __inorden(root):
            if root:
                __inorden(root.left)
                if match.lower() in root.value.lower():
                    print(f"{root.value}: {root.other_value}")
                __inorden(root.right)
        __inorden(self.root)

    # Eliminar Basilisco y Sirenas
    def delete_creatures(self, names):
        for name in names:
            self.delete_node(name)

    # Modificar Aves del Estínfalo con Heracles como derrotador
    def update_aves(self):
        node = self.search("Aves del Estínfalo")
        if node:
            node.other_value["defeated_by"] = "Heracles (derrotó varias)"

    def mostrar_aves_estinfalo(self):
    # Recorremos el árbol en busca del nodo con el valor "Aves del Estínfalo"
      node = self.search('Aves del Estínfalo')  

    # Si el nodo existe, mostramos toda la información
      if node:
        # Aquí estamos accediendo correctamente a los valores dentro de 'node.other_value'
        print(f"Nombre: {node.value}")  # Imprime el nombre de la criatura (Aves del Estínfalo)
        print(f"Descripción: {node.other_value['description']}")
        print(f"Derrotado por: {node.other_value['defeated_by']}")
        print(f"Capturado por: {node.other_value['captured_by']}")
      else:
        print("No se encontró la criatura 'Aves del Estínfalo'.")


    # Modificar Ladón por Dragón Ladón
    def rename_ladon(self):
        # Si el nodo se encuentra y se elimina correctamente, value tendrá el valor "Ladón" y extra_data tendrá los demás datos relacionados a la criatura "Ladón"
        value, extra_data = self.delete_node("Ladón")
        if value: # Si value tiene un valor (es decir, no es None), significa que el nodo con el valor "Ladón" fue encontrado y eliminado exitosamente.
            # Llama al método insert_node para insertar un nuevo nodo en el árbol con el nombre "Dragón Ladón". Los datos adicionales de la criatura (como su descripción y quién la derrotó) se pasan como extra_data para asociarlos al nuevo nodo
            self.insert_node("Dragón Ladón", extra_data)

    # Listado por nivel del arbol de forma desordenada (originalmente)
    def desorden_nivel(self):
        self.by_level_desordenado()

    # Listado por nivel del árbol(0,1,2,3,4,5,6) (modificado)
    def orden_nivel(self):
      self.by_level_ordenado()

    # Mostrar criaturas capturadas por Heracles
    def list_creatures_captured_by_heracles(self):
        def __inorden(root):
            if root:
                __inorden(root.left)
                if root.other_value.get("captured_by") == "Heracles":
                    print(root.value)
                __inorden(root.right)
        __inorden(self.root)


# Crear árbol y cargar criaturas
creature_tree = CreatureTree()
for creature_data in lista_criaturas:
    creature_tree.insert_creature(creature_data)

# Mostrar informacion:
# Listado inorden de las criaturas y quién las derrotó
print("Listado inorden de las criaturas y derrotadores:")
creature_tree.inorden_creatures_and_defeated_by()


# Mostrar información de Talos
print("\nInformación de Talos:")
creature_tree.show_talos_info()

# Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\nTop 3 héroes que derrotaron más criaturas:")
creature_tree.top_3_defeaters()

# Listar criaturas derrotadas por Heracles
print("\nCriaturas derrotadas por Heracles:")
creature_tree.list_creatures_defeated_by("Heracles")

# Listar criaturas que no han sido derrotadas
print("\nCriaturas que no han sido derrotadas:")
creature_tree.list_undefeated_creatures()

# Marcar criaturas capturadas por Heracles
heracles_captures = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
creature_tree.mark_captured_by_heracles(heracles_captures)

# Búsqueda por coincidencia
print("\nBúsqueda por coincidencia ('Cer'): ")
creature_tree.search_by_coincidencia("Cer")

# Eliminar Basilisco y Sirenas
creature_tree.delete_creatures(["Basilisco", "Sirenas"])
print("")
# Modificar Aves del Estínfalo con Heracles como derrotador
creature_tree.update_aves()
creature_tree.mostrar_aves_estinfalo()

# Renombrar Ladón a Dragón Ladón
creature_tree.rename_ladon()

# Listado por nivel desordenadamente
print("\nListado por nivel desordenado del árbol:")
creature_tree.desorden_nivel()

# Listado por nivel ordenadamente
print("\nListado ordenado por nivel del árbol:")
creature_tree.orden_nivel()

# Listar criaturas capturadas por Heracles
print("\nCriaturas capturadas por Heracles:")
creature_tree.list_creatures_captured_by_heracles()

