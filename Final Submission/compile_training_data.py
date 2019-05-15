import os
from collections import OrderedDict 

fact_set= OrderedDict() 
Tomato = OrderedDict() 
Grape = OrderedDict() 
Hibiscus = OrderedDict() 
Sunflower = OrderedDict() 
Hummingbird = OrderedDict() 
Owl = OrderedDict() 
Goldfish = OrderedDict() 
Octopus = OrderedDict() 
Horse = OrderedDict() 
Dog = OrderedDict() 
Car = OrderedDict() 
Bus = OrderedDict() 
Bicycle = OrderedDict() 

Tomato['ISA']=['Living Thing', 'Plant', 'Fruit', 'Tomato']
Tomato['IS']=['Living', 'Red', 'Juicy']
Tomato['CAN']=['Grow','Rot']
Tomato['HAS'] = ['Skin', 'Seeds']
Tomato['NEEDS']=['Water','CO2']
fact_set['Tomato'] = Tomato

Grape['ISA']=['Living Thing', 'Plant', 'Fruit','Grape']
Grape['IS']=['Living', 'Green', 'Juicy']
Grape['CAN']=['Grow','Rot']
Grape['HAS']=['Skin', 'Seeds']
Grape['NEEDS']=['Water','CO2']
fact_set['Grape'] = Grape

Hibiscus['ISA']=['Living Thing', 'Plant', 'Flower','Hibiscus']
Hibiscus['IS']=['Living','Pretty']
Hibiscus['CAN']=['Grow']
Hibiscus['HAS']=['Petals']
Hibiscus['NEEDS']=['Water','CO2']
fact_set['Hibiscus'] = Hibiscus

Sunflower['ISA']=['Living Thing', 'Plant', 'Flower','Sunflower']
Sunflower['IS']=['Living','Pretty', 'Yellow']
Sunflower['CAN']=['Grow']
Sunflower['HAS']=['Petals']
Sunflower['NEEDS']=['Water','CO2']
fact_set['Sunflower'] = Sunflower

Hummingbird['ISA']=['Living Thing', 'Animal','Bird','Hummingbird']
Hummingbird['IS']=['Living','Diurnal']
Hummingbird['CAN']=['Fly', 'Grow', 'Hum', 'Move']
Hummingbird['HAS']=['Wings', 'Feathers']
Hummingbird['NEEDS']=['Water', 'Oxygen', 'Food', 'Sleep']
fact_set['Hummingbird'] = Hummingbird

Owl['ISA']=['Living Thing', 'Animal','Bird','Owl']
Owl['IS']=['Living','Nocturnal']
Owl['CAN']=['Fly', 'Grow', 'Hoot', 'Move']
Owl['HAS']=['Wings', 'Feathers']
Owl['NEEDS']=['Water', 'Oxygen', 'Food', 'Sleep']
fact_set['Owl'] = Owl

Goldfish['ISA']=['Living Thing', 'Animal', 'Water borne', 'Goldfish']
Goldfish['IS']=['Living', 'Small']
Goldfish['CAN']=['Swim', 'Grow','Move']
Goldfish['HAS']=['Fins','Gills','Scales']
Goldfish['NEEDS']=['Water', 'Oxygen', 'Food', 'Sleep']
fact_set['Goldfish'] = Goldfish

Octopus['ISA']=['Living Thing', 'Animal', 'Water borne', 'Mollusk', 'Octopus']
Octopus['IS']=['Living']
Octopus['CAN']=['Swim', 'Grow','Move']
Octopus['HAS']=['Tentacles','Gills']
Octopus['NEEDS']=['Water', 'Oxygen', 'Food', 'Sleep']
fact_set['Octopus'] = Octopus

Horse['ISA']=['Living Thing', 'Animal', 'Land animal', 'Horse']
Horse['IS']=['Living', '4 Legged', 'Domestic']
Horse['CAN']=['Run', 'Strut', 'Neigh', 'Grow']
Horse['HAS']=['Mane', 'Hooves']
Horse['NEEDS']=['Water', 'Oxygen', 'Food', 'Sleep']
fact_set['Horse'] = Horse

Dog['ISA']=['Living Thing', 'Animal', 'Land animal', 'Dog']
Dog['IS']=['Living', '4 Legged', 'Domestic']
Dog['CAN']=['Run', 'Bark', 'Grow']
Dog['HAS']=['Fur', 'Paws']
Dog['NEEDS']=['Water', 'Oxygen', 'Food', 'Sleep']
fact_set['Dog'] = Dog

Car['ISA']=['Non Living Thing', 'Vehicle', 'Car']
Car['IS']=['Non Living', 'Small', 'Motorized']
Car['CAN']=['Move']
Car['HAS']=['4 Wheels', 'Engine', 'Horn']
Car['NEEDS']=['Fuel']
fact_set['Car'] = Car

Bus['ISA']=['Non Living Thing', 'Vehicle', 'Bus']
Bus['IS']=['Non Living', 'Big', 'Motorized']
Bus['CAN']=['Move']
Bus['HAS']=['6 Wheels', 'Engine', 'Horn']
Bus['NEEDS']=['Fuel']
fact_set['Bus'] = Bus

Bicycle['ISA']=['Non Living Thing', 'Vehicle', 'Bicycle']
Bicycle['IS']=['Non Living', 'Small', 'Non Motorized']
Bicycle['CAN']=['Move']
Bicycle['HAS']=['2 Wheels', 'Bell']
Bicycle['NEEDS']=[]
fact_set['Bicycle'] = Bicycle

# get attributes
file = open("data/attributes.txt", "r")
attributes = file.read().splitlines()
file.close()

# get relations
file = open("data/relations.txt", "r")
relations = file.read().splitlines()
file.close()

# get items
file = open("data/items.txt", "r")
items = file.read().splitlines()
file.close()

data_to_train = ''
for obj in fact_set:
    it = [obj]
    #print(it)
    c = [1 if i in it else 0 for i in items]
    s = " ".join(str(x) for x in c)
    s += ' '
    #print(s)
    for relation in fact_set[obj]:    #relation -> the key in each obj('ISA', 'IS' etc)
        rel = [relation]
        #print(rel)
        c = [1 if r in rel else 0 for r in relations]
        q = " ".join(str(x) for x in c)
        q += ' '
        attribs = fact_set[obj][relation]
        #print(attribs)
        c = [1 if a in attribs else 0 for a in attributes]
        q += " ".join(str(x) for x in c)
        data_to_train += s + q + '\n'
        #print(data_to_write)

# write training data to file
file = open("data/data.txt", "w+")
file.write(data_to_train)
file.truncate(file.tell()- len(os.linesep))
file.close()