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
from kivy.graphics import Quad
from kivy.graphics import Triangle
from kivy.uix.relativelayout import RelativeLayout
import random
from kivy.lang.builder import Builder

Builder.load_file("menu.kv")

class MainWidget(RelativeLayout): 
    from transforms import transform, transform_2D, transform_perspective
    from user_actions import keyboard_closed,on_keyboard_up, on_keyboard_down, on_touch_up, on_touch_down
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    V_NB_LINES = 8
    V_LINES_SPACING = .1 # precentage in screen width
    vertical_lines = []
    
    H_NB_LINES = 15
    H_LINES_SPACING = .1  #  percentage in screen height
    horizontal_lines = []
    
    SPEED = 1
    current_offset_y = 0
    current_y_loop = 0
    
    SPEED_x = 2
    current_offset_x = 0
    current_speed_x = 0
    
    NB_TILES = 16
    title = []
    titles_coordinates = []
    
    SHIP_WIDTH = .1
    SHIP_HEIGHT = 0.035
    SHIP_BASE_Y = 0.04
    ship = None
    ship_coordinates = [(0, 0), (0, 0), (0, 0)]
    
    state_game_over = False

    # ti_x = 1
    # ti_y = 2
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        #print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        self.init_tiles()
        self.init_ship()
        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinate()
        self.current_speed_x = 0 
        
        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
    def is_desktop(self):
        if platform in ('linux', 'windows', 'macosx'):
            return True
        return False
    
    def init_ship(self):
        with self.canvas:
            Color(1, 0, 0)
            self.ship = Triangle()
            
    def update_ship(self):
        center_x = self.width / 2
        base_y = self.SHIP_BASE_Y * self.height
        ship_half_width = self.SHIP_WIDTH * self.width / 2
        ship_height = self.SHIP_HEIGHT * self.height
        # ...
        #   2
        # 1    3
        # self.transfore
        self.ship_coordinates[0] = (center_x - ship_half_width, base_y)
        self.ship_coordinates[1] = (center_x + ship_half_width, base_y)
        self.ship_coordinates[2] = (center_x, base_y + ship_height)

        x1, y1 = self.transform(*self.ship_coordinates[0])
        x2, y2 = self.transform(*self.ship_coordinates[1])
        x3, y3 = self.transform(*self.ship_coordinates[2])

        self.ship.points = [x1, y1, x2, y2, x3, y3]

    def check_ship_collision(self):
        for i in range(0, len(self.titles_coordinates)):
            ti_x, ti_y = self.titles_coordinates[i]
            if ti_y > self.current_y_loop + 1 :
                return False
            if self.check_ship_collision_with_tile(ti_x, ti_y):
                return True
        return False
    
    
    def check_ship_collision_with_tile(self, ti_x, ti_y):
        xmin, ymin = self.get_titel_coordinates(ti_x, ti_y)
        xmax, ymax = self.get_titel_coordinates(ti_x + 1, ti_y + 1)
        for i in range(0, 3):
            px, py = self.ship_coordinates[i]
            if xmin <= px <= xmax and ymin <= py <= ymax:
                return True
        return False

    
    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1) #กำหนดสีของเส้นเป็นขาว
            for i in range(0, self.NB_TILES):
                self.title.append(Quad())
                
    def pre_fill_tiles_coordinates(self):
        # 10 tiles in a straight line
        for i in range(0, 10):
            self.titles_coordinates.append((0, i))
                
    def generate_tiles_coordinate(self):
        last_x = 0
        last_y = 0
        
        # clean the coordinate that are out of the screen
        # ti_y < self.current_y_loop
        for i in range(len(self.titles_coordinates)-1, -1, -1):
            if self.titles_coordinates[i][1] < self.current_y_loop:
                del self.titles_coordinates[i]
         
        if len(self.titles_coordinates) > 0:
            last_coordinates = self.titles_coordinates[-1]
            last_y = last_coordinates[1] + 1
            last_x = last_coordinates[0]
       
        print("foo1")
            
        for i in range(len(self.titles_coordinates), self.NB_TILES):
            r = random.randint(0, 2)
            # 0 -> straight
            # 1 -> right
            # 2 -> left
            start_index = -int(self.V_NB_LINES/2) + 1
            end_index = start_index + self.V_NB_LINES - 1
            if last_x <= start_index:
                r = 1
            if last_x >= end_index:
                r = 2
            
            
            self.titles_coordinates.append((last_x, last_y))
            if r == 1:
                last_x += 1
                self.titles_coordinates.append((last_x, last_y))
                last_y += 1
                self.titles_coordinates.append((last_x, last_y))
                
            if r == 2:
                last_x -= 1
                self.titles_coordinates.append((last_x, last_y))
                last_y += 1
                self.titles_coordinates.append((last_x, last_y))
                
                
            last_y += 1
      
        print("foo2")
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1) #กำหนดสีของเส้นเป็นขาว
            #self.line = Line(points=[100, 0, 100, 100]) #ลักษณะของเส้นที่ถูกสร้าง
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
                
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
    
    def get_titel_coordinates(self, ti_x, ti_y):
        ti_y = ti_y - self.current_y_loop
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y
    
    def update_tiles(self):
        for i in range(0, self.NB_TILES):
            tile = self.title[i]
            tile_coordinates = self.titles_coordinates[i]
            xmin, ymin = self.get_titel_coordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.get_titel_coordinates(tile_coordinates[0] + 1, tile_coordinates[1] + 1)
            
            # 2 3
            #
            # 1 4
            x1, y1 = self.transform(xmin, ymin)
            x2, y2 = self.transform(xmin, ymax)
            x3, y3 = self.transform(xmax, ymax)
            x4, y4 = self.transform(xmax, ymin)
            tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]
        
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
        self.update_ship()
        self.update_tiles()
        
        if not self.state_game_over:
            speed_y = self.SPEED * self.height / 100
            self.current_offset_y += speed_y * time_factor  # move
            
            specing_y = self.H_LINES_SPACING * self.height
            while self.current_offset_y >= specing_y:
                self.current_offset_y -= specing_y
                self.current_y_loop += 1
                self.generate_tiles_coordinate()
                print("loop : " + str(self.current_y_loop ))
            
            speed_x = self.current_offset_x *self.width / 100
            self.current_offset_x += speed_x * time_factor
            
        if not self.check_ship_collision() and not self.state_game_over: 
            self.state_game_over = True
            print("GAME OVER")
        #print("Current Speed X:", self.current_speed_x)
    
class CompsuApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    CompsuApp().run()