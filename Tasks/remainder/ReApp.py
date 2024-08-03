from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.app import App

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: [10, 10, 10, 10]
    spacing: 10

    Button:
        text: 'Choose Music File'
        on_release: app.show_filechooser()

    Label:
        id: music_file_label
        text: 'No file selected'

    Button:
        text: 'Play Music'
        on_release: app.play_music()

<FileChooserPopup>:
    size_hint: (0.9, 0.9)
    auto_dismiss: False
    BoxLayout:
        orientation: 'vertical'
        FileChooserIconView:
            id: filechooser
            path: 'D:\\'  # Use double backslashes for Windows paths
        Button:
            text: 'Select'
            on_release: root.select_file()
        Button:
            text: 'Cancel'
            on_release: root.dismiss()
'''

class FileChooserPopup(Popup):
    def __init__(self, **kwargs):
        super(FileChooserPopup, self).__init__(**kwargs)
        self.music_file = None

    def select_file(self):
        chooser = self.ids.filechooser
        selection = chooser.selection
        if selection:
            self.music_file = selection[0]
            self.dismiss()
        else:
            print("No file selected")

class MusicApp(App):
    def build(self):
        return Builder.load_string(KV)

    def show_filechooser(self):
        popup = FileChooserPopup()
        popup.open()

    def play_music(self):
        if hasattr(self, 'music_file') and self.music_file:
            sound = SoundLoader.load(self.music_file)
            if sound:
                sound.play()
            else:
                print("Error loading music file")
        else:
            print("No music file selected")

if __name__ == '__main__':
    MusicApp().run()
