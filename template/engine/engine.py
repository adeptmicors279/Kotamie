from .scripts import Script

class Engine:
    def __init__(self, script):
        self.script = Script(script)      # Script 对象
        self.current_index = 0    # 当前执行到第几个 Node
        self.end = False

    def run(self):
        while self.current_index < len(self.script.nodes) and not self.end:
            node = self.script.nodes[self.current_index]
            self.current_index += 1
            node.execute(self)    # 这里把 engine 传给 Node
            yield

    # engine 对外提供的接口，供 Node 调用
    def show_dialog(self, character, text):
        print(f"{character or '旁白'}: {text}")

    def jump_to(self, label):
        if label in self.script.labels:
            self.current_index = self.script.labels[label]

    def switch_scene(self, scene):
        print(f"切换场景: {scene}")

    def show_char(self, char, mood, x_offset=0, y_offset=0, action=None):
        print(f"显示 {char} {mood} 在 ({x_offset},{y_offset}) 动作: {action}")

    def show_char_withanchor(self, char, mood, position, x_offset=0, y_offset=0, action=None):
        print(f"显示 {char} {mood} 在 {position} 锚点偏移({x_offset},{y_offset}) 动作: {action}")

    def show_choice(self, question, choice_text, command):
        print(f"选择: {question} -> {choice_text} 执行 {command}")

    def play_sound(self, audio):
        print(f"播放音乐{audio}")

    def end_game(self):
        self.end =True
        print("终止游戏")

