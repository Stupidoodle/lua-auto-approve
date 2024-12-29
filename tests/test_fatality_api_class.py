from unittest.mock import MagicMock

from main import FatalityAPI


def test_draw_color_initialization():
    color = FatalityAPI.Draw.Color(255, 100, 50)
    assert color.r == 255
    assert color.g == 100
    assert color.b == 50
    assert color.a == 255


def test_draw_color_white():
    white = FatalityAPI.Draw.Color.white()
    assert white.r == 255
    assert white.g == 255
    assert white.b == 255
    assert white.a == 255


def test_vector2_initialization_and_validity():
    vec = FatalityAPI.Draw.Vector2(1.0, 2.0)
    assert vec.x == 1.0
    assert vec.y == 2.0
    assert vec.is_valid()

    invalid_vec = FatalityAPI.Draw.Vector2(float("inf"), 2.0)
    assert not invalid_vec.is_valid()


def test_vector3_initialization_and_validity():
    vec = FatalityAPI.Vector3(1.0, 2.0, 3.0)
    assert vec.x == 1.0
    assert vec.y == 2.0
    assert vec.z == 3.0
    assert vec.is_valid()

    invalid_vec = FatalityAPI.Vector3(float("nan"), 2.0, 3.0)
    assert not invalid_vec.is_valid()


def test_gui_control_creation():
    gui = FatalityAPI.GUI()
    control_id = gui.control_id("example_control")
    assert control_id in gui.ids

    control = FatalityAPI.GUI.Control(gui, control_id)
    assert control.id == control_id
    assert control.id_string == str(control_id)
    assert control.is_visible


def test_gui_checkbox():
    gui = FatalityAPI.GUI()
    checkbox = gui.checkbox(1234)
    checkbox.tooltip("Example checkbox")
    assert isinstance(checkbox, FatalityAPI.GUI.Checkbox)
    assert checkbox.id == 1234
    assert checkbox.get_value().get() is True


def test_gui_context_find():
    gui = FatalityAPI.GUI()
    checkbox = gui.checkbox(gui.control_id("example_checkbox"))
    found_checkbox = gui.ctx.find("example_checkbox")
    assert checkbox.id == found_checkbox.id


def test_game_screen_size():
    game = FatalityAPI.Game()
    screen_size = game.engine.get_screen_size()
    assert screen_size == (1920, 1080)


def test_entities_local_pawn():
    entities = FatalityAPI.Entities()
    local_pawn = entities.get_local_pawn()
    assert local_pawn.name == "LocalPlayer"
    assert local_pawn.is_alive()


def test_entities_pawn_is_enemy():
    entities = FatalityAPI.Entities()
    local_pawn = entities.get_local_pawn()
    enemy_pawn = FatalityAPI.Entities.Pawn("Enemy", entities.players)
    enemy_pawn.team = 1 if local_pawn.team == 0 else 0

    assert enemy_pawn.is_enemy()


def test_entities_pawn_equal():
    entities = FatalityAPI.Entities()
    local_pawn = entities.get_local_pawn()
    enemy_pawn = FatalityAPI.Entities.Pawn("Enemy", entities.players)
    enemy_pawn.team = 1 if local_pawn.team == 0 else 0

    assert not enemy_pawn == local_pawn
    assert enemy_pawn != local_pawn
    assert None != local_pawn


def test_events_present_queue():
    events = FatalityAPI.Events()
    mock_callback = MagicMock()
    events.present_queue.add(mock_callback)

    # Callback should be invoked 10 times
    assert mock_callback.call_count == 10
