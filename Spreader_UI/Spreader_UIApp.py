# imports

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp

KV = '''
    
<ContentNavigationDrawer>:

    ScrollView:

        MDList:
            
            OneLineListItem:
                text: "Login"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen_login"
            
            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "screen_1"

Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager
            
            Screen: 
                name: "screen_login"
                
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.sizeK
                        
                        source: "damocles_background.jpg"                        
                
                MDLabel:
                    text: "Login Page"
                    font_style: "H6"
                    text_color: 1, 0.75, 0.25, 1
                    theme_text_color: "Custom"
                    size_hint: (0.1, 0.025)
                    pos_hint: {'x':.47, 'y':.43}   
                    
                MDTextFieldRound:
                    icon_right: "eye-outline"
                    hint_text: "Username"
                    
                    normal_color: app.theme_cls.accent_color
                    color_active: 0.75, 0.5, 0, 1
                    color_mode: 'accent'
                    
                    size_hint: (0.1, 0.025)
                    pos_hint: {'x':.45, 'y':.4}
                    
                MDTextFieldRound:
                    icon_right: "eye-outline"
                    hint_text: "Password"
                    
                    normal_color: app.theme_cls.accent_color
                    color_active: 0.75, 0.5, 0, 1
                    color_mode: 'accent'
                    
                    size_hint: (0.1, 0.025)
                    pos_hint: {'x':.45, 'y':.37} 
                        
                MDRoundFlatIconButton:
                    text: "Login"
                    text_color: 1, 0.5, 0, 1
                    md_bg_color: 0.4, 0.1, 0.1, 0.75
                    size_hint: (0.07, 0.03)
                    pos_hint: {'x':.425, 'y':.33}             
                    
                    icon: "skull"
                
                MDRoundFlatIconButton:
                    text: "Sign Up"
                    text_color: 1, 0.5, 0, 1
                    md_bg_color: 0.4, 0.1, 0.1, 0.75
                    size_hint: (0.07, 0.03)
                    pos_hint: {'x':.505, 'y':.33}             
                    
                    icon: "skull"  
            
            Screen:
                name: "screen_1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                '''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Spreader_UIApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "50"
        self.theme_cls.accent_palette = "Brown"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style="Dark"

        return Builder.load_string(KV)

Spreader_UIApp().run()
