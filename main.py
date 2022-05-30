def on_pin_pressed_p0():
    music.play_melody("G F G A - F E D ", 120)
    basic.show_string("Time of Lunch!")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global Var1
    Var1 = "" + Var1 + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Var1
    if DoorLock == Var1:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        . # . # .
                        . . # . .
                        . . # . .
        """)
    else:
        basic.show_leds("""
            # # # . .
                        # . # . .
                        # # # . .
                        # . . # .
                        # . . . #
        """)
    basic.pause(1000)
    basic.clear_screen()
    Var1 = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Var1
    Var1 = "" + Var1 + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global earthquakeNumber
    earthquakeNumber = 0
    earthquakeNumber += 1
    basic.show_number(earthquakeNumber)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

rain: game.LedSprite = None
Temperature = 0
earthquakeNumber = 0
Var1 = ""
DoorLock = ""
basic.show_string("Welcome to Smart House!")
basic.show_icon(IconNames.HAPPY)
basic.pause(100)
basic.clear_screen()
DoorLock = "ABABA"
Var1 = ""

def on_forever():
    global Temperature, rain
    Temperature = input.temperature()
    if input.light_level() < 128:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.clear_screen()
    if Temperature >= 45:
        basic.show_string("risk of fire!")
        music.ring_tone(932)
    if Temperature <= 20:
        basic.show_string("turn on the radiator!")
    if Temperature >= 30:
        basic.show_string("turn on the air conditioner!")
    if Temperature < 7:
        rain = game.create_sprite(randint(0, 4), 2)
        rain.change(LedSpriteProperty.Y, 1)
        basic.pause(5000)
        rain.delete()
    if earthquakeNumber == 1:
        soundExpression.sad.play_until_done()
basic.forever(on_forever)
