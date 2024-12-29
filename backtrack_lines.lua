local gui_reference = gui.ctx:find("visuals>enemy>backtrack")
local gui_rainbow_enable = gui.checkbox(gui.control_id("rainbow_trail_enable"))
local gui_rainbow_enable_control = gui.make_control("Rainbow Trail", gui_rainbow_enable)
local gui_visibility_check_enable = gui.checkbox(gui.control_id("visibility_check_enable"))
local gui_visibility_check_enable_control = gui.make_control("Backtrack lines: Visibility Check", gui_visibility_check_enable)
gui_rainbow_enable_control.tooltip = "Draws a rainbow trail between the backtrack positions."
gui_visibility_check_enable_control.tooltip = "Not working properly"
gui_reference:add(gui_rainbow_enable_control)
local temp_dot_size = 1

local legitbot = gui.ctx:find("legit>general>enabled")

local player_positions = {}

local screen_w, screen_h = game.engine:get_screen_size()

local function drawing_hue(real_time)
    return draw.color(math.floor(math.sin(real_time * 3) * 127 + 128), math.floor(math.sin(real_time * 3 + 2) * 127 + 128), math.floor(math.sin(real_time * 3 + 4) * 127 + 128))
end

local function on_present_queue()
    local local_player = entities.get_local_pawn()
    local backtrack = legitbot:get_value():get() and 200 or gui.ctx:find("rage>aimbot>general>aimbot"):get_value():get() and 200 or 0  -- assume 200ms for legitbot since the backtrack slider handle is broken

    if backtrack == 0 then
        return
    end

    if local_player == nil or not local_player:is_alive() then
        return
    end

    entities.players:for_each(function(player)
        if player.entity == nil or not player.entity:is_alive() or not player.entity:is_enemy() then
            return
        end

        if local_player == player.entity then
            return
        end

        local head_pos = player.entity:get_eye_pos()

        if not head_pos:is_valid() then
            return
        end

        local last_w2s = nil

        if not player_positions[player.entity:get_name()] then
            player_positions[player.entity:get_name()] = {}
        end

        table.insert(player_positions[player.entity:get_name()], {head_pos, game.global_vars.real_time})

        for index, player_position in pairs(player_positions[player.entity:get_name()]) do
            if game.global_vars.real_time - player_position[2] > backtrack / 1000 then
                table.remove(player_positions[player.entity:get_name()], index)
            else
                if not player_position[1]:is_valid() then
                    return
                end

                local w2s = math.world_to_screen(player_position[1])

                if not w2s then
                    return
                end

                if screen_w >= w2s.x and w2s.x >= 0 and screen_h >= w2s.y and w2s.y >= 0 then
                    visible = true
                    if gui_visibility_check_enable:get_value():get() then
                        if player.entity:should_draw() then
                            visible = true
                        else
                            visible = false
                        end
                    end
                    if last_w2s then
                        if gui_rainbow_enable:get_value():get() then
                            draw.surface:add_line(draw.vec2(w2s.x, w2s.y), draw.vec2(last_w2s.x, last_w2s.y), drawing_hue(game.global_vars.real_time))
                        else
                            draw.surface:add_line(draw.vec2(w2s.x, w2s.y), draw.vec2(last_w2s.x, last_w2s.y), draw.color.white())
                        end
                    end
                    last_w2s = w2s
                end
            end
        end
    end)
end

events.present_queue:add(on_present_queue)