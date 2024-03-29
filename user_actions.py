def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'd':
        self.current_speed_x = self.SPEED_x
    elif keycode[1] == 'a':
        self.current_speed_x = -self.SPEED_x
    return True

def on_keyboard_up(self, keyboard, keycode):
    if keycode[1] == 'd' or keycode[1] == 'a':
        self.current_speed_x = 0
    return True

def on_touch_down(self, touch):
    if touch.x < self.width/2:
        # print("<-")
        self.current_speed_x = self.SPEED_x
    else:
        # print("->")
        self.current_speed_x = -self.SPEED_x

def on_touch_up(self, touch):
    #print("up")
    self.current_speed_x = 0
    return True
    
def on_motion(self, etype, motionevent):
    if etype == 'begin':
        self.last_x = motionevent.motion_x
    elif etype == 'update':
        self.calculate_offset_x(motionevent.motion_x)
    elif etype == 'end':
        pass
