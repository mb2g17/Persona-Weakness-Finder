class VariationFactory:
    def __init__(self):
        self.h3_name = ""
        self.h4_name = ""
        self.tab_name = ""

    def create_full_variation_name(self) -> str:
        if self.h3_name == '' and self.h4_name == '' and self.tab_name == '':
            return "No variation"

        names = []
        if self.h3_name != "":
            names.append(self.h3_name)
        if self.h4_name != "":
            names.append(self.h4_name)
        if self.tab_name != "":
            names.append(self.tab_name)

        full_variation = " - ".join(names)

        return full_variation
