class Pokemon_type:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return self.name

class Pokemon:
    def __init__(self, name, level, p_type, max_health, health, is_knocked_out):
        self.name = name
        self.level = level
        self.p_type = p_type
        self.max_health = max_health
        self.health = health
        self.is_knocked_out = is_knocked_out
        
    def __repr__(self):
        return self.name

    def lose_health(self, loss):
        h = self.health - loss 
        if h > 0: 
            self.health = h
            self.print_health() 
        else: 
            self.health = 0 
            self.knock_out()

        self.level = self.health
        

    def gain_health (self, gain):
        h = self.health + gain 
        if h > self.max_health : self.health = self.max_health
        else: self.health = h

        self.level = self.health
        if self.is_knocked_out: self.heal()
        self.print_health()
        
    def print_health(self):
        if self.health == self.max_health:
            print (f"{self.name} has maximum health!")
        elif self.is_knocked_out:
            print(f"{self.name} has been knocked out!")
        else:
            print (f"{self.name} has {self.health} health.")
    
    def knock_out(self):
        self.is_knocked_out = True
        print(f"{self.name} has been knocked out!")
    
    def heal(self):
        self.is_knocked_out = False
        print(f"{self.name} has been healed!")

    def attack(self,other_pokemon):
        loss = 0 
        effective = "Effective attack!"
        if not self.is_knocked_out:
            if self.p_type.weight <= other_pokemon.p_type.weight:
               loss = int(self.level/2)
               effective = "Ineffective attack!"
            else:
                loss = self.level*2
            print(f"{other_pokemon.name} has been attacked by {self.name} with {loss} force! {effective}")
            other_pokemon.lose_health(loss)
        else: print(f"{other_pokemon.name} cannot attack while it is knocked out!")

class Trainer:
    def __init__(self, name, pokemon_list, potions, current_pokemon):
        #ensure that only the first six pokemons are picked
        if len(pokemon_list) > 6 :
            pokemon_list = pokemon_list[:6]

        self.name =  name
        self.pokemons = pokemon_list
        self.potions = potions # number of available potions
        self.current_pokemon = current_pokemon # a no. between 0 and 5
    
    def __repr__(self):
        return self.name

    def drink_potion(self):
        if self.potions > 0:
            print(f"{self}:{self.pokemons[self.current_pokemon]} is drinking a potion.")
            self.pokemons[self.current_pokemon].gain_health(2000)
            self.potions -=1
        else:
            print(f"Unable to heal {self.pokemons[current_pokemon].name}. No potions available!")
        
    def attack(self,other_trainer):
        print(f"\n{self}:{self.pokemons[self.current_pokemon]} is attacking {other_trainer}:{other_trainer.pokemons[other_trainer.current_pokemon]}!")
        self.pokemons[self.current_pokemon].attack(other_trainer.pokemons[other_trainer.current_pokemon])
    
    def switch_pokemon(self,new_pokemon):
        if new_pokemon < len(self.pokemons) :
            if not self.pokemons[new_pokemon].is_knocked_out:
                self.current_pokemon = new_pokemon 
                print(f"{self} switched current pokemon to: {self.pokemons[self.current_pokemon].name}.")
            else: print("Unable to switch to pokemon which is knocked out!")
        else:
            print("Unable to switch pokemon. Incorrect pokemon number")
    
    def print_health(self):
        print(self)
        self.pokemons[self.current_pokemon].print_health()


# Test area

# creating Pokemon_types
grass  = Pokemon_type("Grass",20)
fire  = Pokemon_type("Fire",40)
water  = Pokemon_type("Water",80)

# creating Pokemons
# (self, name, level, p_type, max_health, health, is_knocked_out)
water_pok = Pokemon("Powerful", 9000, water, 30000, 9000, False)
fire_pok = Pokemon("BubblingUnder", 5000, fire, 30000, 5000, False)
grass_pok = Pokemon("Weak", 2000, grass, 30000, 2000, False)

# creating trainers
# (self, name, pokemon_list, potions, current_pokemon)
trainer_alex = Trainer("Alex",[water_pok,water_pok,water_pok,fire_pok], 1,0)
trainer_jane = Trainer("Jane",[fire_pok,grass_pok,fire_pok,], 3,0)
trainer_john = Trainer("John",[grass_pok,grass_pok,water_pok,fire_pok], 5,1)

#attacking
trainer_jane.attack(trainer_john)
trainer_alex.attack(trainer_jane)
print("")
trainer_jane.print_health()
trainer_john.print_health()

trainer_john.switch_pokemon(2)
trainer_jane.drink_potion()
trainer_john.attack(trainer_jane)

print("")
trainer_jane.print_health()
trainer_john.print_health()

print("")
trainer_jane.drink_potion()
trainer_jane.attack(trainer_john)

print("")
trainer_jane.print_health()
trainer_john.print_health()
