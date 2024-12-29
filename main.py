import hashlib
import random
import re
import math
import time
import uuid

from fastapi import FastAPI, UploadFile, HTTPException
from lupa import LuaRuntime
from typing import Dict, Optional, Set, List, Callable

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
lupa_logger = logging.getLogger("lupa")
lupa_logger.setLevel(logging.DEBUG)

app = FastAPI()
lua = LuaRuntime(unpack_returned_tuples=True)

BLACKLIST = BLACKLIST = [
    "os.execute",
    "io.open",
    "os.remove",
    "os.rename",
    "load",
    "loadstring",
    "dofile",
    "socket",
    "http",
    "ffi",
    "require",
    "debug",
    "package",
    "os.exit",
    "os.getenv",
]


def world_to_screen(pos: "FatalityAPI.Vector3") -> "FatalityAPI.Draw.Vector2":
    return FatalityAPI.Draw.Vector2(960, 540)


math.world_to_screen = world_to_screen


class FatalityAPI:
    class Draw:
        def __init__(self):
            self.surface = self.Surface()
            self.vec2 = self.Vector2
            self.color = self.Color

        class Color:
            r: int
            g: int
            b: int
            a: int

            def __init__(self, r: int, g: int, b: int, a: Optional[int] = 255) -> None:
                self.r = r
                self.g = g
                self.b = b
                self.a = a

            @classmethod
            def white(cls):
                return cls(255, 255, 255, 255)

        class Vector2:
            x: float
            y: float

            def __init__(self, x: float, y: float) -> None:
                self.x = x
                self.y = y

            def is_valid(self) -> bool:
                """Returns true if all values in this vector are finite."""
                return all(map(lambda v: math.isfinite(v), [self.x, self.y]))

        class Surface:
            def add_line(
                self,
                start: "FatalityAPI.Draw.Vector2",
                end: "FatalityAPI.Draw.Vector2",
                color: "FatalityAPI.Draw.Color",
            ) -> None:
                pass

    class Vector3:
        x: float
        y: float
        z: float

        def __init__(self, x: float, y: float, z: float) -> None:
            self.x = x
            self.y = y
            self.z = z

        def is_valid(self) -> bool:
            """Returns true if all values in this vector are finite."""
            return all(map(lambda v: math.isfinite(v), [self.x, self.y, self.z]))

    class GUI:
        ids: Set[int]
        controls: Dict[int, "Control"]

        def __init__(self):
            self.ctx = self.Context(self)
            self.ids = set()
            self.controls = {}

        class Control:
            id: int
            id_string: str
            is_visible: bool
            tooltip: Optional[str]

            def __init__(self, gui: "FatalityAPI.GUI", id: int) -> None:
                self.id = id
                self.id_string = str(id)
                self.is_visible = True
                self.gui = gui
                gui.controls[id] = self

            def tooltip(self, tooltip: str) -> None:
                self.tooltip = tooltip

            def add(self, control: "Control") -> None:
                self.gui.controls[control.id] = control

        class Context:
            def __init__(self, gui: "FatalityAPI.GUI") -> None:
                self.gui = gui

            def find(self, context_str: str) -> "FatalityAPI.GUI.Control":
                id = self.gui.control_id(context_str)
                if id not in self.gui.controls:
                    # Create a new Group with the given id
                    return self.gui.group(id)
                    # raise ValueError(f"Control with id {id} not found")
                return self.gui.controls[id]

        class Checkbox(Control):
            def __init__(self, gui: "FatalityAPI.GUI", control_id: int) -> None:
                super().__init__(gui, control_id)

            def get_value(self) -> "ValueParam":
                return self.gui.ValueParam(self)

        class ControlContainer(Control):
            def __init__(self, gui: "FatalityAPI.GUI", control_id: int) -> None:
                super().__init__(gui, control_id)

        class Layout(ControlContainer):
            label: str

            def __init__(
                self, gui: "FatalityAPI.GUI", label: str, control: "Control"
            ) -> None:
                self.label = label
                super().__init__(gui, control.id)

        class ValueParam:
            def __init__(self, control: "Control") -> None:
                self.control = control

            def get(self) -> bool:
                return True

        class Group(ControlContainer):
            def __init__(self, gui: "FatalityAPI.GUI", control_id: int) -> None:
                super().__init__(gui, control_id)

            def get_value(self) -> "ValueParam":
                return self.gui.ValueParam(self)

        def control_id(self, control_id_str: str) -> int:
            hash_object = hashlib.sha256(control_id_str.encode("utf-8"))
            id = int(hash_object.hexdigest(), 16) % 10**8
            self.ids.add(id)
            return id

        def group(self, control_id: int) -> "Group":
            return self.Group(self, control_id)

        def checkbox(self, control_id: int) -> Checkbox:
            return self.Checkbox(self, control_id)

        def make_control(self, label: str, control: Control) -> Layout:
            return self.Layout(self, label, control)

    class Game:
        def __init__(self):
            self.engine = self.Engine()
            self.global_vars = self.GlobalVars()

        class Engine:
            def get_screen_size(self) -> (int, int):
                return 1920, 1080

        class GlobalVars:
            real_time: float

            def __init__(self):
                self.real_time = time.time()

    class Events:
        def __init__(self):
            self.present_queue = self.PresentQueue()

        class PresentQueue:
            callbacks: List[Callable]

            def __init__(self):
                self.callbacks: List[Callable] = []

            def add(self, func: Callable) -> None:
                self.callbacks.append(func)
                for _ in range(10):
                    func()
                    time.sleep(0.016)

    class Entities:
        def __init__(self):
            self.players = self.Players()
            self.players.add(self.Pawn("LocalPlayer", self.players))

            for _ in range(10):
                self.players.add(self.Pawn(uuid.uuid4().hex, self.players))

        class Players:
            players: set["Pawn"]

            def __init__(self):
                self.players = set()

            def add(self, player: "Pawn") -> None:
                self.players.add(player)

            def for_each(self, func: Callable[["Pawn"], None]) -> None:
                for player in self.players:
                    func(player)

        class Pawn:
            name: str
            team: int
            entity: "FatalityAPI.Entities.Pawn"
            players: "FatalityAPI.Entities.Players"

            def __init__(
                self, name: str, players: "FatalityAPI.Entities.Players"
            ) -> None:
                self.name = name
                self.team = random.randint(0, 1)
                self.entity = self
                self.players = players

            def is_alive(self) -> bool:
                return True

            def is_enemy(self) -> bool:
                for player in self.players.players:
                    if player.name == "LocalPlayer":
                        return player.team != self.team

            def get_eye_pos(self) -> "Vector3":
                return FatalityAPI.Vector3(
                    random.randint(-500, 500),
                    random.randint(-500, 500),
                    random.randint(-500, 500),
                )

            def get_name(self) -> str:
                return self.name

            def should_draw(self) -> bool:
                return True

            def __hash__(self):
                return hash((self.name, self.team))

            def __eq__(self, other):
                if not isinstance(other, self.__class__):
                    return False
                return self.name == other.name and self.team == other.team

        def get_local_pawn(self) -> "Pawn":
            for player in self.players.players:
                if player.name == "LocalPlayer":
                    return player


def calculate_entropy(data: str) -> float:
    if not data:
        return 0.0
    probabilities = [data.count(c) / len(data) for c in set(data)]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy


def check_obfuscation(script_content: str) -> bool:
    high_entropy_threshold = 4.0

    for match in re.findall(r'["\']([^"\']+)["\']', script_content):
        if calculate_entropy(match) > high_entropy_threshold:
            return True

    if max(len(line) for line in script_content.splitlines()) > 1000:
        return True

    if re.search(r"\([\"\'].*?\\\d{2,3}(\\\d{2,3})+[\"\']\)", script_content):
        return True

    return False


def analyze_lua_script(script_content: str) -> Dict:
    for dangerous_func in BLACKLIST:
        if re.search(rf"\b{re.escape(dangerous_func)}\b", script_content):
            return {"status": "flagged", "reason": f"Contains {dangerous_func}"}

    if re.search(
        r"while\s+true|repeat.*until\s+false", script_content, re.DOTALL
    ):  # fix black
        return {"status": "flagged", "reason": "Possible infinite loop"}

    if check_obfuscation(script_content):
        return {"status": "flagged", "reason": "Possible obfuscation detected"}
    try:
        if "FatalityAPI" == "FatalityAPI":
            gui = FatalityAPI.GUI()
            game = FatalityAPI.Game()
            events = FatalityAPI.Events()
            entities = FatalityAPI.Entities()
            draw = FatalityAPI.Draw()
            lua.globals().gui = gui
            lua.globals().game = game
            lua.globals().events = events
            lua.globals().entities = entities
            lua.globals().math = math
            lua.globals().draw = draw

        sandbox_env = lua.eval(
            """
            function()
                local sandbox = {}
                setmetatable(sandbox, {__index = _G})
                return sandbox
            end
        """
        )()

        lua.execute(script_content, sandbox_env)
    except Exception as e:
        return {"status": "flagged", "reason": f"Error during execution: {e}"}

    return {"status": "approved"}


@app.post("/analyze-script")
async def analyze_script(file: UploadFile):
    if not file.filename.endswith(".lua"):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only .lua files are allowed."
        )

    script_content = await file.read()
    script_content = script_content.decode("utf-8")

    result = analyze_lua_script(script_content)
    return result
