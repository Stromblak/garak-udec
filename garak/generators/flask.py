from typing import List

import backoff

from garak._config import args
from garak.generators.base import Generator
import requests


class HFRateLimitException(Exception):
    pass


class HFLoadingException(Exception):
    pass


class HFInternalServerError(Exception):
    pass


default_class = "Flask"

class Flask(Generator):
    generator_family_name = "Flask API"

    def __init__(self, name="", api_url="http://127.0.0.1:5000/prompt", generations=10):
        self.api_url = api_url
        super().__init__(name, generations=generations)
        self.deprefix_prompt = True
        self.max_time = 30

    @backoff.on_exception(
        backoff.fibo,
        (HFRateLimitException, HFLoadingException, HFInternalServerError),
        max_value=125,
    )
    
    def _call_api(self, prompt: str) -> List[str]:
        payload = {
            "prompt": prompt,  # Adjust the payload to match your API expectations
        }

        req_response = requests.post(
            self.api_url,  # Adjust the URL to your Flask endpoint
            json=payload,
        )

        if req_response.status_code == 405:
            raise HFInternalServerError("Method Not Allowed")

        # Handle other HTTP status codes and exceptions as needed...

        response = req_response.json()

        if isinstance(response, dict) and "response" in response:
            return [response["response"]]
        else:
            raise IOError(f"Unexpected API response: {response}")


    def generate(self, prompt):
        self.wait_for_model = False
        return self._call_api(prompt)
