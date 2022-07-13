# TENSORFLOW HELLOWORLD (adaptado de https://www.codegrepper.com/code-examples/python/AttributeError%3A+module+%27tensorflow%27+has+no+attribute+%27Session%27 )

import tensorflow as tf
# Para evitar o erro -> AttributeError: module 'tensorflow' has no attribute 'Session' tem que se acrescentar a linha seguinte
tf.compat.v1.disable_eager_execution() # https://www.codegrepper.com/code-examples/python/AttributeError%3A+module+%27tensorflow%27+has+no+attribute+%27Session%27

hello = tf.constant('Hello, TensorFlow!')

# O tensorflow requer uma sessão para executar operações e obter os seus resultados
sess = tf.compat.v1.Session()# sess é um objecto de sessão que encapsula o ambiente onde os objectos de
                              # operações são executados e os objectos de dados são avaliados.
                               #tf.compat.v1.Session() está relacionado com o erro abordado na linha 4
print(sess.run(hello))
sess.close()

# MULTIPLICAÇÃO DE MATRIZES (adaptado de https://www.programadornovato.com/instalar-tensorflow-en-windows-10/)

#tf.compat.v1.disable_eager_execution() #este comando não é necessário pois já está no código acima

# declaração das matrizes (tensores)
matrizA = tf.constant([[1,2,-3],[4,0,2]])
matrizB = tf.constant([[3,1],[2,4],[-1,5]])

# matmul é o comando para a multiplicação de matrizes (tensores) de duas ou mais dimensões
product = tf.matmul(matrizA, matrizB)

sess = tf.compat.v1.Session()

result = sess.run(product)
print ("O resultado da multiplicação da matriz [[1,2,-3],[4,0,2]] pela matriz [[3,1],[2,4],[-1,5]] é: ")
print(result)
sess.close()
