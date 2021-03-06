#!/usr/bin/env python3

import hmac
import json
import os
import os.path
import random
import shutil
import sys
import subprocess
import tempfile

PREFIX = "ugra_when_i_was_this_small_it_already_had_a_beard_that_long_"
SECRET = b"woodpecker-almond-bother-big-reverberation"
SALT_SIZE = 12

def get_flag():
    user_id = sys.argv[1]
    return PREFIX + hmac.new(SECRET, str(user_id).encode(), "sha256").hexdigest()[:SALT_SIZE]


def generate():
    if len(sys.argv) < 3:
        print("Usage: generate.py user_id target_dir", file=sys.stderr)
        sys.exit(1)
    user_id = sys.argv[1]
    target_dir = sys.argv[2]

    random.seed(hmac.new(SECRET, str(user_id).encode(), "sha256").digest())

    flag = get_flag()

    with tempfile.TemporaryDirectory() as temp_dir:
        rar_cmd = f"rar a -rr{random.randint(4, 100)} -m{random.randint(0, 5)} unrar.rar unrar"
        open(os.path.join(temp_dir, "rar.sh"), "w").write(rar_cmd)
        shutil.copy(os.path.join("private", "unrar"), os.path.join(temp_dir, "unrar"))

        image_name = subprocess.run(["docker", "build", "-q", "-f", "Dockerfile", temp_dir],
                                    capture_output=True, check=True).stdout.decode("utf-8").strip()
        container_name = subprocess.run(["docker", "create", image_name],
                                        capture_output=True, check=True).stdout.decode("utf-8").strip()
        subprocess.check_call(["docker", "cp", f"{container_name}:/root/unrar.rar",
                               os.path.join(temp_dir, "unrar.rar")], stdout=subprocess.DEVNULL)
        subprocess.check_call(["docker", "rm", container_name], stdout=subprocess.DEVNULL)

        content = list(open(os.path.join(temp_dir, "unrar.rar"), "rb").read())
        offset = random.randint(2000, 8000)
        for n, i in enumerate(flag):
            content[offset + n] ^= ord(i)
        open(os.path.join(target_dir, "unrar.rar"), "wb").write(bytes(content))

    json.dump({"flags": [flag], "substitutions": {}, "urls": []}, sys.stdout)


if __name__ == "__main__":
    generate()
