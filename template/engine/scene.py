from .engine import Engine
from .action import Action
import  pygame
import yaml

class Scene:
    def __init__(self):
        # 初始化参数,详见config.yml
        with open("./config.yml","r") as conf:
            config = yaml.safe_load(conf)
        self.resolution = (config['window']['width'], config['window']['height'])
        self.fps = config["fps"]
        # 状态机二则
        self.is_scene = False
        self.is_game = False

        self.char_action = None # 初始化char_action
        self.name = config["name"]
        self.engine = Engine("./scripts/main.ks",self)
        self.runner = self.engine.run()

    def create_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.name)


    def create_scene(self, scene):
        # 没有scene创建scene
        self.scene = pygame.image.load(f"{scene}").convert()  # 背景图片
        self.is_scene = True

    def dialog(self):
        # 对话
        pass

    def create_char(self, char_name, char_img, char_pos, anchor, x_offset, y_offset, char_action):
        # 创建角色
        self.char_img = pygame.image.load(char_img).convert_alpha()
        # 覆盖图片路径为pygame实例并放入字典便于执行
        self.characters[f"{char_name}"] = {
            "filepath": f"{char_img}",
            "position": f"{char_pos}",
            "anchor": f"{anchor}",
            "x_offset": f"{x_offset}",
            "y_offset": f"{y_offset}",
            "action": f"{char_action}"
        }
        if char_action:
            self.char_action = Action(char_name, char_action)



    def create_choice(self):
        pass

    def play_sound(self):
        pass

    def draw(self):
        # 每帧都绘制当前状态
        self.screen.blit(self.scene, (0, 0))  # 重绘背景
        for char in self.characters.values():  # 重绘人物
            if char["anchor"]:
                self.screen.blit("待定！！！") # 以锚点为基础渲染
            else:
                # 关闭锚点直接渲染到坐标
                self.scene.blit()


    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # 点击推进
                if event.type == pygame.MOUSEBUTTONDOWN and self.is_game:
                    try:
                        next(self.runner)
                    except StopIteration:
                        pass
            self.draw() # 绘制
            pygame.display.update()
            self.clock.tick(self.fps)