from requests_html import AsyncHTMLSession, HTMLSession

session = HTMLSession()
asession = AsyncHTMLSession()

async def get_homepage():
    r = await asession.get("https://docinfo.org/")
    return r.text

print(asession.run(get_homepage))