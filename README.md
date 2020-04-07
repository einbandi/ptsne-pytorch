ptsne-pytorch
==============================

PyTorch implementation of parametric t-SNE.

While the code was initially based on a [TensorFlow implementation by jsilter](https://github.com/jsilter/parametric_tsne),
everything is now implemented from scratch, including PCA pretraining and different metrics for comparison of probability distributions.

This version of parametric t-SNE makes use of [`pynndescent`](https://github.com/lmcinnes/pynndescent/tree/master/pynndescent)
to approximate nearest neighbors for an efficient calculation of an approximated distance matrix.
This approach as well as the PCA pretraining are borrowed from the [openTSNE package](https://opentsne.readthedocs.io/en/latest/index.html).
