class SceneMananger(object):
    def __init__(self):
        #self.go_to(TitleScene())
        pass
    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self
