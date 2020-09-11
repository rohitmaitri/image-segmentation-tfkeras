from setuptools import find_packages, setup


setup(name="keras_segmentation",
      version="0.3.0",
      description="Image Segmentation toolkit for keras",
      author="Divam Gupta",
      author_email='divamgupta@gmail.com, rohitmaitri@gmail.com',
      platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
      license="GPLv3",
      url="https://github.com/rohitmaitri/image-segmentation-tfkeras",
      packages=find_packages(exclude=["test"]),
      entry_points={
            'console_scripts': [
                  'keras_segmentation = keras_segmentation.__main__:main'
            ]
      },
      install_requires=[
            "imgaug==0.2.9",
            "opencv-python",
            "tqdm"],
      extras_require={
            # These requires provide different backends available with Keras
            "tensorflow": ["tensorflow"],
            "cntk": ["cntk"],
            "theano": ["theano"],
            # Default testing with tensorflow
            "tests-default": ["tensorflow", "pytest"]
      }
)
