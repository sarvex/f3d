import sys
if sys.platform.startswith('win32'):
  import os
  os.add_dll_directory(sys.argv[1])

import f3d

dataset = f"{sys.argv[2]}/testing/data/cow.vtp"
reference = f"{sys.argv[2]}/testing/baselines/TestPythonCompareWithFile.png"
output = f"{sys.argv[3]}/Testing/Temporary/TestPythonCompareWithFile.png"
outputDiff = (
    f"{sys.argv[3]}/Testing/Temporary/TestPythonCompareWithFile.diff.png")

f3d.engine.autoloadPlugins()

engine = f3d.engine(f3d.window.NATIVE_OFFSCREEN)
engine.getWindow().setSize(300, 300)

# verify the size is properly set
assert engine.getWindow().getWidth() == 300
assert engine.getWindow().getHeight() == 300

engine.getLoader().loadGeometry(dataset, True)

img = engine.getWindow().renderToImage()
img.save(output)

diff = f3d.image()
error = 0.0

ret = img.compare(f3d.image(reference), 50, diff, error)

if not ret:
  diff.save(outputDiff)

assert ret is True
