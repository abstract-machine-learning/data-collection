# Data Collection
Collection of datasets, ready-to-use trained classifiers and various utility tools. Data is grouped by *domains* folders (e.g. *iris*, *mnist*...), each one containg at least a *dataset* subfolder. Each directory contains at least the original dataset(s), and possibly normalized dataset(s). See [Dataset format](#dataset-format) for more details about the dataset format. Each domain folder may also contain a *models* folder containing various trained model, grouped by type (e.g. *SVM*, *Random Forest*...). Data includes SVM classifiers for [SAVer](https://github.com/abstract-machine-learning/saver) and [silva](https://github.com/abstract-machine-learning/silva).

Every data is compressed into a zip archive to save space. You can extract everything you need manually, or use the provided PHP script to extract all of the data within a specified directory:

    python3 data-manager.py decompress domains/mnist/datasets
will extract every dataset in the MNIST domain.


## Using data-manager.py
*data-manager.py* is a small Python script which makes compression/decompression of datasets and models easier. It currently supports three modes: *compress*, *decompress* and *clear* and operates (recursively) on a given path. *compress* transforms every file into a zip archive and deletes original file, *decompress* does the opposite (although preserving the zip archive). *clear* deleted every non-archive file.


## Dataset format
Data sets are comma-separated-values (CSV) files in the following format:

    # <number of samples> <feature space size>
    label,value-1,...,value-M
    label,value-1,...,value-M
    ...
    label,value-1,...,value-M
First row begins with a *#* and shows number of samples and size of the feature space, that is, number of components for each sample. Actual data is stored in the following rows, one per sample, consisting in the label followed by the values of the components of the vector representing the sample. See our [Iris dataset](https://github.com/svm-abstract-verifier/data-collection/blob/master/domains/iris/datasets/data-set.csv.zip) for an easy-to-read example. More precisely, a dataset must at least be valid with respect to the following regular expression:

    \# \d* \d*(\n\w*(,-?\d*.?\d*)*)*
with the additional constraints that number of rows and columns must match those indicated in the header.
