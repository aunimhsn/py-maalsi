class Robot:
    # Attribut statique
    # Compter le nombre d'instanciation
    

    def __init__(self, name:str, actions:list[str]):
        self.name = name
        self.actions = actions
        Robot.count += 1
