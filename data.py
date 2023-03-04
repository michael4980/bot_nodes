import configparser
from dataclasses import dataclass


@dataclass
class Nodes:
    node_ips: list
    passwords: list
    api_urls: list


@dataclass
class Bot:
    token: str


@dataclass
class Config:
    bot: Bot
    nodes: Nodes


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        bot = Bot(**config["bot"]),
        nodes = Nodes(**config["nodes"]),
    )