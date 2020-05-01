import re
from utils import lib, letters
from .msd import MSD


class Pronoun(MSD):
    def __init__(self, w):
        super().__init__(w)

        if self.reg[-1] not in letters.vows:
            self.reg += "`"

        self.pers = w.ana[1]
        self.case = w.ana[2].split("/")[-1]
        self.num = w.ana[3].split("/")[-1] if self.pers != "возвр" else "ед"

    def get_lemma(self):
        lemma = None

        if self.pers == "возвр" and self.case in lib.pron_refl:
            if re.match(lib.pron_refl[self.case][0], self.reg):
                lemma = lib.pron_refl[self.case][1]
            elif self.reg == "С`":
                lemma = "СЕБЕ"
        elif (self.pers, self.case, self.num) in lib.pron_pers:
            if re.match(lib.pron_pers[(self.pers, self.case, self.num)][0], self.reg):
                lemma = lib.pron_pers[(self.pers, self.case, self.num)][1]
            elif self.reg == "М`":
                lemma = "АЗЪ"
            elif self.reg == "Т`":
                lemma = "ТЫ"

        return self.reg, lemma

    @property
    def value(self):
        return ["личн", self.pers, self.case, self.num]