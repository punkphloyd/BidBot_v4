import nextcord
from nextcord import Interaction
from utils import ephemeral
# Contains all the buttons relevant to battlefields (WTB, Bahav2, KS99s)


# Waking the Beast Buttons
class WTBButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Carbuncle's Cuffs", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Carbuncle's Cuffs", ephemeral=ephemeral)
        self.drop = 'Carbuncle\'s Cuffs'
        self.stop()

    @nextcord.ui.button(label="Garuda's Sickle", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Garuda's Sickle", ephemeral=ephemeral)
        self.drop = 'Garuda\'s Sickle'
        self.stop()

    @nextcord.ui.button(label="Ifrit's Bow", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ifrit's Bow", ephemeral=ephemeral)
        self.drop = 'Ifrit\'s Bow'
        self.stop()

    @nextcord.ui.button(label="Leviathan's Couse", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Leviathan's Couse", ephemeral=ephemeral)
        self.drop = 'Leviathan\'s Couse'
        self.stop()

    @nextcord.ui.button(label="Ramuh's Mace", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ramuh's Mace", ephemeral=ephemeral)
        self.drop = 'Ramuh\'s Mace'
        self.stop()

    @nextcord.ui.button(label="Shiva\'s Shotel", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Shiva\'s Shotel", ephemeral=ephemeral)
        self.drop = 'Shiva\'s Shotel'
        self.stop()

    @nextcord.ui.button(label="Titan\'s Baselard", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Titan\'s Baselard", ephemeral=ephemeral)
        self.drop = 'Titan\'s Baselard'
        self.stop()

    @nextcord.ui.button(label="Yinyang Robe", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Yinyang Robe", ephemeral=ephemeral)
        self.drop = 'Yinyang Robe'
        self.stop()


class BahamutButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Bahamut\'s Mask", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Bahamut\'s Mask", ephemeral=ephemeral)
        self.drop = 'Bahamut\'s Mask'
        self.stop()

    @nextcord.ui.button(label="Bahamut\'s Robe", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Bahamut\'s Robe", ephemeral=ephemeral)
        self.drop = 'Bahamut\'s Robe'
        self.stop()

    @nextcord.ui.button(label="Bahamut\'s Zaghnal", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Bahamut\'s Zaghnal", ephemeral=ephemeral)
        self.drop = 'Bahamut\'s Zaghnal'
        self.stop()

    @nextcord.ui.button(label="Bahamut\'s Staff", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Bahamut\'s Staff", ephemeral=ephemeral)
        self.drop = 'Bahamut\'s Staff'
        self.stop()

    @nextcord.ui.button(label="Dragon Staff", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dragon Staff", ephemeral=ephemeral)
        self.drop = 'Dragon Staff'
        self.stop()


class KS99Buttons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Adamantoise Egg", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Adamantoise Egg", ephemeral=ephemeral)
        self.drop = 'Adamantoise Egg'
        self.stop()

    @nextcord.ui.button(label="Behemoth Tongue", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Behemoth Tongue", ephemeral=ephemeral)
        self.drop = 'Behemoth Tongue'
        self.stop()

    @nextcord.ui.button(label="Wyrm Beard", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Wyrm Beard", ephemeral=ephemeral)
        self.drop = 'Wyrm Beard'
        self.stop()