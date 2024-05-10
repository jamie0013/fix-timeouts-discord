import discord
from discord.ext import commands
import calendar, datetime, time
 
# CREDITS -- jamie0013 on Discord or GamingBoss1010 on ROBLOX
# INTENDED USE for cogs, download and run (ensure you load the cog via main file)
# Code is WIP and subject to change/cleanup over time
 
class timeouts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() # testing old print method, ignore
    async def on_ready(self): 
        print("Timeouts cog loaded successfully!")

    @commands.command() # tester command to run & ensure the cog is properly loaded
    async def timeouts(self, ctx):
        await ctx.send(f"timeouts cog loaded 👍")

    @commands.command() # in the channel it's run in, will iterate through all server members, pinging the ones with valid timeouts
    async def checktimers(self, ctx, user: discord.Member=None): # also prints all "invalid" (long expired) timeouts to console
        try:    
            i = 0 # WIP, line can be deleted or commented out
            if user is None: # IF no user specified (eg. only ran CHECKTIMERS)
                for target in ctx.guild.members: # CHECK all members
                    utc_freedom = target.timed_out_until
                    if utc_freedom is not None: 
                        unix_release = calendar.timegm(utc_freedom.utctimetuple())
                        unix_current = time.time()
                        if unix_release > unix_current:
                            await ctx.send(f'{target.mention} / ``{target.id}`` is timed out until <t:{unix_release}>')
                            print(f'user {target.id} - freedom utc: {utc_freedom}')
                            print(f'user {target.id} - freedom unix: {unix_release}')
                        else:
                            print(f'invalid timeout: {target.id} -- expired: {utc_freedom}')
            else: # IF user specified
                if user.timed_out_until is not None: # IF user specified is timedout
                    utc_freedom = user.timed_out_until
                    unix_release = calendar.timegm(utc_freedom.utctimetuple())
                    unix_current = time.time()
                    if unix_release > unix_current: # IF user specified timedout is valid
                        await ctx.send(f'{user.mention} / ``{user.id}`` is timed out until <t:{unix_release}>')
                    else: # IF user specified timedout IS NOT valid
                        await ctx.send(f'specified user {user.mention} / ``{user.id}`` is not currently timed out')
                        print(f'invalid timeout: {user.id} -- expired: {utc_freedom}')
                else: # IF user specified IS NOT timedout
                    await ctx.send(f'specified user {user.mention} / ``{user.id}`` is not currently timed out')
        except Exception as e:
            print(e)

    @commands.command() # iterates through all members, checks for timeouts, ignores the valid ones & fixes the expired/invalid metadata timeouts
    async def fixtimers(self, ctx, user: discord.Member=None): # it achieves this via timing these users out for 3 seconds (adjustable), then fixing it
        try:
            if user is None: # IF no user is specified ...
                for target in ctx.guild.members:
                    if target.id == 360379114932404234: # owner ID -- change if you care, if your being registered (printed) as an expired timeout via CHECKTIMERS command
                        continue
                    elif target.timed_out_until is not None: # AND they are timed out ...
                        utc_endtime = target.timed_out_until
                        unix_endtime = calendar.timegm(utc_endtime.utctimetuple())
                        unix_current = time.time()

                        if unix_endtime < unix_current: # AND their time out is expired ...
                            await ctx.send(f'fixing timeout for user {target.mention} / ``{target.id}``, expired timeout ended at <t:{unix_endtime}>...')
                            await target.timeout(datetime.timedelta(seconds=30))
                            time.sleep(3) # OPTIONAL -- edit time in seconds to leave users timed out before fixing
                            await target.timeout(None)
                            await ctx.send(f"✔ - successfully fixed user {target.mention} / ``{target.id}``'s timeout!")
            else: # IF user is specified ...
                if user.timed_out_until is not None: # AND they are timed out ...
                    utc_endtime = target.timed_out_until
                    unix_endtime = calendar.timegm(utc_endtime.utctimetuple())
                    unix_current = time.time()

                    if unix_endtime < unix_current: # AND their time out is expired ...
                        await ctx.send(f'fixing timeout for user {target.mention} / ``{target.id}``, expired timeout ended at <t:{unix_endtime}>...')
                        await target.timeout(datetime.timedelta(seconds=30))
                        time.sleep(3)
                        await target.timeout(None)
                        await ctx.send(f"✔ - successfully fixed user {target.mention} / ``{target.id}``'s timeout!")
                else: # IF user is specified but they aren't timed out ...
                    await ctx.send(f'specified user {user.mention} / ``{user.id}`` is not currently timed out & has no expired time out')
        except Exception as e:
            print(e)


async def setup(client):
    await client.add_cog(timeouts(client))
