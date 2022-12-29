from pprint import pprint as ppr
import requests as req

res = req.get('https://api.vk.com/method/groups.get?user_id=****&v=5.52&access_token=***')

# В запросе выше подставляем в user_id нужный айдишник страницы и свой апи токен в access_token

ppr(res.content)
