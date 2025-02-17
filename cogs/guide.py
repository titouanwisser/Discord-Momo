import nextcord
import sqlite3
from datetime import datetime
from nextcord import File, ButtonStyle, Embed, Color
from nextcord.ext import commands
from nextcord.ui import Button, View
from assets.momoemotes import emotes

class cGuide(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def GuideMap(self, inter: nextcord.Interaction):
        guideMapEmbed = nextcord.Embed()
        guideMapEmbed.colour = Color.from_rgb(255, 187, 69)
        guideMapEmbed.title = "Infinity Nikki's Map!"
        guideMapEmbed.description = "Interactive map: https://infinity-nikki.interactivemap.app/"
        guideMapEmbed.set_image("https://static.wikia.nocookie.net/infinity-nikki/images/0/0e/Miraland_ver_1.0.png/revision/latest?cb=20241211084241")
        guideMapEmbed.set_footer(text="Source: Infinity Nikki Wiki")
        return guideMapEmbed
    
    def GuideChests(self, inter: nextcord.Interaction):
        guideChestsEmbed = nextcord.Embed()
        guideChestsEmbed.colour = Color.from_rgb(255, 187, 69)
        guideChestsEmbed.title = "Chests Guide!"
        guideChestsEmbed.description = "How to differentiate overworld chests:"
        guideChestsEmbed.set_image("https://cdn.discordapp.com/attachments/1323594235307364412/1323733948307607653/IMG_8874.jpg?ex=67953acf&is=6793e94f&hm=7852b003c1d1e3f0454110fd43ee2a17c3653aa34a20fc8b5f9225cb0835226f&")
        guideChestsEmbed.set_footer(text="Source: Nikkiscord Discord Server")
        return guideChestsEmbed
    
    def GuideEurekas(self, inter: nextcord.Interaction):
        guideEurekasEmbed = nextcord.Embed()
        guideEurekasEmbed.colour = Color.from_rgb(255, 187, 69)
        guideEurekasEmbed.title = "Eurekas and their upgrade colors!"
        guideEurekasEmbed.description = "You can find the guide [**here**](https://infinity-nikki.fandom.com/wiki/Eureka)!"
        guideEurekasEmbed.set_image("https://static.wikia.nocookie.net/infinity-nikki/images/d/dd/Rainbell_%28Head%29_Iridescent.png/revision/latest?cb=20241221222011")
        guideEurekasEmbed.set_footer(text="Source: Infinity Nikki Wiki")
        return guideEurekasEmbed
    
    def GuidePictureTutorial(self, inter: nextcord.Interaction):
        guidePictureTutorialEmbed = nextcord.Embed()
        guidePictureTutorialEmbed.colour = Color.from_rgb(255, 187, 69)
        guidePictureTutorialEmbed.title = "In-depth Picture Tutorial!"
        guidePictureTutorialEmbed.description = "You can find the guide [**here**](https://twitter.com/toradowa/status/1876684194660692087)!"
        guidePictureTutorialEmbed.set_image("https://pbs.twimg.com/media/GgtOy-tXAAAmR6a?format=jpg&name=large")
        guidePictureTutorialEmbed.set_footer(text="Source: Sarah @toradowa")
        return guidePictureTutorialEmbed
    
    def GuidePhotoEditing(self, inter: nextcord.Interaction):
        guidePhotoEditingEmbed = nextcord.Embed()
        guidePhotoEditingEmbed.colour = Color.from_rgb(255, 187, 69)
        guidePhotoEditingEmbed.title = "Tips & Tricks on photo editing!"
        guidePhotoEditingEmbed.description = "You can find the guide [**here**](https://x.com/elfaerealm/status/1882213218292260954?s=46)!"
        guidePhotoEditingEmbed.set_image("https://pbs.twimg.com/media/Gh728aVXUAAwkhB?format=jpg&name=small")
        guidePhotoEditingEmbed.set_footer(text="Source: Ellie @ewellie")
        return guidePhotoEditingEmbed

    @nextcord.slash_command(
        name="guide",
        description="Display a chosen Nikki guide!",
    )   
    async def guide(
        self,
        inter: nextcord.Interaction,
        guide: str = nextcord.SlashOption(
            name="type",
            choices={"Infinity Nikki's Map": "guideMap", "Chests Guide": "guideChests", "Eurekas & their upgrade colors": "guideEurekas",
                    "In-depth Picture Tutorial": "guidePictureTutorial", "Tips & Tricks on photo editing": "guidePhotoEditing"},
        ),
        ):
        if guide == "guideMap":
            await inter.response.send_message(embed=self.GuideMap(inter)) # self is needed to call a method from the same class
        elif guide == "guideChests":
            await inter.response.send_message(embed=self.GuideChests(inter))
        elif guide == "guideEurekas":
            await inter.response.send_message(embed=self.GuideEurekas(inter))
        elif guide == "guidePictureTutorial":
            await inter.response.send_message(embed=self.GuidePictureTutorial(inter))
        elif guide == "guidePhotoEditing":
            await inter.response.send_message(embed=self.GuidePhotoEditing(inter))


def setup(bot: commands.Bot):
    bot.add_cog(cGuide(bot))