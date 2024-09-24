import sys
import os
from datetime import datetime

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_tranformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]

            )

            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("encoder",OneHotEncoder(handle_unknown='ignore'))

                ]
            )

            logging.info("numerical columns are encoded and scaling completed")

            logging.info("categorical columns are scaled")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completed")

            logging.info("obtaining preprocessor object")

            preprocessing_obj=self.get_data_transformer_object()

            target_columns_name="math_score"
            numerical_columns=["writing_score","reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_columns_name],axis=1)
            target_faeture_train_df=train_df[target_columns_name]

            input_feature_test_df=test_df.drop(columns=[target_columns_name],axis=1)
            target_faeture_test_df=test_df[target_columns_name]

            logging.info(f"applying preprocessing object on training dataframe and test dataframe")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,np.array(target_faeture_train_df)   
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_faeture_test_df)
            ]

            logging.info(f"saved processing object")

            save_object(
                file_path=self.data_tranformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_tranformation_config.preprocessor_obj_file_path,

            )
        except Exception as e:
            raise CustomException(e,sys)
            