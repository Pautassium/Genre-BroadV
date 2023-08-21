# *博汇科技* 出品

# This file is designed to:
# 1. Take user singing/melody/music
# 2. Using a trained NN to identify the genres of user's input
# 3. List out the TWO most probable genres

import keras
import json
import numpy as np

#importing this function causes issues...
def load_data(data_path):
    """Loads training dataset from json file.

        :param data_path (str): Path to json file containing data
        :return X (ndarray): Inputs
        :return y (ndarray): Targets
    """

    with open(data_path, "r") as fp:
        data = json.load(fp)

    # convert lists to numpy arrays
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    print("Data succesfully loaded!")

    return  X, y

print("\n\n*博汇科技* 出品 \n\nThis file is designed to:\n 1. Take user singing/melody/music\n 2. Using a trained NN to identify the genres of user's input\n 3. List out the TWO most probable genres")

exec(open("recording.py").read())
exec(open("extract_melody.py").read())

model=keras.models.load_model('model2/model.h5')

#Make the predictor variable:
Melody_path = "data_melody.json"
melody, what = load_data(Melody_path)
model=keras.models.load_model('model2/model.h5')
prediction = model.predict(melody)
genre_names = [
    "blues/布鲁斯",
    "classical/古典",
    "country/乡村",
    "disco/迪斯科",
    "hiphop/嘻哈",
    "jazz/爵士",
    "metal/金属",
    "pop/流行",
    "reggae/雷鬼",
    "rock/摇滚"
]

# Assuming you have the prediction variable with shape (2996, 10)

# Get the index of the genre with the highest probability for each prediction
prediction_indices = np.argmax(prediction, axis=1)
# Map the prediction indices to genre names
prediction_list = [genre_names[index] for index in prediction_indices]

from collections import Counter

# Count occurrences of each element in the list
element_counts = Counter(prediction_list)

# Find the two most common elements and their occurrences
most_common_elements = element_counts.most_common(2)

# Print the results
print("\nThe genre is:\n这首片段的风格是:\n")
for element, count in most_common_elements:
    print(f"{element}")

exec(open("keyfinder.py").read())