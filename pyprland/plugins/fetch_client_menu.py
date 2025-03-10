" Select a client window and move it to the active workspace"

from .interface import Plugin
from ..adapters.menus import MenuMixin
from ..common import state


class Extension(MenuMixin, Plugin):
    "Shows a menu with shortcuts"

    # Commands

    async def run_fetch_client_menu(self):
        "Select a client window and move it to the active workspace"
        await self.ensure_menu_configured()

        clients = await self.get_clients(workspace_bl=state.active_workspace)

        separator = self.config.get("separator", "|")

        choice = await self.menu.run(
            [f"{i+1} {separator} {c['title']}" for i, c in enumerate(clients)]
        )

        if choice:
            num = int(choice.split(None, 1)[0]) - 1
            addr = clients[num]["address"]
            await self.hyprctl(
                f"movetoworkspace {state.active_workspace},address:{addr}"
            )
