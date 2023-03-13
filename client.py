import aiohttp


class Connect_session:
    
    @classmethod
    async def connect(cls, func, url, pas, api):
        auth = {"password": pas}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=auth, verify_ssl= False) as r:
                json_body = await r.json()
                result = await func(api, session, json_body['accessToken'])
                return result
    
    @classmethod
    async def get_data(cls, url, session, token):
        async with session.get(url=url, headers = {"X-Api-Token":f"{token}"}, ssl= False) as resp:
            node_data = await resp.json()
            return node_data
    
    @classmethod
    async def restart_node(cls, url, session, token):
        async with session.post(url=url, headers = {"X-Api-Token":f"{token}"}, ssl= False) as resp:
            response = await resp.json()
            return response
    
    @classmethod
    async def stop_node(cls, url, session, token):
        async with session.post(url=url, headers = {"X-Api-Token":f"{token}"}, ssl= False) as resp:
            response = await resp.json()
            return response
    