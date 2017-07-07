import tensorflow as tf
state = tf.Variable(0)
one = tf.constant(1)
new_value = tf.add(state, one)
result = tf.assign(state,new_value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(result)
        print(sess.run(state))