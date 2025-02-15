import asyncio
import aiohttp

SERVICES = [
    ("https://api.ipify.org?format=json", "ipify"),
    ("http://ip-api.com/json", "ip-api"),
    ("https://ifconfig.me/all.json", "ifconfig.me"),
]


async def fetch_ip(session, url, name):
    try:
        async with session.get(url, timeout=5) as response:
            if response.status == 200:
                data = await response.json()
                ip = data.get("ip") or data.get("query") or data.get("ip_address")
                return ip, name
    except Exception as e:
        return None, name


async def get_first_available_ip():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_ip(session, url, name) for url, name in SERVICES]
        for coro in asyncio.as_completed(tasks):
            ip, name = await coro
            if ip:
                return ip, name
    return None, None


async def main():
    ip, service = await get_first_available_ip()
    if ip:
        print(f"Your IP is {ip}, provided by {service}.")
    else:
        print("Unable to fetch IP from any service.")


if __name__ == "__main__":
    asyncio.run(main())
