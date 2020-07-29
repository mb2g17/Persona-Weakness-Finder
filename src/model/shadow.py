from typing import Dict


class Shadow:
    def __init__(self, variation: str):
        self.weakness: Dict[str, str] = {}
        self.variation = variation

    def add_weakness(self, atk_type: str, status: str):
        self.weakness[atk_type] = status

    def get_weaknesses(self, atk_type: str):
        return self.weakness[atk_type]

    def get_variation(self) -> str:
        return self.variation
