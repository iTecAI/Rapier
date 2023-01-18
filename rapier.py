import pyautogui
import PIL
import mouse
import time
import tempfile
import keyboard
import os

NEXT = [1890, 1020]
DELAY = 1


def acquire_bounds() -> list[tuple[int]]:
    print("Click to start")
    while not mouse.is_pressed():
        pass
    time.sleep(0.5)
    print("Select upper left bound ...")
    while not mouse.is_pressed():
        pass
    upper_left = pyautogui.position()
    time.sleep(0.5)
    print("Select lower right bound ...")
    while not mouse.is_pressed():
        pass
    lower_right = pyautogui.position()
    return [upper_left, lower_right]


if __name__ == "__main__":
    upper_left, lower_right = acquire_bounds()
    print(upper_left, lower_right)
    print("Starting... Press ENTER to finish")
    time.sleep(DELAY)
    count = 0
    mouse.move(*NEXT, absolute=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        while not keyboard.is_pressed("enter"):
            pyautogui.screenshot(os.path.join("test", f"{count}-img.png"), region=(
                upper_left[0], upper_left[1], lower_right[0] - upper_left[0], lower_right[1] - upper_left[1]))
            pyautogui.mouseDown()
            pyautogui.sleep(0.05)
            pyautogui.mouseUp()
            time.sleep(DELAY)
            count += 1
