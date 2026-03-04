Animename=input("Anime name:")
maincharacter=input("main char:")
Age=int(input("Age:"))
Bounty=float(input("bounty on head:"))
crewmates=input("crewmates:").split()
Ate_devil_fruit=bool(input("ate devil fruit(yes/no):"))
ships=tuple(input("ship names:").split())
abilities=set(input("what abilites:").split())
pirate = {
    "Name": maincharacter,
    "Age": Age,
    "Bounty": Bounty,
    "Devil Fruit User": Ate_devil_fruit,
    "Crewmates": crewmates,
    "Ships": ships,
    "Abilities": abilities
}




print(Animename)
print(maincharacter)
print(Age)
print(Bounty)
print(crewmates)
print(Ate_devil_fruit)
print(ships)
print(abilities)
print(pirate)
