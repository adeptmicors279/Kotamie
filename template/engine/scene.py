from .engine import Engine
import  pygame
import yaml

class Scene:
    def __init__(self):
        # 初始化参数,详见config.yml
        with open("./config.yml","r") as conf:
            config = yaml.safe_load(conf)
        self.resolution = (config['window']['width'], config['window']['height'])
        self.fps = config["fps"]
        self.is_scene = False
        self.name = config["name"]
        self.engine = Engine("./scripts/main.ks")
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

    def create_char(self):
        # 创建角色
        pass

    def char_action(self):
        # 角色动作
        pass

    def create_choice(self):
        pass

    def play_sound(self):
        pass

    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # 点击推进
                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        next(self.runner)
                    except StopIteration:
                        pass

            # 每帧都绘制当前状态
            self.screen.blit(self.scene, (0, 0))
            pygame.display.update()
            self.clock.tick(self.fps)
'''if __name__ == "__main__":
    a = Scene()
    a.create_window()
    a.create_scene("intro_blade.jpg")
    a.run()
    a.switch_scene("intro_freedom.jpg")
'''