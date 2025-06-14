
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.65, 0.78, 0.91, 1)  # Açık mavi arka plan

class GirisEkrani(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=15, spacing=12)

        self.label = Label(
            text='Şifreni Gir:', font_size='24sp', color=(1, 1, 1, 1), size_hint=(1, 0.15)
        )  # Beyaz

        self.text_input = TextInput(
            password=True, hint_text="Şifre", multiline=False, size_hint=(1, 0.15),
            font_size='20sp',
            foreground_color=(1, 1, 1, 1), background_color=(0.29, 0.56, 0.89, 1),
            hint_text_color=(0.9, 0.9, 0.9, 1)
        )

        button = Button(
            text="Giriş Yap", size_hint=(1, 0.22),
            font_size='20sp',
            background_color=(0.29, 0.56, 0.89, 1), color=(1, 1, 1, 1)
        )
        button.bind(on_press=self.sifre_kontrol)

        self.sonuc = Label(
            text="", font_size='18sp', color=(1, 1, 1, 1), size_hint=(1, 0.12)
        )  # Beyaz

        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(button)
        layout.add_widget(self.sonuc)

        self.add_widget(layout)

    def sifre_kontrol(self, instance):
        sayilar = [47596758, 10142973, 65762194, 51228310, 51220161, 18015461, 27723939,
                   22577668, 39746272, 44834006, 83366898]
        girilen_sifre = self.text_input.text.strip()

        try:
            girilen_sifre_int = int(girilen_sifre)
        except ValueError:
            self.sonuc.text = "Şifre sadece rakamlardan oluşmalı!"
            self.sonuc.color = (1, 0, 0, 1)
            return

        if girilen_sifre_int in sayilar:
            self.sonuc.text = "Giriş Başarılı"
            self.sonuc.color = (0, 1, 0, 1)
            self.manager.current = 'welcome'  # Ana ekrana geçiş welcome ekranı
            with open('durum.txt', 'w', encoding='utf-8') as dosya:
                dosya.write("doğrulandı")
        else:
            self.sonuc.text = "Hatalı Şifre"
            self.sonuc.color = (1, 0, 0, 1)


class CryptoApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=15, spacing=12)

        self.label = Label(
            text="Lütfen Aşağıda İstenilen Bilgileri Giriniz",
            color=(1, 1, 1, 1), font_size='20sp', size_hint=(1, 0.15)
        )
        layout.add_widget(self.label)

        self.api_key_input = TextInput(
            password=False, hint_text="API Key", multiline=False, size_hint=(1, 0.15),
            font_size='18sp',
            foreground_color=(1, 1, 1, 1), background_color=(0.29, 0.56, 0.89, 1),
            hint_text_color=(0.9, 0.9, 0.9, 1)
        )
        layout.add_widget(self.api_key_input)

        self.api_secret_input = TextInput(
            password=True, hint_text="API Secret", multiline=False, size_hint=(1, 0.15),
            font_size='18sp',
            foreground_color=(1, 1, 1, 1), background_color=(0.29, 0.56, 0.89, 1),
            hint_text_color=(0.9, 0.9, 0.9, 1)
        )
        layout.add_widget(self.api_secret_input)

        button = Button(
            text="Devam Et", size_hint=(1, 0.22),
            font_size='20sp',
            background_color=(0.29, 0.56, 0.89, 1), color=(1, 1, 1, 1)
        )
        button.bind(on_press=self.devam_et)
        layout.add_widget(button)

        self.add_widget(layout)

    def devam_et(self, instance):
        api_key = self.api_key_input.text.strip()
        api_secret = self.api_secret_input.text.strip()

        if not api_key or not api_secret:
            self.label.text = "API Key ve Secret boş bırakılamaz!"
            self.label.color = (1, 0, 0, 1)
        else:
            self.label.text = "API bilgileri alındı."
            self.label.color = (1, 1, 1, 1)
            self.manager.current = 'cointype'


class CoinType(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=15, spacing=12)

        self.label = Label(
            text="Lütfen Aralarında İşlem Yapmak İstediğiniz 3 coini giriniz",
            color=(1, 1, 1, 1), font_size='20sp', size_hint=(1, 0.15)
        )
        layout.add_widget(self.label)

        self.coin1_input = TextInput(
            hint_text="Coin 1", multiline=False, size_hint=(1, 0.15),
            font_size='18sp',
            foreground_color=(1, 1, 1, 1), background_color=(0.29, 0.56, 0.89, 1),
            hint_text_color=(0.9, 0.9, 0.9, 1)
        )
        self.coin2_input = TextInput(
            hint_text="Coin 2", multiline=False, size_hint=(1, 0.15),
            font_size='18sp',
            foreground_color=(1, 1, 1, 1), background_color=(0.29, 0.56, 0.89, 1),
            hint_text_color=(0.9, 0.9, 0.9, 1)
        )
        self.coin3_input = TextInput(
            hint_text="Coin 3", multiline=False, size_hint=(1, 0.15),
            font_size='18sp',
            foreground_color=(1, 1, 1, 1), background_color=(0.29, 0.56, 0.89, 1),
            hint_text_color=(0.9, 0.9, 0.9, 1)
        )

        layout.add_widget(self.coin1_input)
        layout.add_widget(self.coin2_input)
        layout.add_widget(self.coin3_input)

        button = Button(
            text="Onayla", size_hint=(1, 0.22),
            font_size='20sp',
            background_color=(0.29, 0.56, 0.89, 1), color=(1, 1, 1, 1)
        )
        button.bind(on_press=self.gonder_coins)

        layout.add_widget(button)
        self.add_widget(layout)

    def gonder_coins(self, instance):
        if (not self.coin1_input.text.strip() or
            not self.coin2_input.text.strip() or
            not self.coin3_input.text.strip()):
            self.label.text = "Lütfen 3 coin bilgisini eksiksiz giriniz!"
            self.label.color = (1, 0, 0, 1)
        else:
            self.label.text = "Teşekkürler, coinler alındı."
            self.label.color = (1, 1, 1, 1)


class Welcome(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=15, spacing=12)

        self.label = Label(
            text="🚀 Welcome to Arbix! Üçgen arbitraj fırsatlarını anında yakala, kazanç senin kontrol senin. "
                 "Piyasayı sen yönet! -Bu Bir BotStore Ürünüdür-",
            color=(1, 1, 1, 1), font_size='18sp', size_hint=(1, 0.3)
        )
        layout.add_widget(self.label)

        button = Button(
            text="Devam Et", size_hint=(1, 0.22),
            font_size='20sp',
            background_color=(0.29, 0.56, 0.89, 1), color=(1, 1, 1, 1)
        )
        button.bind(on_press=self.devam_et)
        layout.add_widget(button)

        self.add_widget(layout)

    def devam_et(self, instance):
        self.manager.current = 'cryptoapp'


