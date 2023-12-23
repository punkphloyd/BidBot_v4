import nextcord
from nextcord import Interaction
# Buttons for the numerous HNMs available in the bidding system (ground kings, etc.)


class RocsButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Trotter Boots", style=nextcord.ButtonStyle.red)
    async def trotters(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Trotter Boots", ephemeral=True)
        self.drop = 'Trotter Boots'
        self.stop()

    @nextcord.ui.button(label="Rucke\'s Rung", style=nextcord.ButtonStyle.red)
    async def ruckes(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Rucke\'s Rung", ephemeral=True)
        self.drop = 'Rucke\'s Rung'
        self.stop()

    @nextcord.ui.button(label="Luftpause Mark", style=nextcord.ButtonStyle.red)
    async def luftpause(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Luftpause Mark", ephemeral=True)
        self.drop = 'Luftpause Mark'
        self.stop()

    @nextcord.ui.button(label="Vaulter\'s Ring", style=nextcord.ButtonStyle.red)
    async def vaulters(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Vaulter\'s Ring", ephemeral=True)
        self.drop = 'Vaulter\'s Ring'
        self.stop()


class DecapodButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Duality Loop", style=nextcord.ButtonStyle.red)
    async def duality(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Duality Loop", ephemeral=True)
        self.drop = 'Duality Loop'
        self.stop()

    @nextcord.ui.button(label="Sprinter\'s Belt", style=nextcord.ButtonStyle.red)
    async def sprinters(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Sprinter\'s Belt", ephemeral=True)
        self.drop = 'Sprinter\'s Belt'
        self.stop()

    @nextcord.ui.button(label="Overlord\'s Ring", style=nextcord.ButtonStyle.red)
    async def overlords(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Overlord\'s Ring", ephemeral=True)
        self.drop = 'Overlord\'s Ring'
        self.stop()

    @nextcord.ui.button(label="Deflecting Band", style=nextcord.ButtonStyle.red)
    async def deflecting(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Deflecting Band", ephemeral=True)
        self.drop = 'Deflecting Band'
        self.stop()


class ScorpButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Horus\'s Helm", style=nextcord.ButtonStyle.red)
    async def horus(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Horus\'s Helm", ephemeral=True)
        self.drop = 'Horus\'s Helm'
        self.stop()

    @nextcord.ui.button(label="Carapace Bullet", style=nextcord.ButtonStyle.red)
    async def cbullet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Carapace Bullet", ephemeral=True)
        self.drop = 'Carapace Bullet'
        self.stop()

    @nextcord.ui.button(label="Dilation Ring", style=nextcord.ButtonStyle.red)
    async def dilation(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dilation Ring", ephemeral=True)
        self.drop = 'Dilation Ring'
        self.stop()

    @nextcord.ui.button(label="Unknown", style=nextcord.ButtonStyle.red)
    async def unknown(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Unknown", ephemeral=True)
        self.drop = 'Unknown'
        self.stop()
