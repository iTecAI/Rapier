import pyautogui
from PIL import ImageFile, Image
import mouse
import time
import tempfile
import keyboard
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

NEXT = [6808, 2082]
DELAY = 5


def acquire_bounds() -> list[tuple[int]]:
    print("Select upper left bound ...")
    time.sleep(5)
    upper_left = pyautogui.position()

    print("Select lower right bound ...")
    time.sleep(5)
    lower_right = pyautogui.position()

    return [upper_left, lower_right]


if __name__ == "__main__":
    """
    upper_left, lower_right = acquire_bounds()
    print(upper_left, lower_right)
    print("Starting... Press ENTER to finish")
    time.sleep(DELAY)
    count = 0
    mouse.move(*NEXT, absolute=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        while count < 147:
            pyautogui.screenshot(
                os.path.join("test", f"{count}-img.png"),
                region=(
                    upper_left[0],
                    upper_left[1],
                    lower_right[0] - upper_left[0],
                    lower_right[1] - upper_left[1],
                ),
            )
            pyautogui.mouseDown()
            pyautogui.sleep(0.05)
            pyautogui.mouseUp()
            time.sleep(DELAY)
            count += 1
    """

    imgs = sorted(os.listdir("test"))
    image_objs = [Image.open(os.path.join("test", i)).convert("RGB") for i in imgs]
    image_objs[0].save("out.pdf", save_all=True, append_images=image_objs[1:])
