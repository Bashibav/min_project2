import pyautogui
import time
import pyperclip

# Give some time to switch to the desired screen (optional)
time.sleep(3)

# Step 1: Click on the icon at (1179, 1049)
pyautogui.click(1350, 1046)
time.sleep(1)
pyautogui.click(335, 400)
time.sleep(1)
# Step 2: Move to (554, 149), then drag to (1897, 931) to select text
pyautogui.moveTo(691, 260)
pyautogui.mouseDown()
pyautogui.moveTo(848, 915, duration=1)  # Drag with smooth transition
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy the selected text (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get the copied text from clipboard
copied_text = pyperclip.paste()

print("Copied Text:", copied_text)
