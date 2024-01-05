import os, json

from kivy.app import App
from kivy.utils import QueryDict, rgba
from kivy.metrics import dp, sp

from .view import MainWindow
from api import Kraken, OKcoin

class MainApp(App):
    colors = QueryDict()
    colors.bg = rgba("#0A051A")
    colors.primary = rgba("#4F1CE1")
    colors.secondary = [1,1,1, .1]
    colors.success = rgba("#15C097")
    colors.warning = rgba("#F2C94C")
    colors.danger = rgba("#EB5757")
    colors.tertiary = rgba("#19122F")
    colors.tertiary_light = rgba("#464058")
    colors.grey_dark = rgba("#c4c4c4")
    colors.grey_light = rgba("#f5f5f5")
    colors.black = rgba("#a1a1a1")
    colors.white = rgba("#ffffff")

    fonts = QueryDict()
    fonts.size = QueryDict()
    fonts.size.h1 = dp(24)
    fonts.size.h2 = dp(22)
    fonts.size.h3 = dp(18)
    fonts.size.h4 = dp(16)
    fonts.size.h5 = dp(14)
    fonts.size.h6 = dp(12)
    fonts.size.extra = dp(32)

    fonts.heading = 'assets/fonts/Inter/Inter-Bold.otf'
    fonts.subheading = 'assets/fonts/Inter/Inter-Regular.otf'
    fonts.body = 'assets/fonts/Inter/Inter-Light.otf'

    kraken = Kraken()
    okcoin = OKcoin()


    def build(self):
        upath = self.user_data_dir
        save_path = os.path.join(upath, "keys.json")
        if os.path.exists(save_path):
            with open(save_path, "r") as f:
                all_keys = json.load(f)
            
            k = [x for x in all_keys.keys()]

            if 'KRAKEN' in k:
                self.kraken.api_key = all_keys['KRAKEN']['keys']['key']
                self.kraken.api_sec = all_keys['KRAKEN']['keys']['secret']

            if 'OKCOIN' in k:
                self.okcoin.api_key = all_keys['OKCOIN']['keys']['key']
                self.okcoin.api_sec = all_keys['OKCOIN']['keys']['secret']
                self.okcoin.pass_phrase = all_keys['OKCOIN']['keys']['passphrase']

        return MainWindow()
