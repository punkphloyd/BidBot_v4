import nextcord
from nextcord import Interaction
# Buttons for sky gods


class KirinButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Kirin\'s Osode", style=nextcord.ButtonStyle.red)
    async def osode(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Kirin's Osode", ephemeral=True)
        self.drop = 'Kirin\'s Osode'
        self.stop()

    @nextcord.ui.button(label="Kirin\'s Pole", style=nextcord.ButtonStyle.red)
    async def pole(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Kirin's Pole", ephemeral=True)
        self.drop = 'Kirin\'s Pole'
        self.stop()

    @nextcord.ui.button(label="D Body", style=nextcord.ButtonStyle.red)
    async def dbody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("D Body", ephemeral=True)
        self.drop = 'D Body'
        self.stop()

    @nextcord.ui.button(label="N Body", style=nextcord.ButtonStyle.red)
    async def nbody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("N Body", ephemeral=True)
        self.drop = 'N Body'
        self.stop()

    @nextcord.ui.button(label="W Legs", style=nextcord.ButtonStyle.red)
    async def wlegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("W Legs", ephemeral=True)
        self.drop = 'W Legs'
        self.stop()


class GenbuButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Genbu's Kabuto", style=nextcord.ButtonStyle.red)
    async def kabuto(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Genbu's Kabuto", ephemeral=True)
        self.drop = 'Genbu\'s Kabuto'
        self.stop()

    @nextcord.ui.button(label="Genbu\'s Shield", style=nextcord.ButtonStyle.red)
    async def shield(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Genbu's Shield", ephemeral=True)
        self.drop = 'Genbu\'s Shield'
        self.stop()

    @nextcord.ui.button(label="A Head", style=nextcord.ButtonStyle.red)
    async def ahead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Head", ephemeral=True)
        self.drop = 'A Head'
        self.stop()

    @nextcord.ui.button(label="A Hands", style=nextcord.ButtonStyle.red)
    async def ahands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Hands", ephemeral=True)
        self.drop = 'A Hands'
        self.stop()

    @nextcord.ui.button(label="M Hands", style=nextcord.ButtonStyle.red)
    async def mhands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("M Hands", ephemeral=True)
        self.drop = 'M Hands'
        self.stop()

    @nextcord.ui.button(label="W Feet", style=nextcord.ButtonStyle.red)
    async def wfeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("W Feet", ephemeral=True)
        self.drop = 'W Feet'
        self.stop()


class SeiryuButtons(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Seiryu's Kote", style=nextcord.ButtonStyle.red)
    async def kote(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Seiryu's Kote", ephemeral=True)
        self.drop = 'Seiryu\'s Kote'
        self.stop()


    @nextcord.ui.button(label="Seiryu's Sword", style=nextcord.ButtonStyle.red)
    async def sword(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Seiryu's Sword", ephemeral=True)
        self.drop = 'Seiryu\'s Sword'
        self.stop()

    @nextcord.ui.button(label="A Legs", style=nextcord.ButtonStyle.red)
    async def alegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Legs", ephemeral=True)
        self.drop = 'A Legs'
        self.stop()

    @nextcord.ui.button(label="W Hands", style=nextcord.ButtonStyle.red)
    async def whands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("W Hands", ephemeral=True)
        self.drop = 'W Hands'
        self.stop()

    @nextcord.ui.button(label="D Head", style=nextcord.ButtonStyle.red)
    async def dhead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("D Head", ephemeral=True)
        self.drop = 'D Head'
        self.stop()

    @nextcord.ui.button(label="M Head", style=nextcord.ButtonStyle.red)
    async def mhead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("M Head", ephemeral=True)
        self.drop = 'M Head'
        self.stop()


class SuzakuButtons(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Suzaku's Sune-ate", style=nextcord.ButtonStyle.red)
    async def suneate(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Suzaku's Sune-ate", ephemeral=True)
        self.drop = 'Suzaku\'s Sune-ate'
        self.stop()

    @nextcord.ui.button(label="Suzaku's Scythe", style=nextcord.ButtonStyle.red)
    async def scythe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Suzaku's Scythe", ephemeral=True)
        self.drop = 'Suzaku\'s Scythe'
        self.stop()

    @nextcord.ui.button(label="A Legs", style=nextcord.ButtonStyle.red)
    async def alegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Legs", ephemeral=True)
        self.drop = 'A Legs'
        self.stop()

    @nextcord.ui.button(label="D Hands", style=nextcord.ButtonStyle.red)
    async def dhands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("D Hands", ephemeral=True)
        self.drop = 'D Hands'
        self.stop()

    @nextcord.ui.button(label="E Head", style=nextcord.ButtonStyle.red)
    async def ehead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("E Head", ephemeral=True)
        self.drop = 'E Head'
        self.stop()

    @nextcord.ui.button(label="N Feet", style=nextcord.ButtonStyle.red)
    async def nfeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("N Feet", ephemeral=True)
        self.drop = 'N Feet'
        self.stop()



class ByakkoButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Byakko's Haidate", style=nextcord.ButtonStyle.red)
    async def haidate(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Byakko's Haidate", ephemeral=True)
        self.drop = 'Byakko\'s Haidate'
        self.stop()

    @nextcord.ui.button(label="Byakko's Axe", style=nextcord.ButtonStyle.red)
    async def axe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Byakko's Axe", ephemeral=True)
        self.drop = 'Byakko\'s Axe'
        self.stop()

    @nextcord.ui.button(label="A Head", style=nextcord.ButtonStyle.red)
    async def ahead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Head", ephemeral=True)
        self.drop = 'A Head'
        self.stop()

    @nextcord.ui.button(label="N Hands", style=nextcord.ButtonStyle.red)
    async def nhands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("N Hands", ephemeral=True)
        self.drop = 'N Hands'
        self.stop()

    @nextcord.ui.button(label="D Legs", style=nextcord.ButtonStyle.red)
    async def dlegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("D Legs", ephemeral=True)
        self.drop = 'D Legs'
        self.stop()

    @nextcord.ui.button(label="E Feet", style=nextcord.ButtonStyle.red)
    async def efeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("E Feet", ephemeral=True)
        self.drop = 'E Feet'
        self.stop()


