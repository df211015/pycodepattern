from observePattern.iObserver import IObserver


class ObserverOfAPP(IObserver):
    def update(self, p):
        print(f"ObserverOfAPP -> update,p={p}")
