from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#colors
red = color.red
green = color.lime
blue = color.blue
white = color.white

#basic app setup and enviorment setup
app = Ursina()
player = FirstPersonController()
sky = Sky()



#texture loading
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
hotbar_texture   = load_texture('assets/hotbar.png')

#variables
block_pick = 1
clear = True

class Voxel(Button):
    def __init__(self,position = (0,0,0),texture = grass_texture):
        super().__init__(
        parent = scene,
        position = position,
        model = 'assets/block',
        origin_y = 0.5,
        texture = texture,
        color = color.color(0,0,random.uniform(0.9,1)),
        scale = 0.5,
        disabled = False)

    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            if key == "right mouse down":
                if block_pick == 1: tex = grass_texture
                if block_pick == 2: tex = dirt_texture
                if block_pick == 3: tex = brick_texture
                if block_pick == 4: tex = stone_texture
                voxel = Voxel(position= self.position + mouse.normal,texture = tex)
        
        
            
    

class Sky(Entity):


    def __init__(self):
        super().__init__(
        parent = scene,
        model = "sphere",
        texture = sky_texture,
        scale = 150,
        double_sided = True
        )


class ItemShow(Entity):
    def __init__(self,texture = "assets/grassBlock.png"):
        super().__init__(
        parent = camera.ui,
        model = "quad",
        texture = texture,
        position = Vec2(0,-0.34),
        scale = (0.15,0.15)
        )


class Hand(Entity):
    def __init__(self):
        super().__init__(
        parent = camera.ui,
        model = "assets/arm",
        texture = arm_texture,
        scale = 0.2,
        rotation = Vec3(150,-10,0),
        position = Vec2(0.6,-0.6)
        )

    def active(self):
        self.position = Vec2(0.5,-0.5)

    def passive(self):
        self.position = Vec2(0.6,-0.6)

def update():
    global block_pick
    global clear
    
    if player.y <= -5:
        player.y = 5
        player.x = 8
        player.z = 8
        vox = Voxel((player.x,player.y-5,player.z))

    if held_keys['c']:
        player.y = 5
        player.x = 8
        player.z = 8
        clear = True



    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']: 
        block_pick = 1
        Hotbar = ItemShow("assets/grassBlock.png")
    if held_keys['2']: 
        block_pick = 2
        Hotbar = ItemShow("assets/dirt.png")
    if held_keys['3']: 
        block_pick = 3
        Hotbar = ItemShow("assets/brick.png")
    if held_keys['4']: 
        block_pick = 4
        Hotbar = ItemShow("assets/stone.png")



for n in range(20):
    for m in range(20):
        voxel = Voxel(position = (m,0,n))
        for i in range(1):
            voxel = Voxel(position = (m,i-1,n),texture = dirt_texture)


#more thing loading
hand = Hand()
Hotbar = ItemShow()

if __name__ == '__main__':  
    window.title = "Minecraft python edition"
    window.exit_button.visible = False
    window.borderless = False
    app.run()