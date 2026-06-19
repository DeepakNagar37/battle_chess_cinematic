from ursina import Entity, color, DirectionalLight, AmbientLight, Sky

class BattlefieldEnvironment:
    def __init__(self):
        print("BattlefieldEnvironment initialized")
        self._setup_ground()
        self._setup_platform()
        self._setup_lighting()
        self._setup_sky()
    
    def _setup_ground(self):
        # Large ground plane for battlefield arena
        self.ground = Entity(
            model='plane',
            scale=(50, 1, 50),
            color=color.rgb(40, 35, 30),
            texture='white_cube',
            position=(0, -0.5, 0)
        )
        print("Ground plane created")
    
    def _setup_platform(self):
        # Board platform/base
        self.platform = Entity(
            model='cube',
            scale=(10, 0.3, 10),
            color=color.rgb(60, 50, 40),
            position=(0, -0.15, 0)
        )
        print("Board platform created")
    
    def _setup_lighting(self):
        # Dramatic directional light (main battlefield light)
        self.sun = DirectionalLight()
        self.sun.look_at((1, -1, 1))
        self.sun.color = color.rgb(255, 240, 220)
        
        # Ambient light for visibility
        self.ambient = AmbientLight()
        self.ambient.color = color.rgb(100, 100, 120)
        
        print("Battlefield lighting created")
    
    def _setup_sky(self):
        # Atmospheric dark sky
        self.sky = Sky()
        self.sky.color = color.rgb(30, 30, 40)
        print("Sky created")
