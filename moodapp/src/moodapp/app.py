"""
Recruitment test application using FB api
"""
import urllib3 as url3
import json
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class MoodApp(toga.App):

    site_data =dict()
    manager = url3.PoolManager()
    url = 'https://moodup.team/test/info.php'

    def load_data(self):
        resp = self.manager.request('GET', self.url)
        buf = resp.data.decode('utf-8')
        self.site_data = json.loads(buf)


    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))

        """
        Top bar section  
            title : RecipeMaster
        """
        top_label = toga.Label('RecipeMaster', style=Pack(
                                    padding=(0, 5),
                                    background_color='Tomato',
                                    color='White')
                               )
        top_bar = toga.Box(style=Pack(
            direction=ROW,
            padding=5,
            background_color='Tomato')
        )
        top_bar.add(top_label)

        button = toga.Button(
            '*Your button to picture*',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(top_bar)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.load_data()
        self.main_window.info_dialog('Result', str(self.site_data))


def main():
    return MoodApp()
