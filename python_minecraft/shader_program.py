from settings import *

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.context = app.context
        # ----- SHADERS
        self.quad = self.get_program(shader_name="quad")
        # -----
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        pass

    def update(self):
        pass
    
    def get_program(self, shader_name):
        with open (f'python_minecraft/shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open (f'python_minecraft/shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        
        program = self.context.program(vertex_shader = vertex_shader, fragment_shader = fragment_shader)
        #returns a shader instance
        return program