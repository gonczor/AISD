import os

TEST_NUMBER_POINTS = 15
DATA_INCREASE_STEP = 100
SIZES = (i * DATA_INCREASE_STEP for i in range(1, 16, ))
DATA_DIRECTORY_NAME = os.path.join('Struktury', 'data')
MEASUREMENT_DIRECTORY_NAME = os.path.join('Struktury', 'measurement')
