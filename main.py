from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy import platform
from kivy.app import App
from kivy.properties import NumericProperty #เป็นคลาสที่ใช้สร้าง property สำหรับเก็บค่าตัวเลข 
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.clock import Clock
from kivy.core.window import Window

class MainWidget(Widget):
    from transforms import transform, transform_2D, transform_perspective
    from user_actions import keyboard_closed,on_keyboard_up, on_keyboard_down, on_touch_up, on_touch_down
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    V_NB_LINES = 4
    V_LINES_SPACING = .1 # precentage in screen width
    vertical_lines = []
    
    H_NB_LINES = 15
    H_LINES_SPACING = .1  #  percentage in screen height
    horizontal_lines = []
    
    SPEED = 4
    current_offset_y = 0
    
    SPEED_x = 12
    current_offset_x = 0
    current_offset_x = 0
    
    def __init__(self, **kwargs):
        super(MainWidget,self).__init__(**kwargs)
        #print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        
        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
    def is_desktop(self):
        if platform in ('linux', 'windows', 'macosx'):
            return True
        return False
  
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1) #กำหนดสีของเส้นเป็นขาว
            #self.line = Line(points=[100, 0, 100, 100]) #ลักษณะของเส้นที่ถูกสร้าง
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line(points=[0, 0, 0, 0]))
                
    def get_line_x_from_index(self, index):
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width
        offset = index - 0.5
        line_x = central_line_x + offset * spacing + self.current_offset_x
        return line_x
    
    def get_line_y_from_index(self, index):
                
        specing_y = self.H_LINES_SPACING*self.height
        line_y = index * specing_y - self.current_offset_y
        return line_y
                
    def update_vertical_lines(self):
        # -1 0 1 2
        start_index = -int(self.V_NB_LINES/2) + 1
        for i in range(start_index, start_index + self.V_NB_LINES):
                line_x = self.get_line_x_from_index(i)
                
                x1, y1 = self.transform(line_x, 0)
                x2, y2 = self.transform(line_x, self.height)
                self.vertical_lines[i].points = [x1, y1, x2, y2]
                
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1) #กำหนดสีของเส้นเป็นขาว
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())
                
    def update_horizontal_lines(self):
        # central_line_x = int(self.width / 2)
        # spacing = self.V_LINES_SPACING * self.width
        # offset = int(self.V_NB_LINES/2) - 0.5
        start_index = -int(self.V_NB_LINES/2) + 1
        end_index = start_index + self.V_NB_LINES - 1
        
        specing_y = self.H_LINES_SPACING*self.height
        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)
        
        for i in range(0, self.H_NB_LINES):
                line_y = self.get_line_y_from_index(i)
                x1, y1 = self.transform(xmin, line_y)
                x2, y2 = self.transform(xmax, line_y)
                self.horizontal_lines[i].points = [x1, y1, x2, y2]
    
    def update(self, dt):
        # print("dt: " + str(dt*60)) 
        time_factor = dt*60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        # self.current_offset_y += self.SPEED * time_factor
        
        specing_y = self.H_LINES_SPACING * self.height
        if self.current_offset_y >= specing_y:
            self.current_offset_y -= specing_y
            
        # self.current_offset_x += self.current_offset_x * time_factor
    
class CompsuApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    CompsuApp().run()