from typing import Dict, Tuple, List

from model.game import Game


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

    def get_game(self) -> Game:
        # Checks game by variation name
        if "Persona 3" in self.variation:
            return Game.PERSONA_3
        elif "Persona 4" in self.variation:
            return Game.PERSONA_4
        elif "Persona 5" in self.variation:
            return Game.PERSONA_5

        # Checks game by attack types
        all_attack_types: List[Tuple[str, List[str]]] = [
            (
                "PERSONA_3",
                ["Slash", "Strike", "Pierce", "Fire", "Ice", "Elec", "Wind", "Light", "Dark", "Almi"]
            ),
            (
                "PERSONA_4",
                ["Phys", "Fire", "Ice", "Elec", "Wind", "Light", "Dark", "Almi"]
            ),
            (
                "PERSONA_5",
                ["Phys", "Gun", "Fire", "Ice", "Elec", "Wind", "Psy", "Nuke", "Bless", "Curse", "Almi"]
            )
        ]

        for (game_name, game_attack_types) in all_attack_types:

            if all([game_attack_type in self.weakness.keys() for game_attack_type in game_attack_types]) and \
                    all([attack_type in game_attack_types for attack_type in self.weakness.keys()]):
                return Game[game_name]

        # We don't know what game this is from
        raise Exception(f"Unknown Persona game for variation {self.variation}")
