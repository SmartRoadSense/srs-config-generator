from dotenv import load_dotenv
import os
from pathlib import Path  # python3 only
import re


def load_env2var(file_path=""):
    envre = re.compile(r'''^([^\s=]+)=(?:[\s"']*)(.+?)(?:[\s"']*)$''')
    result = {}
    with open(file_path) as ins:
        for line in ins:
            match = envre.match(line)
            if match is not None:
                result[match.group(1)] = match.group(2)

    return result


srs_env_path = Path('.') / 'srs.env'
template_env_path = Path('.') / 'config.env-template'
config_env_path = Path('.') / 'config.env'

load_dotenv(dotenv_path=srs_env_path, verbose=True)
template_env = load_env2var(template_env_path)
env_file = open(config_env_path, "w+", newline='\n')

for variable, placeholder in template_env.items():
    print(variable, ":", placeholder)
    value = os.getenv(placeholder)
    value = "" if value is None else value

    env_file.write("{0}={1}\n".format(variable, value))

env_file.close()

