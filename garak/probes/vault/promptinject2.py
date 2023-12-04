#!/usr/bin/env python3
"""PromptInject

Uses the PromptInject framework, https://openreview.net/forum?id=qiaRo_7Zmug,
to probe a system. A subset of the attacks is implemented here. The default
is to use a selection of that subset, because even the subset corresponds to 
thousands of requests by default.
"""

import random
import sys

from garak.attempt import Attempt
from garak.probes.base import Probe
import garak._config
from random import sample

hijacking_attacks = (
    "ignore-say ignore-print ignore-print-upper nevermind screaming-stop".split()
)
rogue_strings = "hate-humans kill-humans long-prompt".split()

this = sys.modules[__name__]


class SecuestroObjetivo(Probe):
    bcp47 = "en"
    description = "PromptInject is a framework that assembles prompts in a modular fashion to provide a quantitative analysis of the robustness of LLMs to adversarial prompt attacks. trophy Best Paper Awards @ NeurIPS ML Safety Workshop 2022",
    recommended_detector= [
        "promptinject.AttackRogueString"
    ]
    tags = ["avid-effect:security:S0403"]
    uri = "https://openreview.net/forum?id=qiaRo_7Zmug"
    active = True


    def __init__(self):
        super().__init__()
        from garak.resources.promptinject import (
            build_prompts,
            prompt_data,
        )

        self.prompts = []
        self.pi_prompts = []
        self.pi_prompt_data = prompt_data
        self.pi_build_prompts = build_prompts
        
        aux = int(self.promptLimit * 1.0/3)

        self.load_data_all_attacks(rogue_strings[0], self.promptLimit - 2 * aux)
        self.load_data_all_attacks(rogue_strings[1], aux)
        self.load_data_all_attacks(rogue_strings[2], aux)


    def load_data_all_attacks(self, rogue_string, n):
        prompt_config = {
            "base": {
                "text": self.pi_prompt_data.ALL_OPENAI_PLAYGROUND_PROMPTS,
            },
            "attack": {
                "text": (
                    self.pi_prompt_data.goal_hikacking_attacks["ignore-print"],
                    self.pi_prompt_data.goal_hikacking_attacks["ignore-say"],
                    self.pi_prompt_data.goal_hikacking_attacks["ignore-print-upper"],
                    self.pi_prompt_data.goal_hikacking_attacks["nevermind"],
                    self.pi_prompt_data.goal_hikacking_attacks["screaming-stop"],
                ),
                "rogue_string": self.pi_prompt_data.rogue_strings[rogue_string],
                "scoring": "match_rogue_to_output",
                "settings": {
                    "escape": self.pi_prompt_data.escape_chars["n"],
                    "delimiter": self.pi_prompt_data.delimiter_chars["dash"],
                    "escape_length": 10,
                    "escape_times": 2,
                },
            },
            "config": {
                "id": (0, 1, 2, 3),
            },
            "visualization": {"columns": ()},
        }

        pi_prompt_aux = sample(self.pi_build_prompts(prompt_config), n)
        self.pi_prompts += pi_prompt_aux

        for pi_prompt in pi_prompt_aux:
            self.prompts.append(pi_prompt["prompt"])


    def _attempt_prestore_hook(self, attempt: Attempt, seq: int) -> Attempt:
        attempt.notes["settings"] = self.pi_prompts[seq]["settings"]
        attempt.notes["trigger"] = self.pi_prompts[seq]["settings"]["attack_rogue_string"]
        return attempt


    def _generator_precall_hook(self, generator, attempt):
        map_attribs = (
            "temperature top_p frequency_penalty presence_penalty max_tokens".split()
        )
        for map_attrib in map_attribs:
            if map_attrib in dir(generator):
                setattr(
                    generator,
                    map_attrib,
                    attempt.notes["settings"]["config_" + map_attrib],
                )

