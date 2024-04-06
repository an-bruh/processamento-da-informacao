#EP1_10

vp = int(input())
fn = int(input())
fp = int(input())
vn = int(input())

acc = (vp + vn) / (vp + vn + fp + fn)

prec = vp / (vp + fp)

sens = vp / (vp + fn)

print(f"{acc:.2f}\n{prec:.2f}\n{sens:.2f}\n")