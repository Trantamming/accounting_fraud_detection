# from setuptools import setup, find_packages

# setup(
#     name="fraud_detection",
#     version="0.1",
#     packages=find_packages(),
#     install_requires=[
#         "pandas",
#         "scikit-learn",
#         "joblib"
#     ],
#     entry_points={
#         "console_scripts": [
#             "train_fraud_model=fraud_detection.model:train_and_save_model",
#             "predict_fraud=fraud_detection.predict:predict_fraud"
#         ],
#     },
#     author="Trần Minh Tâm",
#     description="Package phát hiện gian lận kế toán",
# )



from setuptools import setup, find_packages

setup(
    name="fraud-detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "joblib",
    ],
    author="Trần Minh Tâm",
    author_email="tam.ming.zhan@gmail.com",
    description="AI phát hiện gian lận kế toán",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/fraud-detection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
