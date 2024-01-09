from modules.hitObject import HitObject

class Beatmap:
    def __init__(self, dir: str, name: str):

        # constants
        CIRCLE_SIZE = 55
        CIRCLE_SCALE = 4
        
        self.dir = dir
        self.name = name
        with open(f"{dir}/{name}", mode = 'r', encoding='utf_8') as file:
            try:
                lines = file.readlines()
                self.generalData = self.get_data("[General]\n", lines)
                self.metadata = self.get_data("[Metadata]\n", lines)
                self.difficulty = self.get_data("[Difficulty]\n", lines)
                self.timingPoints = self.get_timing("[TimingPoints]\n", lines)
            except:
                pass    
        CS = float(self.difficulty['CircleSize'])
        self.circleSize = CIRCLE_SIZE - CIRCLE_SCALE * CS

    def get_timing(self, what: str, where: list):
        a = []
        id = where.index(what)
        end = where.index("\n", id)
        for x in where[id+1:end]:
            a.append([float(y) for y in x.split(',')])
        return a

    def get_data(self, what: str, where: list) -> dict:
        d ={}
        id = where.index(what)
        end = where.index("\n", id)
        for x in where[id+1:end]:
            div = x.index(":")
            d[x[:div].strip()] = x[div+1:-1].strip()
        return d

    def get_hitobjects(self) -> list:
        hit = []
        with open(f"{self.dir}/{self.name}", mode='r', encoding='utf_8') as file:
            lines = file.readlines()
            id = lines.index("[HitObjects]\n")
            for desc in lines[id+1:]:
                hit.append(HitObject(desc, self.difficulty, self.timingPoints))
        return hit
    
    def get_audio(self) -> str:
        return f"{self.dir}/{self.generalData['AudioFilename']}"

    def __repr__(self) -> str:
        return self.name
