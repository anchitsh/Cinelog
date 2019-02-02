import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from tensorflow.contrib import learn
from sklearn.metrics import mean_squared_error, mean_absolute_error
from lstm_predictor import generate_data, load_csvdata, lstm_model
from tensorflow.contrib.learn.python import SKCompat

def predict_done():
	LOG_DIR = './ops_logs'
	TIMESTEPS = 10
	RNN_LAYERS = [{'num_units': TIMESTEPS}]
	DENSE_LAYERS = [10, 10]
	TRAINING_STEPS = 1000
	BATCH_SIZE = 100
	PRINT_STEPS = TRAINING_STEPS / 100

	dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y %H:%M')
	rawdata = pd.read_csv("./model/input/ElectricityPrice/RealMarketPriceDataPT.csv",
			parse_dates={'timeline': ['date', '(UTC)']},
			index_col='timeline', date_parser=dateparse)


	X, y = load_csvdata(rawdata, TIMESTEPS, seperate=False)


	regressor = SKCompat(learn.Estimator(model_fn=lstm_model(TIMESTEPS, RNN_LAYERS, DENSE_LAYERS),))


	validation_monitor = learn.monitors.ValidationMonitor(X['val'], y['val'],
						      every_n_steps=PRINT_STEPS,
						      early_stopping_rounds=1000)

	SKCompat(regressor.fit(X['train'], y['train'],
			monitors=[validation_monitor],
			batch_size=BATCH_SIZE,
			steps=TRAINING_STEPS))

	predicted = regressor.predict(X['test'])
	mse = mean_absolute_error(y['test'], predicted)

	plot_predicted, = plt.plot(predicted, label='predicted')
	plt.legend(handles=[plot_predicted])

	plt.show()