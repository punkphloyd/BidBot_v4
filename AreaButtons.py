import nextcord
from nextcord import Interaction
from utils import ephemeral


# This python file contains the classes for 2nd level buttons, those outlining the options within each area once an area is selected
# (e.g, Sky is selected --> SkyButtons() contains buttons for Kirin/Byakko/Genbu, etc..)
class SkyButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Kirin", style=nextcord.ButtonStyle.red)
    async def kirin_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Kirin bids", ephemeral=ephemeral)
        self.god = 'Kirin'
        self.stop()

    @nextcord.ui.button(label="Genbu", style=nextcord.ButtonStyle.blurple)
    async def genbu_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Genbu bids", ephemeral=ephemeral)
        self.god = 'Genbu'
        self.stop()

    @nextcord.ui.button(label="Byakko", style=nextcord.ButtonStyle.blurple)
    async def byakko_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Byakko bids", ephemeral=ephemeral)
        self.god = 'Byakko'
        self.stop()

    @nextcord.ui.button(label="Seiryu", style=nextcord.ButtonStyle.blurple)
    async def seiryu_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Seiryu bids", ephemeral=ephemeral)
        self.god = 'Seiryu'
        self.stop()

    @nextcord.ui.button(label="Suzaku", style=nextcord.ButtonStyle.blurple)
    async def suzakuu_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Suzaku bids", ephemeral=ephemeral)
        self.god = 'Suzaku'
        self.stop()


class SeaButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="A. Virtue", style=nextcord.ButtonStyle.red)
    async def avirtue_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Absolute Virtue", ephemeral=ephemeral)
        self.god = 'AV'
        self.stop()

    @nextcord.ui.button(label="Love", style=nextcord.ButtonStyle.red)
    async def love_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Love", ephemeral=ephemeral)
        self.god = 'Love'
        self.stop()

    @nextcord.ui.button(label="Justice", style=nextcord.ButtonStyle.blurple)
    async def justice_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Justice", ephemeral=ephemeral)
        self.god = 'Justice'
        self.stop()

    @nextcord.ui.button(label="Hope", style=nextcord.ButtonStyle.blurple)
    async def hope_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Hope", ephemeral=ephemeral)
        self.god = 'Hope'
        self.stop()

    @nextcord.ui.button(label="Prudence", style=nextcord.ButtonStyle.blurple)
    async def prudence_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Prudence", ephemeral=ephemeral)
        self.god = 'Prudence'
        self.stop()

    @nextcord.ui.button(label="Fortitude", style=nextcord.ButtonStyle.grey)
    async def fortitude_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Fortitude", ephemeral=ephemeral)
        self.god = 'Fortitude'
        self.stop()

    @nextcord.ui.button(label="Temperance", style=nextcord.ButtonStyle.grey)
    async def temperance_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Temperance", ephemeral=ephemeral)
        self.god = 'Temperance'
        self.stop()

    @nextcord.ui.button(label="Faith", style=nextcord.ButtonStyle.grey)
    async def faith_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Jailer of Faith", ephemeral=ephemeral)
        self.god = 'Faith'
        self.stop()

    @nextcord.ui.button(label="Ix'Aern", style=nextcord.ButtonStyle.grey)
    async def ixaern_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ix'Aern", ephemeral=ephemeral)
        self.god = 'Ix\'Aern'
        self.stop()


# Dynamis buttons - covers DL, DTav (hydra etc.?), Relic drops
class DynaButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Dynamis Lord", style=nextcord.ButtonStyle.grey)
    async def dlord_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dynamis-Lord", ephemeral=ephemeral)
        self.god = 'Dynamis-Lord'
        self.stop()

    @nextcord.ui.button(label="Tavnazia drops", style=nextcord.ButtonStyle.grey)
    async def tav_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Dynamis-Tav drops", ephemeral=ephemeral)
        self.god = 'Dynamis-Tav'
        self.stop()

    @nextcord.ui.button(label="BLM", style=nextcord.ButtonStyle.grey)
    async def blm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("BLM", ephemeral=ephemeral)
        self.god = 'BLM'
        self.stop()

    @nextcord.ui.button(label="BRD", style=nextcord.ButtonStyle.grey)
    async def brd_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("BRD", ephemeral=ephemeral)
        self.god = 'BRD'
        self.stop()

    @nextcord.ui.button(label="BST", style=nextcord.ButtonStyle.grey)
    async def bst_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("BST", ephemeral=ephemeral)
        self.god = 'BST'
        self.stop()

    @nextcord.ui.button(label="DRG", style=nextcord.ButtonStyle.grey)
    async def drg_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("DRG", ephemeral=ephemeral)
        self.god = 'DRG'
        self.stop()

    @nextcord.ui.button(label="DRK", style=nextcord.ButtonStyle.grey)
    async def drk_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("DRK", ephemeral=ephemeral)
        self.god = 'DRK'
        self.stop()

    @nextcord.ui.button(label="MNK", style=nextcord.ButtonStyle.grey)
    async def mnk_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("MNK", ephemeral=ephemeral)
        self.god = 'MNK'
        self.stop()

    @nextcord.ui.button(label="NIN", style=nextcord.ButtonStyle.grey)
    async def nin_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("NIN", ephemeral=ephemeral)
        self.god = 'NIN'
        self.stop()

    @nextcord.ui.button(label="PLD", style=nextcord.ButtonStyle.grey)
    async def pld_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("PLD", ephemeral=ephemeral)
        self.god = 'PLD'
        self.stop()

    @nextcord.ui.button(label="RDM", style=nextcord.ButtonStyle.grey)
    async def rdm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("RDM", ephemeral=ephemeral)
        self.god = 'RDM'
        self.stop()

    @nextcord.ui.button(label="RNG", style=nextcord.ButtonStyle.grey)
    async def rng_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("RNG", ephemeral=ephemeral)
        self.god = 'RNG'
        self.stop()

    @nextcord.ui.button(label="SAM", style=nextcord.ButtonStyle.grey)
    async def sam_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("SAM", ephemeral=ephemeral)
        self.god = 'SAM'
        self.stop()

    @nextcord.ui.button(label="SMN", style=nextcord.ButtonStyle.grey)
    async def smn_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("SMN", ephemeral=ephemeral)
        self.god = 'SMN'
        self.stop()

    @nextcord.ui.button(label="THF", style=nextcord.ButtonStyle.grey)
    async def thf_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("THF", ephemeral=ephemeral)
        self.god = 'THF'
        self.stop()

    @nextcord.ui.button(label="WAR", style=nextcord.ButtonStyle.grey)
    async def war_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("WAR", ephemeral=ephemeral)
        self.god = 'WAR'
        self.stop()

    @nextcord.ui.button(label="WHM", style=nextcord.ButtonStyle.grey)
    async def whm_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("WHM", ephemeral=ephemeral)
        self.god = 'WHM'
        self.stop()


# Limbus buttons - Omega/Ultima
class LimbusButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Omega", style=nextcord.ButtonStyle.grey)
    async def omega_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Omega", ephemeral=ephemeral)
        self.god = 'Omega'
        self.stop()

    @nextcord.ui.button(label="Ultima", style=nextcord.ButtonStyle.grey)
    async def ultima_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ultima", ephemeral=ephemeral)
        self.god = 'Ultima'
        self.stop()


# HNMs (ground kings + lesser HNMs) - could be expanded?
class HNMSButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Behemoth/KB", style=nextcord.ButtonStyle.grey)
    async def behe_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Behemoth/KB", ephemeral=ephemeral)
        self.god = 'Behemoth'
        self.stop()

    @nextcord.ui.button(label="Fafhogg", style=nextcord.ButtonStyle.grey)
    async def fafhogg_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Fafhogg", ephemeral=ephemeral)
        self.god = 'Fafhogg'
        self.stop()

    @nextcord.ui.button(label="Turtles", style=nextcord.ButtonStyle.grey)
    async def turtles_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Turtles", ephemeral=ephemeral)
        self.god = 'Turtles'
        self.stop()

    @nextcord.ui.button(label="Other HNMS", style=nextcord.ButtonStyle.grey)
    async def others_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Other HNMS", ephemeral=ephemeral)
        self.god = 'Other HNMS'
        self.stop()


class BattlefieldButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Waking the Beast", style=nextcord.ButtonStyle.grey)
    async def wtb_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Waking the Beast", ephemeral=ephemeral)
        self.god = 'Waking'
        self.stop()

    @nextcord.ui.button(label="Bahamut v2", style=nextcord.ButtonStyle.grey)
    async def bahv2_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Bahamut v2", ephemeral=ephemeral)
        self.god = 'Bahamut v2'
        self.stop()

    @nextcord.ui.button(label="KS99", style=nextcord.ButtonStyle.grey)
    async def bahv2_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("KS99", ephemeral=ephemeral)
        self.god = 'KS99'
        self.stop()


class HENMButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.god = None

    @nextcord.ui.button(label="Ruinous Rocs", style=nextcord.ButtonStyle.grey)
    async def roc_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Ruinous Rocs", ephemeral=ephemeral)
        self.god = 'Rocs'
        self.stop()

    @nextcord.ui.button(label="Despotic Decapod", style=nextcord.ButtonStyle.grey)
    async def decapod_bids(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Despotic Decapod", ephemeral=ephemeral)
        self.god = 'Decapod'
        self.stop()

    @nextcord.ui.button(label="Sacred Scorpions", style=nextcord.ButtonStyle.grey)
    async def scorps_bids(self, button: nextcord.ui.Button, interaction: Interaction):
         await interaction.response.send_message("Sacred Scorpions", ephemeral=ephemeral)
         self.god = 'Scorpions'
         self.stop()

    # @nextcord.ui.button(label="Mammet - 9999", style=nextcord.ButtonStyle.grey)
    # async def mammet_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Mammet - 9999", ephemeral=ephemeral)
    #      self.god = 'Mammet'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Tonberry Sovereign", style=nextcord.ButtonStyle.grey)
    # async def tonberry_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Tonberry Sovereign", ephemeral=ephemeral)
    #      self.god = 'Tonberry'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Ultimega", style=nextcord.ButtonStyle.grey)
    # async def ultimega_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Ultimega", ephemeral=ephemeral)
    #      self.god = 'Ultimega'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Io", style=nextcord.ButtonStyle.grey)
    # async def io_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Io", ephemeral=ephemeral)
    #      self.god = 'Io'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Primordial Behemoth", style=nextcord.ButtonStyle.grey)
    # async def behemoth_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Primordial Behemoth", ephemeral=ephemeral)
    #      self.god = 'Behemoth'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Minogame", style=nextcord.ButtonStyle.grey)
    # async def minogame_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Minogame", ephemeral=ephemeral)
    #      self.god = 'Minogame'
    #      self.stop()
    #
    # @nextcord.ui.button(label="Council of Zilart", style=nextcord.ButtonStyle.grey)
    # async def council_bids(self, button: nextcord.ui.Button, interaction: Interaction):
    #      await interaction.response.send_message("Council", ephemeral=ephemeral)
    #      self.god = 'Council'
    #      self.stop()
    #
