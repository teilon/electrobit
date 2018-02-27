import asyncio
from pyppeteer.launcher import launch

async def main(browser):
    page = await browser.newPage()
    await page.goto('http://saiman.kz/')
    await page.screenshot({'path': 'example.png'})

    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)

browser = launch()
asyncio.get_event_loop().run_until_complete(main(browser))
browser.close()
