import nextcord
from nextcord import Interaction
# Buttons for sea gods (AV / Jailers / Aerns)


class AVButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Novio Earring", style=nextcord.ButtonStyle.blurple)
    async def novio(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Novio Earring", ephemeral=True)
        self.drop = 'Novio Earring'
        self.stop()

    @nextcord.ui.button(label="Novia Earring", style=nextcord.ButtonStyle.blurple)
    async def novia(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Novia Earring", ephemeral=True)
        self.drop = 'Novia Earring'
        self.stop()


class LoveButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Love Halberd", style=nextcord.ButtonStyle.blurple)
    async def lhalberd(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Love Halberd", ephemeral=True)
        self.drop = 'Love Halberd'
        self.stop()

    @nextcord.ui.button(label="Love Torque", style=nextcord.ButtonStyle.blurple)
    async def ltorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Love Torque", ephemeral=True)
        self.drop = 'Love Torque'
        self.stop()


class JusticeButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Justice Sword", style=nextcord.ButtonStyle.blurple)
    async def jsword(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Justice Sword", ephemeral=True)
        self.drop = 'Justice Sword'
        self.stop()

    @nextcord.ui.button(label="Justice Torque", style=nextcord.ButtonStyle.blurple)
    async def jtorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Justice Torque", ephemeral=True)
        self.drop = 'Justice Torque'
        self.stop()


class HopeButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Hope Staff", style=nextcord.ButtonStyle.blurple)
    async def hstaff(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Hope Staff", ephemeral=True)
        self.drop = 'Hope Staff'
        self.stop()

    @nextcord.ui.button(label="Hope Torque", style=nextcord.ButtonStyle.blurple)
    async def htorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Hope Torque", ephemeral=True)
        self.drop = 'Hope Torque'
        self.stop()


class PrudenceButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Prudence Rod", style=nextcord.ButtonStyle.blurple)
    async def prod(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Prudence Rod", ephemeral=True)
        self.drop = 'Prudence Rod'
        self.stop()

    @nextcord.ui.button(label="Prudence Torque", style=nextcord.ButtonStyle.blurple)
    async def htorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Prudence Torque", ephemeral=True)
        self.drop = 'Prudence Torque'
        self.stop()


class FortitudeButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Fortitude Axe", style=nextcord.ButtonStyle.blurple)
    async def foaxe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Fortitude Axe", ephemeral=True)
        self.drop = 'Fortitude Axe'
        self.stop()

    @nextcord.ui.button(label="Fortitude Torque", style=nextcord.ButtonStyle.blurple)
    async def fotorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Fortitude Torque", ephemeral=True)
        self.drop = 'Fortitude Torque'
        self.stop()


class TemperanceButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Temperance Axe", style=nextcord.ButtonStyle.blurple)
    async def taxe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Temperance Axe", ephemeral=True)
        self.drop = 'Temperance Axe'
        self.stop()

    @nextcord.ui.button(label="Temperance Torque", style=nextcord.ButtonStyle.blurple)
    async def ttorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Temperance Torque", ephemeral=True)
        self.drop = 'Temperance Torque'
        self.stop()


class FaithButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Faith Baghnakhs", style=nextcord.ButtonStyle.blurple)
    async def fabaghnakhs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Faith Baghnakhs", ephemeral=True)
        self.drop = 'Faith Baghnakhs'
        self.stop()

    @nextcord.ui.button(label="Faith Torque", style=nextcord.ButtonStyle.blurple)
    async def fatorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Faith Torque", ephemeral=True)
        self.drop = 'Faith Torque'
        self.stop()


class FaithButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Faith Baghnakhs", style=nextcord.ButtonStyle.blurple)
    async def fabaghnakhs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Faith Baghnakhs", ephemeral=True)
        self.drop = 'Faith Baghnakhs'
        self.stop()

    @nextcord.ui.button(label="Faith Torque", style=nextcord.ButtonStyle.blurple)
    async def fatorque(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Faith Torque", ephemeral=True)
        self.drop = 'Faith Torque'
        self.stop()

class IxaernButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Merciful Cape", style=nextcord.ButtonStyle.blurple)
    async def mcape(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Merciful Cape", ephemeral=True)
        self.drop = 'Merciful Cape'
        self.stop()

    @nextcord.ui.button(label="Altruistic Cape", style=nextcord.ButtonStyle.blurple)
    async def alcape(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Altruistic Cape", ephemeral=True)
        self.drop = 'Altruistic Cape'
        self.stop()

    @nextcord.ui.button(label="Astute Cape", style=nextcord.ButtonStyle.blurple)
    async def alcape(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Astute Cape", ephemeral=True)
        self.drop = 'Astute Cape'
        self.stop()
