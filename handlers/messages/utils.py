from client import Connect_session
from data import load_config
import datetime
import asyncio

config = load_config(r"config.ini")
hosts = config.nodes.node_ips.split('\n')
pasws = config.nodes.passwords.split('\n')
apis = config.nodes.api_urls.split('\n')

class Connection:
    
    @classmethod
    async def main(cls):
        res = await asyncio.gather(*(cls.connect(cls, host, pas, api) for host, pas, api in cls.iterator(cls)))
        return ''.join(str(i) for i in res)
    
    async def connect(cls, host, pas, api):
        result = await Connect_session.connect(url=host, pas=pas, api=api, func = Connect_session.get_data)
        return cls.clear_info(cls, result)
    
    def iterator(cls):
        for host, pas, api in zip(hosts, pasws, apis):
            yield host, pas, api
        
    def clear_info(cls, result):
        if result['state'] == "stopped":
            clear_message = f"*Статус ноды:* {result['state']}\
                            \n*Adress:* {result['nominatorAddress']}\
                            \n*Message:* {result['exitMessage']}\
                            \n*StatusCode:* {result['exitStatus']}\
                            \n\n"  
        else: 
            clear_message = f"*Статус ноды:* {result['state']}\
                            \n*Adress:* {result['nominatorAddress']}\
                            \n*Last_work:* {result['lastActive']}\
                            \n*Rewards:* {cls.rounder(cls, result['currentRewards'])}\
                            \n*IP:* {result['nodeInfo']['externalIp']}\
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
