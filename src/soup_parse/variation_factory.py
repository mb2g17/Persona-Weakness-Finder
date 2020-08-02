class VariationFactory:
    def __init__(self):
        self.h3_name = ""
        self.h4_name = ""
        self.tab_name = ""

    def create_full_variation_name(self) -> str:
        names = []
        if self.h3_name != "":
            names.append(self.h3_name)
        if self.h4_name != "":
            names.append(self.h4_name)
        if self.tab_name != "":
            names.append(self.tab_name)

        full_variation = " - ".join(names)

        if full_variation == '':
            full_variation = "No variation"

        return full_variation
