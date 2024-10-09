## End to end machine learning project
# Student Performance Prediction

![project image](images\student_perfomace.webp)

This project is a machine learning application designed to predict student performance in exams based on various input features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and reading/writing scores.

### Project Overview
The Student Performance Prediction system uses machine learning models to predict students' math scores based on multiple features related to their background and academic history. This system can help educators understand which factors are most influential on a student’s performance, helping guide interventions and improve educational outcomes.

### Dataset
The dataset contains information about students, including:

* Gender
* Race/Ethnicity
* Parental level of education
* Lunch (free/reduced/standard)
*  Test preparation course (none/completed)
* Reading score
* Writing score
These features are used to predict the math score of students.

### Project Structure
* `src/`
  * `pipeline/`
    * `predict_pipeline.py`: Handles the prediction process.
    * `train_pipeline.py`: Handles model training.
* `exception.py`: Custom exception handling.
* `logger.py`: Logging configuration.
* `utils.py`: Helper functions for saving and loading objects.
* `components/`
  * `data_transformation.py`: Handles data preprocessing and transformation.
  * `data_ingestion.py`
  * `model_trainer.py`
* `artifacts/`: Stores artifacts like the model and preprocessor.
* `templates/`: Contains HTML templates for the web app.
* `app.py`: The Flask web application.
* `requirements.txt`: Dependencies list.
* `README.md`: Project documentation.
