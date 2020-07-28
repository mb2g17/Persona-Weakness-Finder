from typing import Dict


class Shadow:
    def __init__(self):
        self.weakness: Dict[str, str] = {}

    def add_weakness(self, atk_type: str, status: str):
        self.weakness[atk_type] = status

    def get_weaknesses(self, atk_type: str):
        return self.weakness[atk_type]
