import nextcord
import sqlite3
from nextcord.ext import commands
from assets.momoemotes import emotes
from assets.neededxp import neededXp

class cLvlEvent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        user = message.author.id
        if user != 1326586963603619995:
            try:
                conn = sqlite3.connect('momodb.db')
                cur = conn.cursor()
                cur.execute(f'SELECT xp, totalxp, level FROM users WHERE userID = ? AND guildid = ?', (user, message.guild.id,))
                results = cur.fetchone()

                if results is None:
                    cur.execute(f'INSERT INTO users (userid, level, totalxp, xp, blings, lastdailypull, lastdailyblings, guildid) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (user, 1, 1, 1, 0, '2000-01-01', '2000-01-01', message.guild.id))
                    cur.execute(f'SELECT xp, totalxp, level FROM users WHERE userID = ? AND guildid = ?', (user, message.guild.id))
                    results = cur.fetchone()

                old_xp = results[0] ##the first item in the index, in this case, xp
                old_level = results[2] ## the second item in the index, in this case, level
                perm_xp = results[1]+1
                new_xp = old_xp + 1
                if new_xp == neededXp: #this is where you set the threshold for leveling up to the first level
                    new_level = old_level+1
                    new_xp = 0
                    await message.channel.send(f":up: Congrats {message.author.mention}, you gained a **Mira Level** {emotes['emoteMiraLevel']}, **10,000 Blings** {emotes["emoteBling"]} and you are now Level **{new_level}**!")
                    cur.execute("SELECT blings FROM users WHERE userid = ? AND guildid = ?", (message.author.id, message.guild.id))
                    userBalance = cur.fetchone()[0]
                    cur.execute("UPDATE users SET blings = ? WHERE userid = ? AND guildid = ?", (userBalance+10000, message.author.id, message.guild.id))
                else:
                    new_level = old_level
                ###add more logic here for successive level-ups
                cur.execute('UPDATE users SET xp = ?, totalXp = ?, level = ? WHERE userid = ? AND guildid = ?', (new_xp, perm_xp, new_level, user, message.guild.id))
                conn.commit()
                conn.close()
            except:
                pass

def setup(bot: commands.Bot):
    bot.add_cog(cLvlEvent(bot))