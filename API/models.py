from keras.models import load_model


def load_model_summarization(text):
    '''
    Loading the model from the HDF5 file 
    '''

    try:
        model = load_model('sum_model.h5')


        predicted_output = model.predict(text)
    except:
        predicted_output = None
    return predicted_output


def load_model_truth_detection(text):
    '''
    Loading the model from the HDF5 file 
    '''

    try:
        model = load_model('dec_model.h5')


        predicted_output = model.predict(text)
    except:
        predicted_output = None
    return predicted_output