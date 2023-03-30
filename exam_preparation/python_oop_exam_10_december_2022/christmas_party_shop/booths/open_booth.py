from exam_preparation.python_oop_exam_10_december_2022.christmas_party_shop.booths.booth import Booth


class OpenBooth(Booth):

    @property
    def price_per_person(self):
        return 2.50
