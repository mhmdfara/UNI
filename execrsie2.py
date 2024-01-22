import tensorflow as tf 
import numpy as np 

input_data = np.array([[0, 0, 0, 0],
                       [0, 0, 0, 1],
                       [0, 0, 1, 0],
                       [0, 0, 1, 1],
                       [0, 1, 0, 0],
                       [0, 1, 0, 1],
                       [0, 1, 1, 0],
                       [0, 1, 1, 1],
                       [1, 0, 0, 0],
                       [1, 0, 0, 1],
                       [1, 0, 1, 0],
                       [1, 0, 1, 1],
                       [1, 1, 0, 0],
                       [1, 1, 0, 1],
                       [1, 1, 1, 0],
                       [1, 1, 1, 1]])

output_labels = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, input_shape=(4,), activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(input_data, output_labels, epochs=1000, verbose=0)

test_inputs = np.array([[0, 0, 0, 1],
                        [1, 0, 1, 0],
                        [1, 1, 1, 1]])

predictions = model.predict(test_inputs)
rounded_predictions = np.round(predictions)

for i in range(len(test_inputs)):
    print(f"Input: {test_inputs[i]}, Predicted Output: {rounded_predictions[i]}")

