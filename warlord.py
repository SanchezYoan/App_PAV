from .warrior import Warrior

class Warlord(Warrior):

    def __init__(self, strength=4, life_point=100, defense=2):
        """
        :param strenght: damage that will inflict the Healer
        :param life_point: Maximum life point that ealer can hold
        """
        self.defense=defense

        super().__init__(strength=strength, life_point=life_point)

    def damaged(self, dmg):
        """
        reduce damage from self.defense call Warrior.damaged
        :param dmg: damage to be reduced
        """
        dmg -= self.defense
        if dmg < 0:
            dmg = 0
        super().damaged(dmg)
        