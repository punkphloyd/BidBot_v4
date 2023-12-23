import nextcord
from nextcord import Interaction
# Buttons for the numerous HNMs available in the bidding system (ground kings, etc.)


class BeheButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Defending Ring", style=nextcord.ButtonStyle.red)
    async def dring(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Defending Ring", ephemeral=True)
        self.drop = 'Defending Ring'
        self.stop()

    @nextcord.ui.button(label="Pixie Ring", style=nextcord.ButtonStyle.red)
    async def pring(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Pixie Ring", ephemeral=True)
        self.drop = 'Pixie Ring'
        self.stop()

    @nextcord.ui.button(label="E Legs", style=nextcord.ButtonStyle.red)
    async def elegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("E Legs", ephemeral=True)
        self.drop = 'E Legs'
        self.stop()

    @nextcord.ui.button(label="M Legs", style=nextcord.ButtonStyle.red)
    async def mlegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("M Legs", ephemeral=True)
        self.drop = 'M Legs'
        self.stop()

    @nextcord.ui.button(label="W Head", style=nextcord.ButtonStyle.red)
    async def whead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("W Head", ephemeral=True)
        self.drop = 'W Head'
        self.stop()

    @nextcord.ui.button(label="A Feet", style=nextcord.ButtonStyle.red)
    async def afeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Feet", ephemeral=True)
        self.drop = 'A Feet'
        self.stop()


class FafhoggButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Ridill", style=nextcord.ButtonStyle.red)
    async def ridill(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ridill", ephemeral=True)
        self.drop = 'Ridill'
        self.stop()

    @nextcord.ui.button(label="Hrotti", style=nextcord.ButtonStyle.red)
    async def hrotti(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Hrotti", ephemeral=True)
        self.drop = 'Hrotti'
        self.stop()

    @nextcord.ui.button(label="Aegishjalmr", style=nextcord.ButtonStyle.red)
    async def aegish(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Aegishjalmr", ephemeral=True)
        self.drop = 'Aegishjalmr'
        self.stop()

    @nextcord.ui.button(label="Andvarnauts", style=nextcord.ButtonStyle.red)
    async def andvar(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Aegishjalmr", ephemeral=True)
        self.drop = 'Aegishjalmr'
        self.stop()

    @nextcord.ui.button(label="A Feet", style=nextcord.ButtonStyle.red)
    async def afeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Feet", ephemeral=True)
        self.drop = 'A Feet'
        self.stop()

    @nextcord.ui.button(label="N Head", style=nextcord.ButtonStyle.red)
    async def nhead(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("N Head", ephemeral=True)
        self.drop = 'N Head'
        self.stop()

    @nextcord.ui.button(label="E Hands", style=nextcord.ButtonStyle.red)
    async def ehands(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("E Hands", ephemeral=True)
        self.drop = 'E Hands'
        self.stop()

    @nextcord.ui.button(label="E Body", style=nextcord.ButtonStyle.red)
    async def ebody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("E Body", ephemeral=True)
        self.drop = 'E Body'
        self.stop()

    @nextcord.ui.button(label="A Body", style=nextcord.ButtonStyle.red)
    async def abody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Body", ephemeral=True)
        self.drop = 'A Body'
        self.stop()

    @nextcord.ui.button(label="M Body", style=nextcord.ButtonStyle.red)
    async def mbody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("M Body", ephemeral=True)
        self.drop = 'M Body'
        self.stop()

    @nextcord.ui.button(label="N Legs", style=nextcord.ButtonStyle.red)
    async def nlegs(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("N Legs", ephemeral=True)
        self.drop = 'N Legs'
        self.stop()


class AspidButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="A Body", style=nextcord.ButtonStyle.red)
    async def abody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("A Body", ephemeral=True)
        self.drop = 'A Body'
        self.stop()

    @nextcord.ui.button(label="M Feet", style=nextcord.ButtonStyle.red)
    async def mfeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("M Feet", ephemeral=True)
        self.drop = 'M Feet'
        self.stop()

    @nextcord.ui.button(label="D Feet", style=nextcord.ButtonStyle.red)
    async def dfeet(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("D Feet", ephemeral=True)
        self.drop = 'D Feet'
        self.stop()

    @nextcord.ui.button(label="W Body", style=nextcord.ButtonStyle.red)
    async def wbody(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("W Body", ephemeral=True)
        self.drop = 'W Body'
        self.stop()


class OtherHNMButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.drop = None

    @nextcord.ui.button(label="Strider Boots", style=nextcord.ButtonStyle.red)
    async def sboots(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Strider Boots", ephemeral=True)
        self.drop = 'Strider Boots'
        self.stop()

    @nextcord.ui.button(label="Ace's Helm", style=nextcord.ButtonStyle.red)
    async def ahelm(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ace's Helm", ephemeral=True)
        self.drop = 'Ace\'s Helm'
        self.stop()

    @nextcord.ui.button(label="Heavy Shell", style=nextcord.ButtonStyle.red)
    async def hshell(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Heavy Shell", ephemeral=True)
        self.drop = 'Heavy Shell'
        self.stop()

    @nextcord.ui.button(label="Herald Gaiters", style=nextcord.ButtonStyle.red)
    async def hgaiters(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Herald Gaiters", ephemeral=True)
        self.drop = 'Herald Gaiters'
        self.stop()
