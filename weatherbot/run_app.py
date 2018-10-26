#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


C="Hóla"
print(C)
print(len(C))
print(len(C.encode('utf-8')))
nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-466411853734-464845534772-Bd6b7a74B1NxiBVYyCNIF7Ou')

agent.handle_channels([input_channel], 5004, serve_forever=True)
