import glfw
import moderngl as mgl
import numpy as np

if not glfw.init():
    raise Exception('GLFW出错')

windown = glfw.create_window(800, 600, 'OPGL', None, None)

if not windown:
    glfw.terminate()
    raise Exception('windown出错')

glfw.make_context_current(windown)
ctx = mgl.create_context()


def framebuffer_size_callback(windown, width, height):
    ctx.viewport(0, 0, width, height)


glfw.set_framebuffer_size_callback(windown, framebuffer_size_callback)


def process_input(windown):
    if glfw.get_key(windown, glfw.KEY_ESCAPE) == glfw.PRESS:
        glfw.set_window_should_close(windown, True)


vertex_shader = """
#version 330 core

in vec3 in_vert;

void main()
{
    gl_Position=vec4(in_vert.x,in_vert.y,in_vert.z,1.0);
}
"""

fragment_shader = """
#version  330 core
out vec4 FragColor;
void main()
{
    FragColor=vec4(1.0,0.5,0.2,1);
}
"""

verticcs = np.array([
    -0.5, -0.8, 0.0,
    0.5, -0.1, 0.0,
    0, 0.2, 0
], dtype='f4')

prog = ctx.program(vertex_shader, fragment_shader)
vbo = ctx.buffer(verticcs.tobytes())
vao = ctx.vertex_array(prog, vbo, 'in_vert')

while not glfw.window_should_close(windown):
    process_input(windown)
    # 渲染
    ctx.clear(0.2, 0.3, 0.3)
    vao.render(mgl.TRIANGLES)
    glfw.poll_events()
    glfw.swap_buffers(windown)

glfw.terminate()
