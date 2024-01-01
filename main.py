from kivy.app import App
from kivy.properties import NumericProperty #เป็นคลาสที่ใช้สร้าง property สำหรับเก็บค่าตัวเลข 
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    line = None
    def __init__(self, **kwargs):
        super(MainWidget,self).__init__(**kwargs)
        #print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        
    def on_parent(self, widget, parent):
        #print("ON PARENY W:" + str(self.width) + " H:" +str(self.height))
        pass
    
    def on_size(self, *args):
        #print("ON PARENY W:" + str(self.width) + " H:" +str(self.height))
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        self.init_vertical_lines()
        
    def on_perspective_point_x(self, widget, value):
        #print("PX:" + str(value))
        pass
        
    def on_perspective_point_y(self, widget, value):
        #print("PY:" + str(value))
        pass
    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1) #กำหนดสีของเส้นเป็นขาว
            self.line = Line(points=[self.width/2, 0, self.width/2, 100]) #ลักษณะของเส้นที่ถูกสร้าง [(x1, y1), (x2, y2)]
            
    def update_vertical_lines(self):
        self.line.point = []
            
    
class CompsuApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    CompsuApp().run()
