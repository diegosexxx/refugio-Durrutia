"simulacion de un dia en el refugio. "


from animal import Animal           


#instanciar animales
Luna = Animal("Luna", "gato", 3)
Rocky = Animal("Rocky", "perro", 5)
Kiwi = Animal("Kiwi", "loro", 2)

#Presentaciones
Luna.presentarse()
Rocky.presentarse()
Kiwi.presentarse()


#Actividades luna

Luna.jugar()
Luna.comer(150)
Luna.dormir()

#Actividades rocky

Rocky.jugar()
Rocky.jugar()
Rocky.jugar()
Rocky.comer(300)

#Actividades kiwi

Kiwi.comer(100)
Kiwi.dormir()





















