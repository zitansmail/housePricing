from flask import Flask,request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    filename = 'BostonHousePricing.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    rm ,ptratio, lstat = request.args.get('rm'), request.args.get('ptratio'), request.args.get('lstat')
    x = np.array([rm, ptratio, lstat]).reshape(1,3)
    return str(loaded_model.predict(x)[0])
    #return 'works'


if __name__ == "__main__":
    app.run()