# method-SAUVOLA
Sauvola method uses integral images for fast computation of the threshold function.

Sauvola thresholds are local thresholding technique that are useful for images where the background is not uniform, especially for text recognition. Instead of calculating a single global threshold for the entire image, several thresholds are calculated for every pixel by using specific formulae that take into account the mean and standard deviation of the local neighborhood (defined by a window centered around the pixel).

