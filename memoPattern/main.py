from memoPattern.caretaker import Caretaker
from memoPattern.originator import Originator

"""
备忘录模式demo
"""
if __name__ == "__main__":
    originator = Originator()
    originator.propdata = "首次操作"
    memo = originator.createMemo()
    caretaker = Caretaker()
    caretaker.addMemo(memo)
    print(f"originator.propdata,op1:{originator.propdata}")
    originator.propdata = "二次操作"
    memo = originator.createMemo()
    caretaker.addMemo(memo)
    print(f"originator.propdata,op2:{originator.propdata}")
    # 从备忘录中恢复
    originator.restoreMemo(caretaker.getMemo())
    print(f"originator.propdata,restore:{originator.propdata}")
