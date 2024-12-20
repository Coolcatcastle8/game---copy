class ActionKind(Enum):
    Walking = 0
    Idle = 1
    Jumping = 2
@namespace
class SpriteKind:
    menu = SpriteKind.create()
    pproj = SpriteKind.create()
    bproj = SpriteKind.create()
    weapon = SpriteKind.create()
@namespace
class MultiplayerState:
    Class = MultiplayerState.create()
    joined = MultiplayerState.create()
    ready = MultiplayerState.create()
    level = MultiplayerState.create()
def intermission():
    global gameState
    gameState = "intermission"

def on_player4_connected():
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR),
        sprites.create(assets.image("""
            ss
        """), SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)).set_position(120, 100)
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def gaming():
    global gameState
    gameState = "gaming"
    sprites.destroy_all_sprites_of_kind(SpriteKind.menu, effects.ashes, 500)
    sprites.destroy_all_sprites_of_kind(SpriteKind.text, effects.ashes, 500)
    controller.player1.move_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))
    controller.player2.move_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)))
    controller.player3.move_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)))
    controller.player4.move_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)))
    pause(1000)
    wave1()
def weapons():
    if gameState == "gaming":
        pass

def on_button_multiplayer_left_released(player2):
    if gameState == "gaming":
        characterAnimations.clear_character_state(mp.get_player_sprite(player2))
        characterAnimations.set_character_state(mp.get_player_sprite(player2),
            characterAnimations.rule(Predicate.FACING_LEFT))
mp.on_button_event(mp.MultiplayerButton.LEFT,
    ControllerButtonEvent.RELEASED,
    on_button_multiplayer_left_released)

def on_button_multiplayer_right_released(player22):
    if gameState == "gaming":
        characterAnimations.clear_character_state(mp.get_player_sprite(player22))
        characterAnimations.set_character_state(mp.get_player_sprite(player22),
            characterAnimations.rule(Predicate.FACING_RIGHT))
mp.on_button_event(mp.MultiplayerButton.RIGHT,
    ControllerButtonEvent.RELEASED,
    on_button_multiplayer_right_released)

def on_menu_pressed():
    global listen
    if gameState == "characterselection":
        if readyplayers > 0:
            if mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
                MultiplayerState.ready) == 0:
                sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))
            if mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
                MultiplayerState.ready) == 0:
                sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)))
            if mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
                MultiplayerState.ready) == 0:
                sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)))
            if mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
                MultiplayerState.ready) == 0:
                sprites.destroy(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR)))
            gaming()
        elif listen == 1:
            game.splash("press A to ready up.")
            listen = 2
        elif listen == 2:
            game.splash("bro at LEAST ONE.")
            listen = 3
        elif listen == 3:
            game.splash("...okay then.")
            game.splash("just hang out here, I guess.")
        else:
            game.splash("insufficient players!")
            game.splash("one or more okay?")
            listen = 1
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

def hpbar():
    pass
# shows every enemy in the game!
def enemies():
    global enemylist
    enemylist = [assets.image("""
        babydino
    """)]

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    sprites.destroy(sprite)
sprites.on_overlap(SpriteKind.bproj, SpriteKind.enemy, on_on_overlap)

# shows if a player is ready to start
def showready():
    if gameState == "characterselection":
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
            MultiplayerState.ready) == 1:
            ready1.set_image(img("""
                f f f f f f f f f f f f f f f f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f f f f f f f f f f f f f f f f
            """))
            ready12.set_text("ready")
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
            MultiplayerState.ready) == 1:
            ready2.set_image(img("""
                f f f f f f f f f f f f f f f f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f f f f f f f f f f f f f f f f
            """))
            ready22.set_text("ready")
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
            MultiplayerState.ready) == 1:
            ready3.set_image(img("""
                f f f f f f f f f f f f f f f f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f f f f f f f f f f f f f f f f
            """))
            ready32.set_text("ready")
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
            MultiplayerState.ready) == 1:
            ready4.set_image(img("""
                f f f f f f f f f f f f f f f f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f . . . . . . . . . . . . . . f 
                                f f f f f f f f f f f f f f f f
            """))
            ready42.set_text("ready")

def on_button_multiplayer_left_pressed(player23):
    if gameState == "characterselection":
        mp.set_player_state(player23, MultiplayerState.Class, 1)
        mp.get_player_sprite(player23).set_image(assets.image("""
            ss
        """))
    if gameState == "gaming":
        characterAnimations.clear_character_state(mp.get_player_sprite(player23))
        characterAnimations.set_character_state(mp.get_player_sprite(player23),
            characterAnimations.rule(Predicate.MOVING_LEFT))
mp.on_button_event(mp.MultiplayerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_left_pressed)

def ss1():
    pass
def wave1():
    global spawns, babydino
    scene.set_background_image(img("""
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999111111111119999999999999999999999999999999999999991111999999999999999999999999999999999999999999111111111111
                99999999999999999999999999999999999999999999999999991ddddddddd19999999999999999999999999991111199999991dd11999999999999999999999999999999999999999991dddddddddd1
                99999999999999999999999999999911111999999999999999991ddddddddd19999999999999999999999999991ddd199999991ddd1999999999999999999991111999999999999999991dddddddddd1
                9999999999999999999999999999911ddd1199999999999999991d11dddddd19999999999999999999999999111ddd111999911ddd1199999999999999999911dd1199999999999999991dd1d1ddddd1
                999999999999999999999999999911ddddd199999999999999991ddddddd1d199999999111999999111111191ddddddd199991ddddd19999999999999999111dddd199999999999999991dddddd11dd1
                99999911119999999999999999991dddddd199911199999999991ddddddddd1999999911d19999991ddddd191ddddddd199911ddddd119999999999999991dddddd199911119999999991dddddddddd1
                9999991dd19999999999999999991ddd1d119991d199999999991ddddddddd199999991dd19999991ddddd191ddddddd199911ddddd119999999999999991ddd1d119991dd19999999991dddd1ddddd1
                1111111dd19111111991111111111dddddd19111d111999999991ddddddd1d111111111dd19999991ddddd111d11dddd19111ddddddd11111991111111111dddddd19911dd11999999991ddddddd1dd1
                d11dddddd191d1dd1991ddddddddddd1ddd111ddddd1111111111ddddddd1d11d11ddd1dd199999911dd1dd11ddddddd191dddddddddd1dd1991ddddddddddddd1d1111dddd1191111111dddddd11ddd
                dddd1dddd191dddd19911d1dd1ddddddddd111ddddd111dd1dd11ddddddddd11dddd1d1dd11111111dddddd11dd1dddd191ddddddddddddd1991dd1ddd1dddddddd1111dddd1191d11dd1ddddddddddd
                ddddddddd111dd1d1111dddddddddddddddd11dddddd11ddddddddddddddddd1ddddddddd11d11d11ddddddddddddddd191ddddddddddd1d1111dddddddddddddddd11dddddd111ddddddddddddddddd
                d11d1dddd1ddddddd1dd1d1ddddddddddddd11ddddddd1dddd11ddddddddddddd1111ddddddd1ddd11dd1ddddddddddd111ddddddddddddddd1ddd1ddddddddddddd11ddddddd111d11ddddddddddddd
                ddddddddd1ddddddd1dddddddddddddddddddd1dddddd11ddddddddddddddddddddddddddddd1ddd1ddddddddddddddd1d1ddddddddddddddd1dddddddddddddddddddddddddd1dddddddddddddddddd
                cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
                11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc11ccccccccccc11cccccccccccc11ccccccccccc
                11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc
                11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc11cdddddddddc11cddddddddddc11cdddddddddc
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d
                11ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d1111111
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                1111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd111
                111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbcbbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d111d1111d111dd11dd
                d11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11d
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd11111111111d1111d111dd11dd1111111111dddd1111111d
                11ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d111111111ddd111111dddd11dd11111111111d1d1111111
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbccbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                cccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
                bccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccc
                ccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbb
                bbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbddbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddbbbbbbbbbbbbbbbbbdd1111111111dddd11111ddb
                bbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111ddbbbbbbbbbbbbbbbbbdd11111111111d1d11111dd
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                ccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcc
                dbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbd
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    """))
    spawns = [30, 90]
    for index in range(5):
        babydino = sprites.create(assets.image("""
            babydino
        """), SpriteKind.enemy)
        babydino.image.flip_x()
        babydino.set_position(0, randint(10, 110))
        babydino.set_velocity(35, 0)
        pause(2000)
        babydino = sprites.create(assets.image("""
            babydino
        """), SpriteKind.enemy)
        babydino.set_position(160, randint(10, 110))
        babydino.set_velocity(-35, 0)
        pause(2000)

def on_button_multiplayer_right_pressed(player24):
    if gameState == "characterselection":
        mp.get_player_sprite(player24).set_image(assets.image("""
            sc
        """))
        mp.set_player_state(player24, MultiplayerState.Class, 2)
    if gameState == "gaming":
        characterAnimations.clear_character_state(mp.get_player_sprite(player24))
        characterAnimations.set_character_state(mp.get_player_sprite(player24),
            characterAnimations.rule(Predicate.MOVING_RIGHT))
mp.on_button_event(mp.MultiplayerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_right_pressed)

def on_button_multiplayer_b_pressed(player25):
    global readyplayers
    if gameState == "characterselection":
        if mp.get_player_state(player25, MultiplayerState.ready) == 1:
            readyplayers += -1
            mp.set_player_state(player25, MultiplayerState.ready, 0)
            shownotready()
mp.on_button_event(mp.MultiplayerButton.B,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_b_pressed)

def on_button_multiplayer_a_pressed(player26):
    global readyplayers, bullet_projectile, pierce_projectile
    if gameState == "characterselection":
        if mp.get_player_state(player26, MultiplayerState.ready) == 0:
            readyplayers += 1
            mp.set_player_state(player26, MultiplayerState.ready, 1)
            showready()
    if gameState == "gaming" and mp.get_player_state(player26, MultiplayerState.Class) == 1:
        if characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.MOVING_LEFT)) or characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.FACING_LEFT)):
            bullet_projectile = sprites.create_projectile_from_sprite(img("""
                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . 5 5 5 5 5 5 5 5 5 5 5 . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . . 
                                    . . . . . . . . . . . . . . . .
                """),
                mp.get_player_sprite(player26),
                -500,
                0)
            bullet_projectile.set_kind(SpriteKind.bproj)
        if characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.MOVING_RIGHT)) or characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.FACING_RIGHT)):
            bullet_projectile = sprites.create_projectile_from_sprite(assets.image("""
                    bullet projectile
                """),
                mp.get_player_sprite(player26),
                500,
                0)
            bullet_projectile.set_kind(SpriteKind.bproj)
    if gameState == "gaming" and mp.get_player_state(player26, MultiplayerState.Class) == 2:
        if characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.MOVING_LEFT)) or characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.FACING_LEFT)):
            pierce_projectile = sprites.create_projectile_from_sprite(assets.image("""
                    piercing projectile
                """),
                mp.get_player_sprite(player26),
                -250,
                0)
            pierce_projectile.set_kind(SpriteKind.pproj)
        if characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.MOVING_RIGHT)) or characterAnimations.matches_rule(mp.get_player_sprite(player26),
            characterAnimations.rule(Predicate.FACING_RIGHT)):
            pierce_projectile = sprites.create_projectile_from_sprite(assets.image("""
                    piercing projectile
                """),
                mp.get_player_sprite(player26),
                250,
                0)
            pierce_projectile.set_kind(SpriteKind.pproj)
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def on_player2_connected():
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
        sprites.create(assets.image("""
            ss
        """), SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).set_position(120, 20)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

# shows if a player is not ready
def shownotready():
    if gameState == "characterselection":
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.ONE),
            MultiplayerState.ready) == 0:
            ready1.set_image(img("""
                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            """))
            ready12.set_text("not ready")
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.TWO),
            MultiplayerState.ready) == 0:
            ready2.set_image(img("""
                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            """))
            ready22.set_text("not ready")
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.THREE),
            MultiplayerState.ready) == 0:
            ready3.set_image(img("""
                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            """))
            ready32.set_text("not ready")
        if mp.get_player_state(mp.player_selector(mp.PlayerNumber.FOUR),
            MultiplayerState.ready) == 0:
            ready4.set_image(img("""
                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 . . . . . . . . . . . . . . 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            """))
            ready42.set_text("not ready")
def characterselection():
    global gameState, ready1, ready12, ready2, ready22, ready3, ready32, ready4, ready42
    gameState = "characterselection"
    scene.set_background_image(img("""
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    """))
    ready1 = sprites.create(img("""
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """),
        SpriteKind.menu)
    ready1.set_position(40, 20)
    scaling.scale_to_percent(ready1, 200, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    ready12 = textsprite.create("not ready")
    ready12.set_position(40, 40)
    ready2 = sprites.create(img("""
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """),
        SpriteKind.menu)
    ready2.set_position(120, 20)
    scaling.scale_to_percent(ready2, 200, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    ready22 = textsprite.create("not ready")
    ready22.set_position(120, 40)
    ready3 = sprites.create(img("""
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """),
        SpriteKind.menu)
    ready3.set_position(40, 100)
    scaling.scale_to_percent(ready3, 200, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    ready32 = textsprite.create("not ready")
    ready32.set_position(40, 79)
    ready4 = sprites.create(img("""
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 . . . . . . . . . . . . . . 1 
                    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        """),
        SpriteKind.menu)
    ready4.set_position(120, 100)
    scaling.scale_to_percent(ready4, 200, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
    ready42 = textsprite.create("not ready")
    ready42.set_position(120, 79)
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
        sprites.create(assets.image("""
            ss
        """), SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).set_position(40, 20)

def on_player3_connected():
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
        sprites.create(assets.image("""
            ss
        """), SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE)).set_position(40, 100)
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

# first block fixes a VERY annoying bug from the multiplayer extension.

def on_controller_connected(player2):
    mp.set_player_state(player2, 100, 0)
    mp.set_player_state(player2, MultiplayerState.Class, 1)
    mp.set_player_state(player2, MultiplayerState.level, 1)
    mp.set_player_state(player2, MultiplayerState.ready, 0)
mp.on_controller_event(ControllerEvent.CONNECTED, on_controller_connected)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.pproj, SpriteKind.enemy, on_on_overlap2)

pierce_projectile: Sprite = None
bullet_projectile: Sprite = None
babydino: Sprite = None
spawns: List[number] = []
ready42: TextSprite = None
ready4: Sprite = None
ready32: TextSprite = None
ready3: Sprite = None
ready22: TextSprite = None
ready2: Sprite = None
ready12: TextSprite = None
ready1: Sprite = None
enemylist: List[Image] = []
gameState = ""
readyplayers = 0
listen = 0
scene.set_background_image(img("""
    ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
        ................................................................................................................................................................
"""))
ok = True
listen = 0
readyplayers = 0
game.show_long_text("Player 1, press menu to start after selection!",
    DialogLayout.CENTER)
enemies()
characterselection()

def on_update_interval():
    if gameState == "gaming":
        pass
game.on_update_interval(500, on_update_interval)

def on_forever():
    pass
forever(on_forever)
