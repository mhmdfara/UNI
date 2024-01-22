import tensorflow as tf 
import numpy as np 

train_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
train_labels = np.array([0, 1, 1, 0])

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(2,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(20, activation='relu'), 
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(train_data, train_labels, epochs=1000, verbose=0)


test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = model.predict(test_data)
rounded_predictions = np.round(predictions)


for i in range(len(test_data)):
    print(f"Input: {test_data[i]}, Predicted Output: {rounded_predictions[i]}")
