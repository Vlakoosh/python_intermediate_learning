from settings import *
from shader_program import ShaderProgram
from scene import Scene
import moderngl as mgl
import pygame as pg
import sys

class PythonMinecraft:
	def __init__(self):
		pg.init()
		#choose openGL 3.3
		pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
		pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
		#prohibit using deprecated functions
		pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
		#set buffer depth value to 24 bits
		pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

		#create pygame window, set it to window resolution, and create an OpenGL context
		pg.display.set_mode(WINDOW_RESOLUTION, flags=pg.OPENGL | pg.DOUBLEBUF )
		self.context = mgl.create_context()

		self.context.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
		
		self.clock = pg.time.Clock()
		self.delta_time = 0
		self.time = 0

		self.is_running = True
		self.on_init()

	def on_init(self):
		self.shader_program = ShaderProgram(self)
		self.scene = Scene(self)

	def update(self):
		self.shader_program.update()
		self.scene.update()

		self.delta_time = self.clock.tick()
		self.time = pg.time.get_ticks() * 0.001
		#show current framerate
		pg.display.set_caption(f'{self.clock.get_fps() : .0f}')

	def render(self):
		#clear frame and depth buffers
		self.context.clear(color=BG_COLOR)
		self.scene.render()
		pg.display.flip()

	def handle_events(self):
		#check for pressing escape key or closing the window to stop the code from running
		for event in pg.event.get():
			if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
				self.is_running = False

	def run(self):
		while self.is_running:
			self.handle_events()
			self.update()
			self.render()
		pg.quit()
		sys.exit()



if __name__ == "__main__":
	app = PythonMinecraft()
	app.run()
