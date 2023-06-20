from observePattern.iObserver import IObserver


class ObserverOfPC(IObserver):

    def update(self, p):
        print(f"ObserverOfPC -> update,p={p}")