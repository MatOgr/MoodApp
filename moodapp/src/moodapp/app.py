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

        name_label = toga.Label('Your name seems to be ',
                                style=Pack(padding=(0, 5)))
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            '*Your button to picture*',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.load_data()
        print(self.site_data['ingredients'])


def main():
    return MoodApp()
