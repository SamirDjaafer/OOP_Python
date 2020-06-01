class Animal:
    def __init__(self, limbs=4, height="0.5m", weight="7kg"):
        self.limbs = limbs
        self.height = height
        self.weight = weight

    def jump(self):
        return "Woooosh! I just jumped."

    def yawn(self):
        return "*YAWN*.. So tired..."

    def eat(self, food):
        return f"I'm gonna eat this {food}"

