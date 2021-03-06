import pinkconf as p
import emotes as e
import discord

def help_main():
    acc = 'Type !help [topic] for more detailed information about the following:\n'
    for topic in help_dict:
        acc += '- {}\n'.format(topic)
    return '```{}```'.format(acc)

new = discord.Embed(title='Create a new account: !new', colour=discord.Colour.orange(),
description='''
An account is required to use the bot. (No personal details required)
Be sure to also read the !rules and !terms.''')

bal = discord.Embed(title='Check your balance: !bal !balance', colour=discord.Colour.orange(),
description='''
Checks your current balance and shows your deposit address.
To get a clipboard friendly address, use !addr.
Deposits should arrive within 5 minutes of a transaction taking place.
If the bot is offline, you are still safe to make deposits.''')

wdr = discord.Embed(title='Withdraw your funds: !wdr !withdraw !send', colour=discord.Colour.orange(),
description='''
**Format: !wdr [address to send to] [amount-PINK]**

Takes your PINK out of the bot's wallet.
Fee for withdraw is {} PINK and is automatically deducted.
If you wish to transfer to another user, use !give instead.'''.format(p.tx_fee))

donate = discord.Embed(title='Donate to someone: !donate', colour=discord.Colour.orange(),
description='''
**Format: !donate [selection no.] [amount-PINK]**

Type just !donate to see a list of possible donation options.
Choose a number from the list of selections and then choose the amount to donate.
Fees here are regular network fees.''')

rdonate = discord.Embed(title='Donate to a random contributor: !rdonate', colour=discord.Colour.orange(),
description='''
**Format: !rdonate [amount-PINK]**

Same as !donate but a random person on the bot's donation list is chosen for you.''')

give = discord.Embed(title='Give funds to another user: !give !tip', colour=discord.Colour.orange(),
description='''
**Format: !give [discord mention of user] [amount-PINK]**

Give some PINK to another person within the server. (no fees apply)
Requires the mentioned user to also have an account with the bot through !new.''')

rain = discord.Embed(title='Rain on active users: !rain', colour=discord.Colour.orange(),
description='''
**Format: !rain [amount-PINK]**

Typing !rain on its own will display the current rain balance and threshold.
Once the balance of the rainbot exceeds the threshold, it will rain on all **online** users.''')

faucet = discord.Embed(title='Get some free PINK: !faucet !get', colour=discord.Colour.orange(),
description='''
Type this command to get some free Pinkcoins.
Amounts are random and you can only request once per {} hours.
To help fund the faucet, you can type `!fgive [amount-PINK]`.'''.format(p.FCT_REQ_LIM))

qr = discord.Embed(title='Generate a QR code: !qr', colour=discord.Colour.orange(),
description='''
**Format: !qr [optional data]**

Generates a qr code. If no data is given, it will send a QR code of your
wallet address. Any data given must contain no spaces.''')

block = discord.Embed(title='Explore blocks on the Pinkcoin network: !block', colour=discord.Colour.orange(),
description='''
**Format: !block [height]**

Fetches information about a particular block on the Pinkcoin blockchain.''')

status = discord.Embed(title='Bot and network status: !status', colour=discord.Colour.orange(),
description='''
Check the bot status to see whether it is online and observe some basic stats.''')

time = discord.Embed(title='Show your timeouts: !time', colour=discord.Colour.orange(),
description='''
Shows faucet, withdrawal and donation availability and time until eligibility.''')

rules_help = discord.Embed(title='Show the bot rules: !rules', colour=discord.Colour.orange(),
description='''
Rules about using the bot and what may result in a ban.''')

terms_help = discord.Embed(title='Show the bot terms: !terms', colour=discord.Colour.orange(),
description='''
Terms and conditions for making an account with the bot that you automatically accept by typing !new.''')

info_help = discord.Embed(title='Information about the bot: !info', colour=discord.Colour.orange(),
description='''
Shows information about authors and contributors.''')

help_dict = {
    'new'       :   new,
    'balance'   :   bal,
    'withdraw'  :   wdr,
    'donate'    :   donate,
    'rdonate'   :   rdonate,
    'give'      :   give,
    'rain'      :   rain,
    'faucet'    :   faucet,
    'qr'        :   qr,
    'block'     :   block,
    'status'    :   status,
    'time'      :   time,
    'rules'     :   rules_help,
    'terms'     :   terms_help,
    'info'      :   info_help
}
