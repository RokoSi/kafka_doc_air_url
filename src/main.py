# -*- coding: utf-8 -*-
import logging
import os
import random

from settings import settings
from cli.count_user_add_menu import count_user_add_menu
from producer import get_msg_json
from validators import validator_pass

log_dir = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_dir, "logfile.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    filemode="a",
    encoding="utf-8",
    level=logging.INFO,
    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
log = logging.getLogger(__name__)


def main():
    person = []

    users = count_user_add_menu(settings.url, random.randint(1, 3))
    if users:
        for user in users:
            valid_pass = validator_pass(user["login"]["password"])
            user["valid"] = valid_pass

            person.append(user)

        if len(person):
            get_msg_json(person)

    else:
        exit(1)


if __name__ == "__main__":
    main()
