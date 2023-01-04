import flet
from flet import Page
from player1dev.client import InMemoryStore, Player1Client

if __name__ == "__main__":

    def main(page: Page):
        app = Player1Client(page, InMemoryStore())
        page.title = "HackedSystem"
        app.appbar.title = flet.Text("HackedSystem")
        page.add(app)
        page.update()
        app.initialize()

    flet.app(target=main, assets_dir="../assets", route_url_strategy="path")
