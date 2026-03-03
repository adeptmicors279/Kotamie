'''
主程序入口
'''

'''from engine import Engine

def main():
    engine = Engine("./scripts/main.ks")
    engine.run()


if __name__ == "__main__":
    main()
'''
from engine import Scene

def main():
    scene = Scene()
    scene.create_window()
    scene.create_scene("./engine/intro_blade.jpg")
    scene.run()

if __name__ == "__main__":
    main()