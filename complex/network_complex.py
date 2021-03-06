from tensorflow import keras

import pandas as pd
import numpy as np

train_df = pd.read_csv('train(2).csv')

np.random.shuffle(train_df.values)

print(train_df.head())

model = keras.Sequential([
    keras.layers.Dense(256, input_shape=(2,), activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(2, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

x = np.column_stack((train_df.x.values, train_df.y.values))

model.fit(x, train_df.color.values, batch_size=32, epochs=20)

test_df = pd.read_csv('test(2).csv')
test_x = np.column_stack = np.column_stack((test_df.x.values, test_df.y.values))

print("EVALUATION")
model.evaluate(test_x, test_df.color.values)

print("Prediction: ", model.predict(np.array([[0, 3]])))
