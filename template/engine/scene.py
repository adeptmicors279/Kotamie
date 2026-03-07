from .engine import Engine
from .action import Action
import  pygame
import yaml

class Scene:
    def __init__(self):
        # 初始化参数,详见config.yml
        with open("./config.yml","r") as conf:
            config = yaml.safe_load(conf)
        # 基本信息
        self.resolution = (config['window']['width'], config['window']['height'])
        self.fps = config["fps"]
        self.name = config["name"]

        # 初始化anchor坐标
        self.left = (self.resolution[0]/5, self.resolution[1]/2)
        self.center = (self.resolution[0]*2/5, self.resolution[1]/2)
        self.right = (self.resolution[0]*3/5, self.resolution[1]/2)

        # 初始化characters队列
        self.characters = {}
        # 状态机
        self.is_scene = False # 目前不知道有没有用???
        self.is_game = False # 检测是否在游戏内，如若是，True并且等待鼠标点击激活engine内的yield
        self.char_action = None # 初始化char_action

        # 调用engine
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
        char_img = pygame.image.load(char_img).convert_alpha()
        # 覆盖char_pos的文本为坐标，使其可以直接调用
        if char_pos == "left":
            char_pos = self.left
        elif char_pos == "center":
            char_pos = self.center
        elif char_pos == "right":
            char_pos = self.right
        # 覆盖图片路径为pygame实例并放入字典便于执行
        self.characters[f"{char_name}"] = {
            "image": char_img,
            "position": char_pos,
            "anchor": anchor,
            "x_offset": x_offset,
            "y_offset": y_offset,
            "action": char_action
        }


    def create_choice(self):
        pass

    def play_sound(self):
        pass

    def draw_scene(self):
        # 每帧都绘制当前状态
        # 重绘背景
        self.screen.blit(self.scene, (0, 0))

    def draw_characters(self):
        # 重绘人物
        for char in self.characters.values():
            if char["anchor"] and char["action"] is None:
                # 以锚点为基础渲染
                self.screen.blit(
                    char["image"],
                    (char["x_offset"] + char["position"][0],
                            char["y_offset"] + char["position"][1])
                )
            elif not char["anchor"] and char["action"] is None:
                # 关闭锚点直接渲染到坐标
                self.screen.blit(
                    char["image"],
                    (char["x_offset"], char["y_offset"])
                )
            elif char["action"]:
                # 使用action进行操作
                coordinates = Action()

                pass

    def draw_ui(self):
        pass


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
            # 绘制
            self.draw_scene()
            self.draw_characters()
            # self.draw_ui()

            pygame.display.update()
            self.clock.tick(self.fps)