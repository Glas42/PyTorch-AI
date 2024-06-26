import os

PATH = os.path.dirname(os.path.dirname(__file__)) + "\\ModelFiles\\"

count = len(os.listdir(f"{PATH}EditedTrainingData")) / 2

for i, file in enumerate(os.listdir(f"{PATH}EditedTrainingData")):
    if file.endswith(".txt"):
        line = str(open(os.path.join(f"{PATH}EditedTrainingData", file), "r").readline())

        pairs = line.split(',')
        for pair in pairs:
            key, value = pair.split(':')
            if key == 'Correction':
                correction = float(value)
            elif key == 'LeftIndicator':
                left_indicator = 1 if value.lower() == 'true' else 0
            elif key == 'RightIndicator':
                right_indicator = 1 if value.lower() == 'true' else 0
        line = f"{correction},{left_indicator},{right_indicator}"

        with open(os.path.join(f"{PATH}EditedTrainingData", file), "w") as f:
            f.truncate(0)
            f.write(line)

        if i % 10 == 0:
            print(f"{i}/{count} files edited...")