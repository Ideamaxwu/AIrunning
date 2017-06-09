import tensorflow as tf
a = tf.constant(2)
b = tf.constant(3)
with tf.Session() as sess:
	print("a=2, b=3")
	print("Add: %i" % sess.run(a + b))
	print("Mul: %i" % sess.run(a * b))
	
m1 = tf.constant([[3., 3.]])
m2 = tf.constant([[2.], [2.]])
product = tf.matmul(m1, m2)
with tf.Session() as sess:
	result = sess.run(product)
	print(result)
