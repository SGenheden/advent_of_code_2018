
import fileinput
import re
from operator import attrgetter


class Group():

    def __init__(self, definition, id, boost=0):
        self.id = id
        regex1 = r"(?P<units>.+) units each with (?P<hit_points>.+) hit points (?P<traits>\(.+\))? ?with an attack " \
                 r"that does (?P<attack_damage>.+) (?P<damage_type>.+) damage at initiative (?P<initiative>.+)"
        match = re.match(regex1, definition)
        self.units = int(match['units'])
        self.hit_points = int(match['hit_points'])
        self.attack_damage = int(match['attack_damage']) + boost
        self.damage_type = match['damage_type']
        self.initiative = int(match['initiative'])

        self.weaknesses = []
        self.immunities = []
        if match['traits']:
            for trait in match['traits'][1:-1].split('; '):
                if trait.startswith('weak to '):
                    self.weaknesses = trait[len('weak to '):].split(', ')
                if trait.startswith('immune to '):
                    self.immunities = trait[len('immune to '):].split(', ')

        self.target = None

    def __lt__(self, other):
        if self.effective_power == other.effective_power:
            return self.initiative < other.initiative
        else:
            return self.effective_power < other.effective_power

    def __repr__(self):
        traits_str = ""
        if self.immunities:
            traits_str += "immune to " + ", ".join(f"!{w}!" for w in self.immunities)
        if self.weaknesses:
            if self.immunities:
                traits_str += "; "
            traits_str += "weak to " + ", ".join(f"!{w}!" for w in self.weaknesses)
        if traits_str:
            traits_str = "("+traits_str+")"
        return f"<{self.__class__.__name__} {self.id}> {self.units} units each with {self.hit_points} hit points " \
               f"{traits_str} with an attack that does {self.attack_damage} {self.damage_type} at " \
               f"initiative {self.initiative}"

    @property
    def effective_power(self):
        return self.units * self.attack_damage

    def infliction(self, attacking, half=False):
        if attacking.damage_type in self.immunities:
            return 0
        elif attacking.damage_type in self.weaknesses:
            return 2*attacking.effective_power
        else:
            return attacking.effective_power

    def wound(self, attacking):
        damage = self.infliction(attacking, half=True)
        loss = int(damage / self.hit_points)
        if loss > self.units:
            loss = self.units
        self.units -= loss
        return loss


class Infection(Group):
    pass


class ImmuneSystem(Group):
    pass


def count(groups):
    nimmunes = sum([g.units for g in groups if isinstance(g, ImmuneSystem)])
    ninfections = sum([g.units for g in groups if isinstance(g, Infection)])
    return nimmunes, ninfections


def selection_phase(groups, verbose=False):
    taken = [False]*len(groups)
    groups.sort(reverse=True)
    for i, attacking in enumerate(groups):
        attacking.target = None
        candidates = [c for i, c in enumerate(groups)
                      if not taken[i] and c.__class__ != attacking.__class__ and c.infliction(attacking) > 0]
        if len(candidates) == 0:
            continue
        inflictions = [c.infliction(attacking) for c in candidates]
        #if verbose:
        #    for i, c in zip(inflictions, candidates):
        #        print(f"{attacking.__class__.__name__} {attacking.id} would deal group {c.id} {i} damage")
        max_infliction = max(inflictions)
        candidates = [c for i, c in zip(inflictions, candidates) if i == max_infliction]
        candidates.sort(reverse=True)
        attacking.target = candidates[0]
        if verbose:
            print(f"{attacking.__class__.__name__} {attacking.id} would deal group {candidates[0].id} {max_infliction} damage")
        taken[groups.index(candidates[0])] = True


def attacking_phase(groups, verbose=False):
    groups.sort(key=attrgetter('initiative'), reverse=True)
    wounded = False
    for attacking in groups:
        if attacking.target is None or attacking.units <= 0:
            continue
        loss = attacking.target.wound(attacking)
        if loss > 0:
            wounded = True
        if verbose:
            print(f"{attacking.__class__.__name__} {attacking.id} attacks group {attacking.target.id}, killing {loss} units")
    if not wounded:
        raise Exception("No wounded!")


def read_input(boost=0, lines=None):
    if lines is None:
        lines = [line.strip() for line in fileinput.input()]
    groups = []
    i = 1
    n = 0
    while i < len(lines):
        n += 1
        groups.append(ImmuneSystem(lines[i], n, boost=boost))
        i += 1
        if len(lines[i]) == 0:
            break

    i += 2
    n = 0
    while i < len(lines):
        n += 1
        groups.append(Infection(lines[i], n))
        i += 1
    return groups, lines
