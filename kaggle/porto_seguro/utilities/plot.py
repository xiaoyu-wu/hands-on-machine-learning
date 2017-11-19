import matplotlib.pyplot as plt
import numpy as np

def hist_with_target(data, feature, target, feature_devide=1):
    """ Plots histogram of specified feature with target value
    """
    data_copy = data.loc[:, [feature, target]]
    target_values = sorted(data[target].value_counts().index.values)
    data_copy['feature_cat'] = np.ceil(data_copy[feature] / float(feature_devide))
    fig, ax = plt.subplots()
    for target_value in target_values:
        vc = data_copy.loc[data_copy[target] == target_value, 'feature_cat'].value_counts()
        ax.bar(vc.index.values, vc.values)

def hist_ratio_with_target(data, feature, target, feature_devide=1, target_value_of_interest=1):
    """ Plots histogram of specified feature with target value
    """
    data_copy = data.loc[:, [feature, target]]
    data_copy['feature_cat'] = np.ceil(data_copy[feature] / float(feature_devide))
    fig, ax = plt.subplots()
    vc_1 = data_copy.loc[data_copy[target] == target_value_of_interest, 'feature_cat'].value_counts()
    vc_all = data_copy['feature_cat'].value_counts()
    ratio = vc_1 / vc_all
    ax.bar(ratio.index.values, ratio.values)
    return ratio
