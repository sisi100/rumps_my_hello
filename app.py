from datetime import datetime

import rumps


class HelloApp(rumps.App):
    @rumps.clicked("挨拶")
    def hello(self, _):
        show_text = f"現在時刻は[{datetime.today()}]です"
        rumps.notification(
            "Helloタイトル",
            "Hello world",
            show_text,
            icon="app.png",
        )


if __name__ == "__main__":
    HelloApp("HelloApp", icon="app.png", quit_button="終了").run()
