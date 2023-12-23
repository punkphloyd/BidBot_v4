import nextcord
from nextcord import Interaction


# This python file contains the classes for 2nd level buttons, those outlining the options within each area once an area is selected
# (e.g, Sky is selected --> SkyButtons() contains buttons for Kirin/Byakko/Genbu, etc..)
class SkyButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Kirin", style=nextcord.ButtonStyle.red)
    async def kirin_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Kirin bids", ephemeral=True)
        self.god = 'Kirin'
        self.stop()

    @nextcord.ui.button(label="Genbu", style=nextcord.ButtonStyle.blurple)
    async def genbu_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Genbu bids", ephemeral=True)
        self.god = 'Genbu'
        self.stop()

    @nextcord.ui.button(label="Byakko", style=nextcord.ButtonStyle.blurple)
    async def byakko_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Byakko bids", ephemeral=True)
        self.god = 'Byakko'
        self.stop()

    @nextcord.ui.button(label="Seiryu", style=nextcord.ButtonStyle.blurple)
    async def seiryu_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Seiryu bids", ephemeral=True)
        self.god = 'Seiryu'
        self.stop()

    @nextcord.ui.button(label="Suzaku", style=nextcord.ButtonStyle.blurple)
    async def suzakuu_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Suzaku bids", ephemeral=True)
        self.god = 'Suzaku'
        self.stop()


class SeaButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="A. Virtue", style=nextcord.ButtonStyle.red)
    async def avirtue_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Absolute Virtue", ephemeral=True)
        self.god = 'AV'
        self.stop()

    @nextcord.ui.button(label="Love", style=nextcord.ButtonStyle.red)
    async def love_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Love", ephemeral=True)
        self.god = 'Love'
        self.stop()

    @nextcord.ui.button(label="Justice", style=nextcord.ButtonStyle.blurple)
    async def justice_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Justice", ephemeral=True)
        self.god = 'Justice'
        self.stop()

    @nextcord.ui.button(label="Hope", style=nextcord.ButtonStyle.blurple)
    async def hope_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Hope", ephemeral=True)
        self.god = 'Hope'
        self.stop()

    @nextcord.ui.button(label="Prudence", style=nextcord.ButtonStyle.blurple)
    async def prudence_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Prudence", ephemeral=True)
        self.god = 'Prudence'
        self.stop()

    @nextcord.ui.button(label="Fortitude", style=nextcord.ButtonStyle.grey)
    async def fortitude_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Fortitude", ephemeral=True)
        self.god = 'Fortitude'
        self.stop()

    @nextcord.ui.button(label="Temperance", style=nextcord.ButtonStyle.grey)
    async def temperance_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Temperance", ephemeral=True)
        self.god = 'Temperance'
        self.stop()

    @nextcord.ui.button(label="Faith", style=nextcord.ButtonStyle.grey)
    async def faith_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Faith", ephemeral=True)
        self.god = 'Faith'
        self.stop()

    @nextcord.ui.button(label="Ix'Aern", style=nextcord.ButtonStyle.grey)
    async def ixaern_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ix'Aern", ephemeral=True)
        self.god = 'Ix\'Aern'
        self.stop()


# Dynamis buttons - covers DL, DTav (hydra etc.?), Relic drops
class DynaButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Dynamis Lord", style=nextcord.ButtonStyle.grey)
    async def dlord_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dynamis-Lord", ephemeral=True)
        self.god = 'Dynamis-Lord'
        self.stop()

    @nextcord.ui.button(label="Tavnazia drops", style=nextcord.ButtonStyle.grey)
    async def tav_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dynamis-Tav drops", ephemeral=True)
        self.god = 'Dynamis-Tav'
        self.stop()

    @nextcord.ui.button(label="BLM", style=nextcord.ButtonStyle.grey)
    async def blm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("BLM", ephemeral=True)
        self.god = 'BLM'
        self.stop()

    @nextcord.ui.button(label="BRD", style=nextcord.ButtonStyle.grey)
    async def brd_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("BRD", ephemeral=True)
        self.god = 'BRD'
        self.stop()

    @nextcord.ui.button(label="BST", style=nextcord.ButtonStyle.grey)
    async def bst_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("BST", ephemeral=True)
        self.god = 'BST'
        self.stop()

    @nextcord.ui.button(label="DRG", style=nextcord.ButtonStyle.grey)
    async def drg_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("DRG", ephemeral=True)
        self.god = 'DRG'
        self.stop()

    @nextcord.ui.button(label="DRK", style=nextcord.ButtonStyle.grey)
    async def drk_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("DRK", ephemeral=True)
        self.god = 'DRK'
        self.stop()

    @nextcord.ui.button(label="MNK", style=nextcord.ButtonStyle.grey)
    async def mnk_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("MNK", ephemeral=True)
        self.god = 'MNK'
        self.stop()

    @nextcord.ui.button(label="NIN", style=nextcord.ButtonStyle.grey)
    async def nin_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("NIN", ephemeral=True)
        self.god = 'NIN'
        self.stop()

    @nextcord.ui.button(label="PLD", style=nextcord.ButtonStyle.grey)
    async def pld_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("PLD", ephemeral=True)
        self.god = 'PLD'
        self.stop()

    @nextcord.ui.button(label="RDM", style=nextcord.ButtonStyle.grey)
    async def rdm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("RDM", ephemeral=True)
        self.god = 'RDM'
        self.stop()

    @nextcord.ui.button(label="RNG", style=nextcord.ButtonStyle.grey)
    async def rng_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("RNG", ephemeral=True)
        self.god = 'RNG'
        self.stop()

    @nextcord.ui.button(label="SAM", style=nextcord.ButtonStyle.grey)
    async def sam_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("SAM", ephemeral=True)
        self.god = 'SAM'
        self.stop()

    @nextcord.ui.button(label="SMN", style=nextcord.ButtonStyle.grey)
    async def smn_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("SMN", ephemeral=True)
        self.god = 'SMN'
        self.stop()

    @nextcord.ui.button(label="THF", style=nextcord.ButtonStyle.grey)
    async def thf_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("THF", ephemeral=True)
        self.god = 'THF'
        self.stop()

    @nextcord.ui.button(label="WAR", style=nextcord.ButtonStyle.grey)
    async def war_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("WAR", ephemeral=True)
        self.god = 'WAR'
        self.stop()

    @nextcord.ui.button(label="WHM", style=nextcord.ButtonStyle.grey)
    async def whm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("WHM", ephemeral=True)
        self.god = 'WHM'
        self.stop()


# Limbus buttons - Omega/Ultima
class LimbusButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Omega", style=nextcord.ButtonStyle.grey)
    async def omega_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Omega", ephemeral=True)
        self.god = 'Omega'
        self.stop()

    @nextcord.ui.button(label="Ultima", style=nextcord.ButtonStyle.grey)
    async def ultima_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ultima", ephemeral=True)
        self.god = 'Ultima'
        self.stop()


# HNMs (ground kings + lesser HNMs) - could be expanded?
class HNMSButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Behemoth/KB", style=nextcord.ButtonStyle.grey)
    async def behe_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Behemoth/KB", ephemeral=True)
        self.god = 'Behemoth'
        self.stop()

    @nextcord.ui.button(label="Fafhogg", style=nextcord.ButtonStyle.grey)
    async def fafhogg_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Fafhogg", ephemeral=True)
        self.god = 'Fafhogg'
        self.stop()

    @nextcord.ui.button(label="Turtles", style=nextcord.ButtonStyle.grey)
    async def turtles_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Turtles", ephemeral=True)
        self.god = 'Turtles'
        self.stop()

    @nextcord.ui.button(label="Other HNMS", style=nextcord.ButtonStyle.grey)
    async def others_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Other HNMS", ephemeral=True)
        self.god = 'Other HNMS'
        self.stop()


class HENMButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Ruinous Rocs", style=nextcord.ButtonStyle.grey)
    async def roc_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ruinous Rocs", ephemeral=True)
        self.god = 'Rocs'
        self.stop()

    @nextcord.ui.button(label="Despotic Decapod", style=nextcord.ButtonStyle.grey)
    async def decapod_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Despotic Decapod", ephemeral=True)
        self.god = 'Decapod'
        self.stop()

    @nextcord.ui.button(label="Sacred Scorpions", style=nextcord.ButtonStyle.grey)
    async def scorps_bids(self, button: nextcord.ui.Button, interaction: Interaction):
         await interaction.response.send_message("Sacred Scorpions", ephemeral=True)
         self.god = 'Scorpions'
         self.stop()

    # @nextcord.ui.button(label="Mammet - 9999", style=nextcord.ButtonStyle.grey)
    # async def mammet_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Mammet - 9999", ephemeral=True)
    #      self.god = 'Mammet'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Tonberry Sovereign", style=nextcord.ButtonStyle.grey)
    # async def tonberry_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Tonberry Sovereign", ephemeral=True)
    #      self.god = 'Tonberry'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Ultimega", style=nextcord.ButtonStyle.grey)
    # async def ultimega_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Ultimega", ephemeral=True)
    #      self.god = 'Ultimega'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Io", style=nextcord.ButtonStyle.grey)
    # async def io_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Io", ephemeral=True)
    #      self.god = 'Io'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Primordial Behemoth", style=nextcord.ButtonStyle.grey)
    # async def behemoth_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Primordial Behemoth", ephemeral=True)
    #      self.god = 'Behemoth'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Minogame", style=nextcord.ButtonStyle.grey)
    # async def minogame_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Minogame", ephemeral=True)
    #      self.god = 'Minogame'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Council of Zilart", style=nextcord.ButtonStyle.grey)
    # async def council_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Council", ephemeral=True)
    #      self.god = 'Council'
    #      self.stop()
    #
