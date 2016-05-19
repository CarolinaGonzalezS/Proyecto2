
from textblob import TextBlob

def traduccion(text):
    traduc=TextBlob(text)
    print (traduc.translate(to="en"))

print("1.- traduccion de parte de un texto de harry Potter")
print("2.- traduccion de un frase ingresada por usted")
opcion=int(input("elija la opcion que desee:\n"))



if opcion==1:
    frase = '''
    La historia empieza cuando Harry es dejado en la casa de sus Tios, los Dursley, por Rubeus Hagrid, Albus Dumbledore y Minerva McGonnagall. 
    Alli mencionan que Lord Voldemort, el mago mas tenebroso de esos tiempos habia sido vencido, luego de intentar matar a Harry Potter. Harry sobrevivio a la maldicion asesina, con no otra secuela que una cicatriz con forma de rayo en la frente. Como consecuencia de los actos de Voldemort, los padres de Harry, Lily y James, habian muerto, y por eso Harry debia quedarse con sus tios. ni
    El libro continua diez anios despues, donde vemos que Harry no es nada feliz con sus tios, ni sabe que es mago. Los Dursley malcrian a su hijo Dudley, mientras que a Harry lo tratan como un sirviente. 
    Harry sospecha que es especial, y mas cuando en el cumpleanios de Dudley, en un zoologico, hace desaparecer un cristal, haciendo caer a su primo en la jaula de una Boa Constrictora. 
    Poco antes de su cumpleanios Harry recibe una carta de Hogwarts, pero no logra abrirla o causa de su tio, que no quiere que el chico se entere de que puede hacer magia. Los esfuerzos de Vernon no prosperan, y siguen llegando cartas, traidas extraniamente por lechuzas. Para que no haya mas disturbios con las cartas, la familia Dursley con Harry se mudan a una casita en una islita. 
    El dia de cumpleanios de Harry, todavia en esa casita, llega el gigantesco Hagrid a entregarle la carta personalmente, y a desearle feliz cumpleanios. Vernon se tiene que dar por vencido, y Harry se entera de toda la verdad. 
    La carta decia que Harry estaba invitado a participar del primer anio en el Colegio Hogwarts de Magia y Hechizeria. Harry se entusiasma por salir de su vida como muggle, de escaparse de los Dursley, a un lugar donde todos serian como el. 
    Hagrid lleva a Harry al Callejon Diagon a comprar sus cosas para el colegio. Harry, con el Guardian de Llaves de Hogwarts, va al banco de los magos, Gringotts, donde descubre que sus padres le habian dejado una gran fortuna. Luego, por “asuntos de Hogwarts” van a la camara 713 y Hagrid se lleva un paquete misterioso… Harry compra una varita, libros, y Hagrid le regala a Hedwig, una lechuza. 
    Luego empieza el anio en Hogwarts. 
    Al llegar Harry descubre que hay cuatro casas; Gryffindor, Slytherin, Ravenclaw y Hufflepuff, y que va a ser asignador a una. Ron Weasley, un chico que habia conocido en el tren que los llevaba al Colegio, le dice que en Slytherin estaban los magos malos, y Harry desea no entrar a esa casa. Finalmente termina con Ronald en Gryffindor, y el que acaba en Slytherin es Draco Malfoy, un chico que habia insultado a Ron. El director de Hogwarts, Dumbledore, dice que ese anio no se iba a poder entrar en un cuarto del tercer piso. Alli cursa materias antes desconocidas para el, como Pociones, con el Profesor Snape, Defensa Contra las Artes Oscuras, con el Profesor Quirrell, Encantamientos, Transformaciones, y otras mas. Harry conoce a Ron Weasley, y se hacen muy amigos. Luego de vencer a un troll en Halloween, Harry se hace otra mejor amiga; Hermione Granger. 
    En Navidad, Harry recibe anonimamente una capa invisible, que oculta a la vista de los demas al que la usa. Una nota dice que era de su padre, y que la utilice bien. 
    Harry encuentra un espejo, llamado espejo de Oesed. Muestra el mas grande deseo de la persona que lo ve; Harry ve en el espejo a sus padres y a toda su familia. Dumbledore le dice que ese espejo muestra el deseo de la persona, pero que pronto sera llevado a otra parte, dada a la adiccion que provoca. 
    Harry, Neville Longbottom y Hermione llegan por accidente al prohibido tercer piso, donde encuentran un perro de tres cabezas. 
    Una noche Harry, Hermione, Neville y Malfoy quedan castigados porque los dos primeros habian visitado a Hagrid, Malfoy los estaba espiando y Neville les iba a avisar a los dos amigos lo que hacia Draco y Filch los atrapo a todos. Como castigo tuvieron que ir al Bosque Prohibido con Hagrid. 
    En el bosque encontraron sangre de unicornio y Hagrid les dijo que is la tomabas te servia para seguir viviendo. Luego Harry ve a alguien bebiendo de un unicornio, y cai lo ataca pero fue salvado por el Centauro Firenze. 
    El centauro le revela que en el colegio tienen la piedra filosofal, una piedra que da vida eterna. Dice que Voldemort era el que estaba tomando eso. Harry se da cuenta que Fluffy (el perro de tres cabezas, que es de Hagrid) vigila una puerta trampa que hay bajo su cuerpo. Al parecer, esta cuidando algo. Harry, Ron y Hermione estaban seguros de que la Piedra Filosofal era lo que estaba cuidando el Perro. El acontecimiento del Troll, y otras cosas mas, hacen sospechar al Trio que Snape quiere robar la piedra, y hacer el Elixir para revivir a Voldemort. 
    Un dia Hagrid les dice accidentalmente como dormir a Fluffy, y Harry, sabiendo que Sanpe habia ido a robar la Piedra, junto con Hermione y Ron, se encamina al tercer piso. En el camino se encuentran con Neville, que trata de detenerlos, sin exito. Al llegar con Fluffy se encuentran con que se durmio con un arpa que se tocaba sola, y logran bajar por la puerta trampa. Alli abajo se encuentran con una serie de pruebas como un ajedrez gigante y un acertijo de ingenio de pociones. Al final, Harry queda solo para ir a enfrentas a Snape. 
    Harry entra al ultimo cuarto, donde se encuentra con Quirrell. Asi es, no era Snape, era el Profesor Quirrell. Él habia soltado al troll, y embrujado la escoba de Harry en otra ocasion. El Maestro de Defensa se estaba mirando al espejo de Oesed. Una voz aparece de la nada. ¡Usa al muchacho!, dice la voz. Quirrell se saca el turbante de su cabeza, y donde deberia estar su nuca, esta la cara de Lord Voldemort. Quirrel hace reflejarse a Harry en el espejo. Al reflejarse en el, El Ninio Que Vivio se ve con la Piedra Filosofal, y magicamente y sin saber como esta aparece en su bolsillo. Luego, Quirrell se saca su turbante y se da vuelta. En vez de su nuca, esta la cara de Voldemort. El Senior Tenebroso trata de tentar a Harry para que le de la piedra, con promesas de poder, pero Harry no se deja vencer. Luego, Quirrell trata de arrebatarsela, pero Harry lo toca y ve que se empieza a quemar. Al final, Harry lo sigue tocando y Voldemort-Quirrell se hace cenizas. Luego se desmaya. 
    Se despierta en la enfermeria y Dumbledore le dice que Quirrell murio, y Voldemort escapo. Tambien el director habia sido el que le habia mandado la capa de invisibilidad a Harry. 
    Finalmente, el banquete de fin de anio. Cuando Harry entra al Gran Comedor se encuentra con decoraciones verde y plata: Slytherin habia ganado. Pero luego de agragarle a Harry, Ron y Hermione puntos, Gryffindor y Slytherin quedaron empatados. Finalmente, se le agregan unos pocos puntos mas a Neville por haber intentado detener al Trio. Gryffindor habia ganado la Copa de las Casas.
    '''
    traduccion(frase)

if opcion==2:
    frase=str(input("ingrese la frase a traducir\n"))
    print("tu frase es:")
    print(frase)
    print("tu traduccion es: ")  
    traduccion(frase)







