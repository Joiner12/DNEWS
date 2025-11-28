from pynput import mouse, keyboard
from math import sqrt
distance = 0


def on_scroll(x, y, dx, dy):
    """鼠标滚轮滚动回调函数"""
    global distance
    if dy > 0:
        print(f'向上滚动 at ({x}, {y})')
    else:
        print(f'向下滚动 at ({x}, {y})')
    if dx != 0 or dy != 0:
        distance += sqrt(abs(dx*dx) + abs(dy*dy))
        print(f'当前距离：{distance*0.2275/1000/1000}')


def on_press(key):
    """键盘按键按下回调函数"""
    # # 检查是否按下了 Ctrl+C
    # if key == keyboard.KeyCode.from_char('c') and hasattr(key, 'ctrl') and key.ctrl:
    #     print("检测到 Ctrl+C 组合键，退出程序")
    #     # 停止监听器
    #     mouse_listener.stop()
    #     keyboard_listener.stop()
    #     return False  # 返回False以停止监听器

    # 也可以使用 ESC 键退出
    if key == keyboard.Key.esc:
        print("按下ESC键，退出程序")
        mouse_listener.stop()
        keyboard_listener.stop()
        return False


# 创建并启动鼠标和键盘监听器
mouse_listener = mouse.Listener(on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

# 等待监听器完成
mouse_listener.join()
keyboard_listener.join()
