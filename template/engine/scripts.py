from symbol import yield_expr

from .nodes import SayNode, JumpNode, LabelNode, ChoiceNode, ShowNode, SceneNode, EndNode, PlaySoundNode


class Script:

    def __init__(self, filepath):
        self.nodes = []
        self.labels = {}
        self.in_choice = False #控制是否进入缩进
        self.question = None
        self.choices = {}
        self.load(filepath)
        self.current_index = 0

    def load(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if not self.in_choice:
                i += 1

            if not self.in_choice and not line or line.startswith("//"):
                continue

            # label
            if line.startswith("*") and not self.in_choice:
                label_name = line[1:]
                node = LabelNode(label_name)
                self.labels[label_name] = len(self.nodes)
                self.nodes.append(node)


            # jump
            elif line.startswith("jump") and not self.in_choice:
                _, label = line.split()
                self.nodes.append(JumpNode(label))

            # 对话
            elif line.startswith("@") and not self.in_choice:
                char, text = line[1:].split(":", 1)
                self.nodes.append(SayNode(char.strip(), text.strip()))

            # 旁白
            elif line.startswith(":") and not self.in_choice:
                text = line[1:].strip()
                self.nodes.append(SayNode(None, text))

            # choice
            elif line.startswith("?") and not self.in_choice:
                self.question = line[1:].strip()
                self.in_choice = True

            elif self.in_choice and line.startswith("-"):
                text = line[1:].split("->")[0].strip()
                target = line.split("->")[1].strip()
                self.choices[text] = target
                i += 1

            elif self.in_choice and not line.startswith("-"):
                self.nodes.append(
                    ChoiceNode(question=self.question, choices = self.choices))
                i += len(self.choices)
                #print(i)
                self.in_choice = False
                self.question = None
                self.choices = {}

            # show
            elif line.startswith("show "):
                parts = line[5:].strip().split()  # 去掉 "show "

                char = parts[0]
                mood = parts[1]

                position = "center"
                x_offset = 0
                y_offset = 0
                anchor = True
                action = None

                show_index = 2
                while show_index < len(parts):
                    p = parts[show_index]
                    # 识别是否有锚点与位置
                    if p in ["left", "center", "right"]:
                        position = p
                        anchor = True
                        show_index += 1
                    elif p == "at":
                        x_offset = int(parts[show_index + 1])
                        y_offset = int(parts[show_index + 2])
                        anchor = False
                        show_index += 3
                    elif p == "offset":
                        x_offset = int(parts[show_index + 1])
                        y_offset = int(parts[show_index + 2])
                        anchor = True
                        show_index += 3
                    #检测动作
                    elif p == "action":
                        action = parts[show_index + 1]
                        show_index += 2
                    else:
                        # 未知关键字，报错
                        raise ValueError(f"Unknown show parameter: {p}")
                #print(char,mood,position,anchor,x_offset,y_offset,action)
                self.nodes.append(ShowNode(char, mood, position, anchor, x_offset, y_offset, action))

            elif line.startswith("hide"):
                pass

            elif line.startswith("move"):
                pass

            # bg
            elif line.startswith("bg "):
                scene = line.strip("bg ").strip()
                self.nodes.append(SceneNode(scene))

            elif line == "END":
                self.nodes.append((EndNode()))
                print(self.nodes)

            elif line.startswith("sound "):
                audio = line.strip("sound ").strip()
                self.nodes.append(PlaySoundNode(audio))

            else:
                raise ValueError(f"Unknown line: {line}")





if __name__ == "__main__":
    script = Script("../scripts/main.ks")
