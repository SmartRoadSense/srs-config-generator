from pathlib import Path  # python3 only
import re
import sys


def load_env2var(file_path=""):
    envre = re.compile(r'''^([^\s=]+)=(?:[\s"']*)(.+?)(?:[\s"']*)$''')
    result = {}
    with open(file_path) as ins:
        for line in ins:
            match = envre.match(line)
            if match is not None:
                result[match.group(1)] = match.group(2)

    return result


base_path = str(sys.argv[1]) if len(sys.argv) > 1 else "."
srs_env_path = Path(base_path) / 'srs.env'
template_env_path = Path(base_path) / 'config.env-template'
config_env_path = Path(base_path) / 'config.env'

srs_env = load_env2var(srs_env_path)
template_env = load_env2var(template_env_path)

print(srs_env)
print(template_env)

env_file = open(config_env_path, "w+", newline='\n')

for variable, placeholder in template_env.items():
    #print(variable, ":", placeholder)
    value = srs_env.get(placeholder)
    value = "" if value is None else value
    env_file.write("{0}={1}\n".format(variable, value))
    print(variable, ":", value)

env_file.close()
