from sklearn_whiskers.ouliers import WhiskerOutliers
from sklearn.utils.estimator_checks import check_estimator

# starting to set up test the procedures
check_estimator(WhiskerOutliers())
