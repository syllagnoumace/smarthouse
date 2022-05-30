input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    music.playMelody("G F G A - F E D ", 120)
    basic.showString("Time of Lunch!")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Var1 = "" + Var1 + "A"
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (DoorLock == Var1) {
        basic.showLeds(`
            # . . . #
                        # . . . #
                        . # . # .
                        . . # . .
                        . . # . .
        `)
    } else {
        basic.showLeds(`
            # # # . .
                        # . # . .
                        # # # . .
                        # . . # .
                        # . . . #
        `)
    }
    
    basic.pause(1000)
    basic.clearScreen()
    Var1 = ""
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Var1 = "" + Var1 + "B"
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    earthquakeNumber = 0
    earthquakeNumber += 1
    basic.showNumber(earthquakeNumber)
})
let rain : game.LedSprite = null
let Temperature = 0
let earthquakeNumber = 0
let Var1 = ""
let DoorLock = ""
basic.showString("Welcome to Smart House!")
basic.showIcon(IconNames.Happy)
basic.pause(100)
basic.clearScreen()
DoorLock = "ABABA"
Var1 = ""
basic.forever(function on_forever() {
    
    Temperature = input.temperature()
    if (input.lightLevel() < 128) {
        basic.showLeds(`
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        `)
        basic.clearScreen()
    }
    
    if (Temperature >= 45) {
        basic.showString("risk of fire!")
        music.ringTone(932)
    }
    
    if (Temperature <= 20) {
        basic.showString("turn on the radiator!")
    }
    
    if (Temperature >= 30) {
        basic.showString("turn on the air conditioner!")
    }
    
    if (Temperature < 7) {
        rain = game.createSprite(randint(0, 4), 2)
        rain.change(LedSpriteProperty.Y, 1)
        basic.pause(5000)
        rain.delete()
    }
    
    if (earthquakeNumber == 1) {
        soundExpression.sad.playUntilDone()
    }
    
})
