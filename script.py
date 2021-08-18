import time
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed


def get_status(links):
    for x in links:
        response = requests.get(x).text

        get_name = response.split('<h2 class="expand-sum-sysname">')[1].split('</h2>')[0]
        get_price = response.split('<span class="expand-sum-price">')[1].split('</span>')[0]

        get_cpu = response.split('<dd mdata="CPU"><strong>CPU:</strong>')[1].split('</dd>')[0].strip()
        get_gpu = response.split('<dd mdata="VIDEO"><strong>Video Card:</strong>')[1].split('</dd>')[0].strip()
        get_ram = response.split('<dd mdata="MEMORY"><strong>RAM / System Memory:</strong>')[1].split('</dd>')[0].strip()

        get_shipdate = response.split('<strong id="sys_ship_date">')[1].split('</strong>')[0].strip()

        if "Out of stock" in response:
            pass
        else:
            print(f"{get_name} in stock, webhook sent!")
            send_webhook(f"**{get_name} IN STOCK!**\n\n**Specifications**:\nGraphics Card: {get_gpu}\nProcessor: {get_cpu}\nMemory: {get_ram}\n\nPrice: {get_price}\nEstimated Shipping Date: {get_shipdate}")
            time.sleep(600)
    time.sleep(60)
    main()


def send_webhook(text):
    webhook = DiscordWebhook(url="discord webhook goes here")
    embed = DiscordEmbed(description=text, color='FF4500')
    embed.set_footer(text='Cyberpower Logs - by carl#0666', icon_url='https://www.pngitem.com/pimgs/m/592-5924082_cyberpower-pc-logo-hd-png-download.png')
    webhook.add_embed(embed)

    response = webhook.execute()


def main():
    array = []
    with open('links.txt', "r") as f:
        for x in f:
            array.append(x.strip())
    get_status(array)


main()
