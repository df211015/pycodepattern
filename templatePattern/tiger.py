from templatePattern.absAnimal import AbsAnimal


class Tiger(AbsAnimal):
    def ready(self):
        print("tiger is ready")

    def hunt(self):
        print("Tiger is ready for hunting")
