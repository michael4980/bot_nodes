from client import Connect_session
from data import load_config
import datetime
import asyncio

config = load_config(r"config.ini")
hosts = config.nodes.node_ips.split('\n')
pasws = config.nodes.passwords.split('\n')
apis = config.nodes.api_urls.split('\n')
nums = config.nodes.nums.split('\n')

class Node:
    
    @classmethod
    async def main(cls):
        res = await asyncio.gather(*(cls.connect(host, pas, api, num, cls.clear_info) for host, pas, api, num in cls.iterator(cls)))
        return ''.join(str(i) for i in res)
    
    @classmethod
    async def connect(cls, host, pas, api, num, func):
        result = await Connect_session.connect(url=host, pas=pas, api=api, func = Connect_session.get_data)
        return func(result, num)
    
    @classmethod
    async def connect_detail(cls, host, pas, api):
        result = await Connect_session.connect(url=host, pas=pas, api=api, func = Connect_session.get_data)
        return result
    
    @classmethod
    async def start_node(cls, host, pas, api):
        result = await Connect_session.connect(url=host, pas=pas, api=api, func = Connect_session.restart_node)
        return result
    
    @classmethod
    async def stop_node(cls, host, pas, api):
        result = await Connect_session.connect(url=host, pas=pas, api=api, func = Connect_session.stop_node)
        return result
    
    def iterator(cls):
        for host, pas, api, num in zip(hosts, pasws, apis, nums):
            yield host, pas, api, num
    
    @classmethod  
    def clear_info(cls, result, num):
        if result['state'] == "stopped":
            clear_message = f"*Number node:* /{num}\
                            \n\n*Статус ноды:* {result['state']}\
                            \n*Adress:* {result['nominatorAddress']}\
                            \n*Message:* {result['exitMessage']}\
                            \n*StatusCode:* {result['exitStatus']}\
                            \n\n"  
        else: 
            clear_message = f"*Number node:* /{num}\
                            \n\n*Статус ноды:* {result['state']}\
                            \n*Adress:* {result['nominatorAddress']}\
                            \n*Last_work:* {result['lastActive']}\
                            \n*Rewards:* {cls.rounder(cls, result['currentRewards'])}\
                            \n*Time:* {result['totalTimeRunning']}\
                            \n\n"                   
        return clear_message  

    def get_time(cls, time):
        if isinstance(time, int):
            dt = datetime.datetime.fromtimestamp(int(time)/1000)
            return dt
    
    def rounder(cls, earns):
        try:
            result = round(float(earns), 2)
            return result
        except ValueError:
            return 'no earns yet'
    
    @classmethod
    def clear_details_info(cls, result, num):
        if result['state'] == "stopped":
            clear_message = f"*Number node:* /{num}\
                            \n\n*Статус ноды:* {result['state']}\
                            \n*Message:* {result['exitMessage']}\
                            \n*StatusCode:* {result['exitStatus']}\
                            \n\n"  
        else: 
            clear_message = f"*Number node:* /{num}\
                            \n\n*Статус ноды:* {result['state']}\
                            \n*Adress:* {result['nominatorAddress']}\
                            \n\n"                   
        return clear_message
