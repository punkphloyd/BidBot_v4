import nextcord
from nextcord import Interaction
# Contains Limbus buttons (present omega/ultima) with homam/nashira


class OmegaButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Homam Zucchetto", style=nextcord.ButtonStyle.red)
    async def homamhead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Homam Zucchetto", ephemeral=True)
        self.drop = 'Homam Zucchetto'
        self.stop()

    @nextcord.ui.button(label="Homam Corazza", style=nextcord.ButtonStyle.red)
    async def homambody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Homam Corazza", ephemeral=True)
        self.drop = 'Homam Corazza'
        self.stop()

    @nextcord.ui.button(label="Homam Manopolas", style=nextcord.ButtonStyle.red)
    async def homamhands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Homam Manopolas", ephemeral=True)
        self.drop = 'Homam Manopolas'
        self.stop()

    @nextcord.ui.button(label="Homam Cosciales", style=nextcord.ButtonStyle.red)
    async def homamlegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Homam Cosciales", ephemeral=True)
        self.drop = 'Homam Cosciales'
        self.stop()

    @nextcord.ui.button(label="Homam Gambeiras", style=nextcord.ButtonStyle.red)
    async def homamhead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Homam Gambeiras", ephemeral=True)
        self.drop = 'Homam Gambeiras'
        self.stop()


class UltimaButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Nashira Turban", style=nextcord.ButtonStyle.red)
    async def nashhead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Nashira Turban", ephemeral=True)
        self.drop = 'Nashira Turban'
        self.stop()

    @nextcord.ui.button(label="Nashira Manteel", style=nextcord.ButtonStyle.red)
    async def nashbody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Nashira Manteel", ephemeral=True)
        self.drop = 'Nashira Manteel'
        self.stop()

    @nextcord.ui.button(label="Nashira Gages", style=nextcord.ButtonStyle.red)
    async def nashhands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Nashira Gages", ephemeral=True)
        self.drop = 'Nashira Gages'
        self.stop()

    @nextcord.ui.button(label="Nashira Seraweels", style=nextcord.ButtonStyle.red)
    async def nashlegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Nashira Seraweels", ephemeral=True)
        self.drop = 'Nashira Seraweels'
        self.stop()

    @nextcord.ui.button(label="Nashira Crackows", style=nextcord.ButtonStyle.red)
    async def nashfeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Nashira Crackows", ephemeral=True)
        self.drop = 'Nashira Crackows'
        self.stop()