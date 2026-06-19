from ursina import camera, held_keys, time

class CameraController:
    def __init__(self):
        print("CameraController initialized")
        self.reset_camera()
        self.rotation_speed = 50
        self.zoom_speed = 5
        self.min_distance = 8
        self.max_distance = 25
    
    def reset_camera(self):
        camera.position = (0, 12, -12)
        camera.rotation_x = 45
        camera.rotation_y = 0
        self.distance = 17
        print("Camera reset to default view")
    
    def update(self):
        # Rotate camera with arrow keys or A/D
        if held_keys['left arrow'] or held_keys['a']:
            camera.rotation_y -= self.rotation_speed * time.dt
        if held_keys['right arrow'] or held_keys['d']:
            camera.rotation_y += self.rotation_speed * time.dt
        
        # Reset camera with R key
        if held_keys['r']:
            self.reset_camera()
    
    def zoom(self, direction):
        # Zoom in/out with mouse scroll
        self.distance -= direction * self.zoom_speed
        self.distance = max(self.min_distance, min(self.max_distance, self.distance))
        
        # Update camera position based on distance
        import math
        angle_rad = math.radians(camera.rotation_y)
        camera.x = self.distance * math.sin(angle_rad)
        camera.z = -self.distance * math.cos(angle_rad)
        camera.y = self.distance * 0.7
