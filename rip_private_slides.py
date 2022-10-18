from PIL import Image 
import PIL 
import pyautogui
import time

pdf_list = []

if pyautogui.confirm('After entering the number of slides in next dialog,\nopen the slides presentation in full screen within 3 seconds', title='rip_private_slides by AJ') == "OK":
    slides = int(pyautogui.prompt('Enter number of slides:', title = "rip_private_slides by AJ"))
    time.sleep(3)
    for i in range(0,slides):
        time.sleep(1)
        image = pyautogui.screenshot()
        pyautogui.press('right')
        image.convert('RGB')
        if i != 1:
            pdf_list.append(image)
        else:
            first_image = image
            pdf_list.append(image)
    file_name = pyautogui.prompt('Save as ___ .pdf')
    first_image.save(f"out/{file_name}.pdf", save_all=True, append_images=pdf_list)