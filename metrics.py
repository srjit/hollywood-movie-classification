import numpy as np
import pandas as pd


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


def accuracy(actual, predicted):
    
    actual_ = pd.Series(list(actual), name="actual")
    pred_ = pd.Series(list(predicted), name="pred")

    y_df = pd.concat([actual_, pred_], axis=1)
    correctly_classified = y_df[y_df.actual == y_df.pred]

    return round(float(len(correctly_classified))/len(actual_),3)


def aphr_bingo(actual, predicted):

    actual_ = pd.Series(list(actual), name="actual")
    pred_ = pd.Series(list(predicted), name="pred")

    y_df = pd.concat([actual_, pred_], axis=1)
    count_bingo = len(y_df[y_df.actual == y_df.pred])
    
    unique_classes = np.unique(actual)
    correctly_classified_instances = []
    class_averages = []

    for classid in unique_classes:
        tmp = y_df[y_df.actual == classid]
        correctly_classified_instances.append(len(tmp))

        correct_pred = tmp[tmp.actual == tmp.pred]
        ratio = float(len(correct_pred))/len(tmp)
        class_averages.append(ratio)

    aphr_bingo = sum(correctly_classified_instances)/len(unique_classes)
    percent_bingo = round(sum(class_averages)/len(unique_classes),3)
    return count_bingo, aphr_bingo, percent_bingo
    


def aphr_oneaway(actual, predicted):

    actual_ = pd.Series(list(actual), name="actual")
    pred_ = pd.Series(list(predicted), name="pred")

    y_df = pd.concat([actual_, pred_], axis=1)

    oneaway_dict = {1:[1,2], 2:{1,2,3}, 3:{2,3,4},
                    4:{3,4,5}, 5:{4,5,6}, 6:{5,6,7},
                    7:{6,7,8}, 8:{7,8,9}, 9:{8,9}}

    def is_one_away(a, p):
        one_away = 0
        if(a in oneaway_dict[p]):
            one_away = 1
        return one_away

    y_df["correct_pred"] = y_df.apply(lambda row: is_one_away(row["actual"], row["pred"]), axis=1)
    oneaway = round(float(sum(y_df["correct_pred"]))/len(y_df["correct_pred"]), 4)

    return oneaway
    

    
    



    
    
