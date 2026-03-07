class Node:
    def execute(self, engine):
        pass


class SayNode(Node):
    def __init__(self, character, text):
        self.character = character
        self.text = text

    def execute(self, engine):
        engine.show_dialog(self.character, self.text)


class JumpNode(Node):
    def __init__(self, label):
        self.label = label

    def execute(self, engine):
        engine.jump_to(self.label)


class LabelNode(Node):
    def __init__(self, name):
        self.name = name

class ChoiceNode(Node):
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices
        print(self.choices)

    def execute(self, engine):
        for choices, command in self.choices.items():
            print(choices,command)
            engine.show_choice(self.question, choices, command)

class SceneNode(Node):
    def __init__(self, scene):
        self.scene = scene

    def execute(self, engine):
        engine.switch_scene(self.scene)

class ShowNode(Node):
    def __init__(self, char, mood, position, anchor, x_offset, y_offset, action):
        self.char = char
        self.mood = mood
        self.position = position
        self.anchor = anchor
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.action = action

    def execute(self, engine):
        engine.show_char(
            self.char, self.mood, self.position, self.anchor, self.x_offset, self.y_offset, self.action
        )

class EndNode(Node):
    def execute(self, engine):
        engine.end_game()

class PlaySoundNode(Node):
    def __init__(self, audio):
        self.audio = audio

    def execute(self, engine):
        engine.play_sound(self.audio)