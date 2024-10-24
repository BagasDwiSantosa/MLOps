import tensorflow as tf
import tensorflow_transform as tft

CATEGORICAL_FEATURES = {
    "Gender": 3,
    "Email_Opt_In": 2,
    "Promotion_Response": 3,
}
NUMERICAL_FEATURES = [
    "Customer_ID",
    "Age",
    "Annual_Income",
    "Total_Spend",
    "Years_as_Customer",
    "Num_of_Purchases",
    "Average_Transaction_Amount",
    "Num_of_Returns",
    "Num_of_Support_Contacts",
    "Satisfaction_Score",
    "Last_Purchase_Days_Ago"
]
LABEL_KEY = "Target_Churn"

def transformed_name(key):
    return key + "_xf"

def convert_num_to_one_hot(label_tensor, num_labels=2):
    one_hot_tensor = tf.one_hot(label_tensor, num_labels)
    return tf.reshape(one_hot_tensor, [-1, num_labels])

def preprocessing_fn(inputs):
    outputs = {}
    
    # Handle categorical features
    for key in CATEGORICAL_FEATURES:
        dim = CATEGORICAL_FEATURES[key]
        # Pastikan input adalah string
        string_value = tf.cast(inputs[key], tf.string)
        # Konversi ke vocabulary index
        int_value = tft.compute_and_apply_vocabulary(
            string_value, top_k=dim + 1
        )
        # Konversi ke one-hot
        outputs[transformed_name(key)] = convert_num_to_one_hot(
            int_value, num_labels=dim + 1
        )
    
    # Handle numerical features
    for feature in NUMERICAL_FEATURES:
        # Pastikan input adalah float
        float_value = tf.cast(inputs[feature], tf.float32)
        outputs[transformed_name(feature)] = tft.scale_to_0_1(float_value)
    
    # Handle label
    # Asumsikan label sudah berupa integer (0 atau 1)
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    
    return outputs
