import nextcord
from nextcord import Interaction
# Contains all the buttons relevant to dynamis options - relic, tav, DL


# Relic buttons (Head/Body/Hands/Legs/Feet + -1s + Accessory)
class RelicButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Relic Head", style=nextcord.ButtonStyle.red)
    async def head(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Head", ephemeral=True)
        self.drop = 'Head'
        self.stop()

    @nextcord.ui.button(label="Relic Body", style=nextcord.ButtonStyle.red)
    async def body(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Body", ephemeral=True)
        self.drop = 'Body'
        self.stop()

    @nextcord.ui.button(label="Relic Hands", style=nextcord.ButtonStyle.red)
    async def hands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Hands", ephemeral=True)
        self.drop = 'Hands'
        self.stop()

    @nextcord.ui.button(label="Relic Legs", style=nextcord.ButtonStyle.red)
    async def legs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Legs", ephemeral=True)
        self.drop = 'Legs'
        self.stop()

    @nextcord.ui.button(label="Relic Feet", style=nextcord.ButtonStyle.red)
    async def feet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Feet", ephemeral=True)
        self.drop = 'Feet'
        self.stop()

    @nextcord.ui.button(label="Relic Accessory", style=nextcord.ButtonStyle.red)
    async def accessory(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Accessory", ephemeral=True)
        self.drop = 'Accessory'
        self.stop()

    @nextcord.ui.button(label="Relic Head -1", style=nextcord.ButtonStyle.red)
    async def head_mone(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Head -1", ephemeral=True)
        self.drop = 'Head -1'
        self.stop()

    @nextcord.ui.button(label="Relic Body -1", style=nextcord.ButtonStyle.red)
    async def body_mone(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Body -1", ephemeral=True)
        self.drop = 'Body -1'
        self.stop()

    @nextcord.ui.button(label="Relic Hands", style=nextcord.ButtonStyle.red)
    async def hands_mone(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Hands -1", ephemeral=True)
        self.drop = 'Hands -1'
        self.stop()

    @nextcord.ui.button(label="Relic Legs -1", style=nextcord.ButtonStyle.red)
    async def legs_mone(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Legs -1", ephemeral=True)
        self.drop = 'Legs -1'
        self.stop()

    @nextcord.ui.button(label="Relic Feet -1", style=nextcord.ButtonStyle.red)
    async def feet_mone(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Relic Feet -1", ephemeral=True)
        self.drop = 'Feet -1'
        self.stop()


# Dyna lord item buttons (ring/mantle)
class DynaLButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Shadow Ring", style=nextcord.ButtonStyle.red)
    async def shad_ring(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Shadow Ring", ephemeral=True)
        self.drop = 'Shadow Ring'
        self.stop()

    @nextcord.ui.button(label="Shadow Mantle", style=nextcord.ButtonStyle.red)
    async def shad_mantle(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Shadow Mantle", ephemeral=True)
        self.drop = 'Shadow Mantle'
        self.stop()


# Dyna tav buttons (currently not coded)
class DynaTButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Placeholder", style=nextcord.ButtonStyle.red)
    async def shad_ring(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Placeholder", ephemeral=True)
        self.drop = 'Placeholder'
        self.stop()


