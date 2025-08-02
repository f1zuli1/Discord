# Görev 2 - İhtiyacınız olan her şeyi içe aktarın
from discord import ui,ButtonStyle
class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 
    def gen_buttons(self):
        buttons=[]
        for i,option in enumerate(self.options):
            if i==self.__answer_id:
                buttons.append(ui.Button(label=option,style=ButtonStyle.primary,custom_id=f"correct_{i}"))
            else:
                buttons.append(ui.Button(label=option,style=ButtonStyle.primary,custom_id=f"wrong_{i}"))
        return buttons
# Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Azerbaycan'ın başkenti neresidir?", 1, "Küba", "Bakü"),
   Question("Hangisi Asya'da bulunur?", 0, "Azerbaycan", "ABD", "Almanya"),
   Question("Galatasaray hangi yıl kuruldu ?", 3, "1907", "1903","1904", "1905"),
   Question("Galatasaray takiminin renkleri", 1 , "sari, lacivert", "sari, kirmizi")
]
