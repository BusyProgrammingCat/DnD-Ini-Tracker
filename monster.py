import dice

tracker_list = [] # Haltet alle aktiven Kreaturen


class DeathAbility:
    pass
DEATH_ABI_ARRAY = []


class Monster:
    def __init__(self, type, const_hp=0, hp_dice=[], death_abi=None): # Wird automatisch in der Tracker Liste hinzugefügt

        self.name = type.capitalize()
        self.TYPE = type.capitalize()
        self.CONST_HP = const_hp     # CONSTANT HP, also konstante Hit Points, ist das Basis HP, welches die Kreatur haben muss
        self.HP_DICE = hp_dice       # HP DICE, also HP Würfel, sind die Würfel, die für die Hit Points genutzt werden
        self.DEATH_ABI = death_abi   # DEATH ABIlities, also Todesfähigkeiten, sind sonderheiten, die im Falle des Todes auftreten

        self.cur_hp = 0

        for d in self.HP_DICE:
            self.cur_hp += d.roll()
        self.cur_hp += self.CONST_HP

        self.MAX_HP = self.cur_hp

        tracker_list.append(self)
        # Name - Type - Constant HP - HP Dice - Death Ability - Current HP - Max HP

    def __str__(self): # Zeigt den bloßen Variablennamen als modifizierter String auf
        return f"{self.name} - {self.TYPE} - {self.cur_hp}/{self.MAX_HP}"

    def death_sequence(self):
        if self.DEATH_ABI in DEATH_ABI_ARRAY:
            self.DEATH_ABI()
        else:
            tracker_list.remove(self)

    def check_if_dead(self):
        if self.cur_hp < 1:
            self.death_sequence()

    def rename_monster(self, new_name):
        self.name = new_name

    def change_hp(self):
        pass

    def force_edit(self, type, const_hp, hp_dice, death_abi, name):
        pass # Fürs nutzen von pre-made Arten von Kreaturen

def show_list():
    for i in range(len(tracker_list)):
        print(f"{i} : {tracker_list[i]}")
