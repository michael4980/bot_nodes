import configparser
from dataclasses import dataclass


@dataclass
class Nodes:
    node_ips: list
    passwords: list
    api_urls: list
    nums: list

@dataclass
class Node_1:
    ip: str
    password: str
    api_status: str
    api_start: str
    api_stop: str
    
@dataclass
class Node_2:
    ip: str
    password: str
    api_status: str
    api_start: str
    api_stop: str
    
@dataclass
class Bot:
    token: str


@dataclass
class Config:
    bot: Bot
    nodes: Nodes
    node1: Node_1
    node2: Node_2


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        bot = Bot(**config["bot"]),
        nodes = Nodes(**config["nodes"]),
        node1 = Node_1(**config["node1"]),
        node2 = Node_2(**config["node2"])
    )